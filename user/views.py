from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.db import IntegrityError
from django.contrib import messages
import re
from django.contrib.auth.models import User
from company.models import Company, CompanyMembership
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe

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
    datapack = {}
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
        datapack = {
                "fname": fname,
                "lname": lname,
                "email": email,
                "phone_number": phone_number,
            }
        if errors:
            for error in errors:
                messages.warning(request, error)  
        else:
            try:
                User = get_user_model()
                if User.objects.filter(email=email).exists():
                    messages.warning(request, mark_safe('Email is already in use. <a href="/profile/login">Log in</a> instead.'))
                
                else:
                    user = User.objects.create_user(
                        username=f"{fname}_{lname}",
                        first_name=fname,
                        last_name=lname,
                        email=email,
                        password= password1,
                        phone_number=phone_number,
                    )
                    user.save()
                    return redirect('/home') # needs to be changed to the user dash board

            except IntegrityError as e:
                messages.warning(request, f"Integrity Error: {e}")
    print(datapack)
    return render(request, 'user/register.html', {"datapack": datapack})


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

def createcompany(request):
    auth = userAuth(request)
    # needs MFA
    if auth:
        return auth
    if request.method == 'POST':
        name = request.POST['companyname']
        try:
            Company.objects.get(name=name)
            context = {'error':'Company Name is already used.'}
            return render(request, 'user/newcompany.html', context)
        except ObjectDoesNotExist:
            Company.objects.create(
                name=name,
                leadAdmin=request.user
            )
            # return redirect(Company)
    
    return render(request, 'user/newcompany.html', {'error':''})

def joinGroup(request):
    auth = userAuth(request)
    if auth:
        return auth
    if request.method == 'POST':
        companyid = request.POST['companyid']
        try:
            addedCompany = Company.objects.get(id=companyid)
            try:
                CompanyMembership.objects.get(company=addedCompany, user=request.user)
                
            except ObjectDoesNotExist:
                CompanyMembership.objects.create(company=addedCompany, user=request.user)
        except ObjectDoesNotExist:
            print("obj not exist")
    companies = Company.objects.all()
    usercompanies = CompanyMembership.objects.filter(user=request.user)
    return render(request, 'user/companies.html', {'companies': companies, 'usercompanies': usercompanies})
    
