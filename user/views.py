from django.shortcuts import render, HttpResponse, redirect
from django.db import IntegrityError
from django.contrib import messages
import re
from django.contrib.auth.models import User
from company.models import Company, CompanyMembership
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
    
@login_required
def profile(request):
    return render(request, "user/profiledashboard.html")


@login_required
def settings(request):
    return render(request, "user/settings.html")

@login_required
def payments(request):
    return


@login_required
def createcompany(request):
   # need MFA
    if request.method == 'POST':
        name = request.POST['companyname']
        try:
            Company.objects.get(name=name)
            context = {'error':'Company Name is already used.'}
            return render(request, 'user/newcompany.html', context) # this section checks if the company name already exists
        except ObjectDoesNotExist:# if it does not exist
            newcompany = Company.objects.create( # it creates a new company
                name=name,
                leadAdmin=request.user
            )
            CompanyMembership.objects.create(
                user = request.user,
                company = newcompany,
                isAdmin = True,
            ) # this is untested so far
            # TODO return redirect(Company settings) 
    
    return render(request, 'user/newcompany.html', {'error':''})


@login_required
def joinGroup(request):
    # TODO somehow we also need to make users able to leave companies
    if request.method == 'POST':
        companyid = request.POST['companyid']
        try:
            addedCompany = Company.objects.get(id=companyid) #gets the company based on the id inputed
            try:
                CompanyMembership.objects.get(company=addedCompany, user=request.user) # checks for a CompanyMembership that already is the same
            except ObjectDoesNotExist:
                CompanyMembership.objects.create(company=addedCompany, user=request.user) # creates the a CompanyMembership
        except ObjectDoesNotExist:
            print("obj not exist") # TODO needs to find a way to handle if thats not a valid company id
    companies = Company.objects.all() # all companies
    usercompanies = CompanyMembership.objects.filter(user=request.user) # all the companies the user is a part of
    return render(request, 'user/companies.html', {'companies': companies, 'usercompanies': usercompanies})

