from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.db import IntegrityError
from django.contrib import messages
import re


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

def userAuth(request):
    if request.user.is_authenticated:
        return
    else:
        return render(request, "main/notSignedIn.html")
    
def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        # username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        userdata = {
            'fname': fname,
            'lname': lname,
            'email': email,
            'phone_number': phone_number,
            'match_password': [password1, password2]
        }
        errors = validate(userdata)
        if errors:
            pass
           #messages.warning(request, f'There were the following errors: {", \n".join(errors)}')  
        else:
            try:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'This email already exists, do you mean to <a href="google.com">log in</a>')

                User = get_user_model()

                user = User.objects.create_user(
                    username=f"{fname}_{lname}",
                    first_name=fname,
                    last_name=lname,
                    email=email,
                    password= password1,
                    phone_number=phone_number,
                )
                user.save()

            except IntegrityError as e:
                messages.warning(request, f"Integrity Error: {e}")
        
    return render(request, 'register.hmtl')


def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            context = {'error':'Invalid username or password.'}
            return render(request, 'user/login.html', context)
    return render(request, 'user/login.html', {'error':''})

def profile(request):
    auth = userAuth(request)
    if auth:
        return auth
    return 

def settings(request):
    auth = userAuth(request)
    if auth:
        return auth
    return
    
def payments(request):
    auth = userAuth(request)
    # needs MFA
    if auth:
        return auth
    return

