from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.db import IntegrityError
from django.contrib import messages
import re
from django.utils.safestring import mark_safe
from public.backends import EmailBackend
from user.models import User



def validate(data):
    errorList = []

    def checkname(name, info):
        pattern = r'^[A-Za-z\s-]+$'
        # Define a regular expression pattern that allows letters and spaces
        # Use regular expressions to check if the name matches the pattern
        if re.match(pattern, name):
            pass
        else:
            errorList.append(f"Error in {info}: Names can only contain letters and spaces")
    
    def blank(var):
        return True if not var else False
        
    for info in data:
        match info:
            case 'fname':
                if blank(data[info]):
                    errorList.append(f"{info} is blank")
                else:
                    checkname(data[info], info)
            case 'lname':
                if blank(data[info]):
                    errorList.append(f"{info} is blank")
                else:
                    checkname(data[info], info)
            case 'email':
                if blank(data[info]):
                    errorList.append(f"{info} is blank")
                else:
                    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                    # Use regular expressions to check if the email matches the pattern
                    if re.match(pattern, data[info]):
                        pass
                    else:
                        errorList.append("Email is not in a valid format")
            case 'phone_number':
                if blank(data[info]):
                    errorList.append(f"{info} is blank")
                else:
                    pattern = r'^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'
                    # This pattern allows for various formats, like (123) 456-7890 or 123-456-7890
                    # idk how this works but chatgpt said its okay
                    # Use regular expressions to check if the phone number matches the pattern
                    if re.match(pattern, data[info]):
                        pass
                    else:
                        errorList.append("Invaild Phone Number Format, Acceptable Formats: (123) 456-7890 or 123-456-7890")
            case 'match_password':
                if blank(data[info]):
                    errorList.append(f"{info} is blank")
                else:
                    try:
                        if data[info][0]!=data[info][1]:
                            errorList.append('Passwords are not Equal')
                    except IndexError as e:
                        errorList.append(f"Backend Error, Please Resubmit\nError Code:{e}")

    return errorList
    
def register(request):
    # check if they are already logged in 
    # auth = userAuth(request)
    # if auth:
    #     return redirect('/profile/dashboard')
    
    datapack = {}
    if request.method == 'POST': # gets all the info from the form
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST["username"]
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        # username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        userdata = { # puts it in a dict for the validate fucntion
            'fname': fname,
            'lname': lname,
            'username': username,
            'email': email,
            'phone_number': phone_number,
            'match_password': [password1, password2]
        }
        errors = validate(userdata) # returns a list of errors
        datapack = { # this is for making sure that the data in the forms stays the same if we reload the page
                "fname": fname,
                "lname": lname,
                'username': username,
                "email": email,
                "phone_number": phone_number,
            }
        if errors: # if there are errors in the errors list
            for error in errors:
                messages.warning(request, error)  # add them to messages this is weird but somehow they go into messages.html and that gets put into the register.html page
        else:
            try:
                User = get_user_model()
                if User.objects.filter(email=email).exists(): # if the inputed email already ezists
                    messages.warning(request, mark_safe('Email is already in use. <a href="/profile/login">Log in</a> instead.')) # sends pure html
                
                else:#creates a user obj
                    user = User.objects.create_user(
                        username=username,
                        first_name=fname,
                        last_name=lname,
                        email=email,
                        password= password1,
                        phone_number=phone_number,
                    )
                    user.save()
                    login(request, user)
                    return redirect('/profile/dashboard') 

            except IntegrityError as e:
                messages.warning(request, f"Integrity Error: {e}") # this is like a real fuck up and somehow the database is not working right or we put weird data that fucked up the database in
    return render(request, 'public/register.html', {"datapack": datapack})

def home(request):
    return render(request, 'public/home.html')

def login_view(request):
    # check if they are already logged in 
    if request.user.is_authenticated:
        next_url = request.GET.get('next')
        if next_url:
            # Redirect to the URL specified in the 'next' parameter
            return redirect(next_url)
        else:
            # Redirect to users profile dashboard
            return redirect('/profile/dashboard')
        

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password = password.strip()
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                # Redirect to the URL specified in the 'next' parameter
                return redirect(next_url)
            else:
                # Redirect to users profile dashboard
                return redirect('/profile/dashboard')
        else:
            context = {'error':'Invalid username or password.'}
            return render(request, 'public/login.html', context)
    return render(request, 'public/login.html', {'error':''})
