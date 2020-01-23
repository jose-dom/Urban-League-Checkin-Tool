from django.db import models
from django.core import validators
from django import forms
import datetime
from multiselectfield import MultiSelectField
##Models

##Transaction
class Visit(models.Model):
    first_name = models.CharField(max_length=3000, default="", verbose_name="First Name")
    last_name = models.CharField(max_length=3000, default="", verbose_name="Last Name")
    email = models.EmailField(max_length=3000, default="", verbose_name="Email")
    gender = models.CharField(max_length=3000, default="", verbose_name="Gender")
    address = models.CharField(max_length=3000, default="", verbose_name="Address")
    city = models.CharField(max_length=3000, default="", verbose_name="City")
    uid = models.CharField(max_length=3000, default="", verbose_name="User ID#")
    date = models.CharField(max_length=3000, default="", verbose_name="Date")
    time =  models.CharField(max_length=3000, default="", verbose_name="Timestamp")
    referral = models.CharField(max_length=3000, default="", verbose_name="Referral")
    phone_number = models.CharField(max_length=10, default="", verbose_name="Main Phone Number")
    purpose = models.CharField(max_length=3000, default="", verbose_name="Purpose")
    household_number = models.CharField(max_length=3000, default="", verbose_name="Number of People in Household")
    household_income = models.CharField(max_length=3000, default="", verbose_name="Household Income")
    race = models.CharField(max_length=3000, default="", verbose_name="Ethnicity")
    dob  = models.CharField(max_length=3000, default="", verbose_name="Date of Birth")
    veteran = models.CharField(max_length=3000, default="", verbose_name="Veteran Status")
    disabled = models.CharField(max_length=3000, default="", verbose_name="Disabled Status")
    marital_status = models.CharField(max_length=3000, default="", verbose_name="Marital Status")
    major_purpose = models.CharField(max_length=3000, default="", verbose_name="Major Purpose")

    def __str__(self):
        return self.first_name

class Visitor(models.Model):
    first_name = models.CharField(max_length=3000, verbose_name="First Name", blank=False)
    last_name = models.CharField(max_length=3000, verbose_name="Last Name", blank=False)
    email = models.EmailField(max_length=3000,verbose_name="Email", blank=False)
    phone_number = models.CharField(max_length=10, verbose_name="Main Phone Number", blank=False)
    address = models.CharField(max_length=3000, verbose_name="Address", blank=False)
    city = models.CharField(max_length=3000, verbose_name="City", blank=False)

    referral_choices = [
        ("Friend", "Friend"),
        ("Online Advertisement", "Online Advertisement"),
        ("Other", "Other"),
    ]
    referral = models.CharField(max_length=3000, choices=referral_choices, verbose_name="How did you hear about our services?", blank=True)

    options1 = (
        ("Job Placement Assistance", 'Job Placement Assistance'),
        ("Resume Preparation", 'Resume Preparation'),
        ("Mock Interviewing", 'Mock Interviewing'),
        ("Career Counseling",'Career Counseling'),
    )
    options2 = (
        ("Construction", 'Construction'),
        ("Pre-Apprenticeship", 'Pre-Apprenticeship'),
        ("Microsoft Office Certification", 'Microsoft Office Certification'),
        ("A+ certification",'A+ certification'),
        ("paintWorks",'paintWorks'),
    )
    options3 = (
        ("Public Income Benefits Screening",'Public Income Benefits Screening'),
        ("Financial Workshop",'Financial Workshop'),
        ("Financial Coaching",'Financial Coaching '),
    )
    options4 = (
        ("Start Saving on a Shoestring",'Start Saving on a Shoestring'),
        ("Early Career Guide to Becoming Financially Fit",'Early Career Guide to Becoming Financially Fit'),
        ("MoneyWISE is a Family Affair)",'MoneyWISE is a Family Affair'),
        ("Managing Credit and Debt - The RIGHT Way",'Managing Credit and Debt - The RIGHT Way'),
        ("Protecting Your Assets; Protecting Your Family",'Protecting Your Assets; Protecting Your Family'),
    )
    options5 = (
        ("Rental Assistance / Counseling",'Rental Assistance / Counseling'),
        ("First Time Homebuyer Counseling",'First Time Homebuyer Counseling'),
        ("Foreclosure Counseling",'Foreclosure Counseling'),
        ("Post Purchase Counseling",'Post Purchase Counseling'),
    )
    options6 = (
        ("High School Equivalency Program",'High School Equivalency Program'),
        ("Job Readiness",'Job Readiness'),
        ("Career Preparation",'Career Preparation'),
    )
    options7= (
        ("Early Childhood Center",'Early Childhood Center'),
        ("Newark Kids Code",'Newark Kids Code'),
    )
    options8 = (
        ("Youth Programs",'Youth Programs'),
        ("Adult Programs",'Adult Programs'),
        ("Early Childhood",'Early Childhood'),
    )
    options9 = (
        ("Food Referral", 'Food Referral'),
        ("Computer Lab", 'Computer Lab'),
        ("Make Copies", 'Make Copies'),
        ("Other", 'Other')
    )
    purpose1 = MultiSelectField(choices=options1, default="None", verbose_name="<strong>Employment Assistance</strong>", blank=True)
    purpose2 = MultiSelectField(choices=options2, default="None", verbose_name="<strong>Training Programs</strong>", blank=True)
    purpose3 = MultiSelectField(choices=options3, default="None", verbose_name="<strong>Financial Information</strong>", blank=True)
    purpose4 = MultiSelectField(choices=options4, default="None", verbose_name="<strong>Workshops</strong>", blank=True)
    purpose5 = MultiSelectField(choices=options5, default="None", verbose_name="<strong>Housing or Rental Assistance</strong>", blank=True)
    purpose6 = MultiSelectField(choices=options6, default="None", verbose_name="<strong>Young Adult Programs / Youth Programs</strong>", blank=True)
    purpose7 = MultiSelectField(choices=options7, default="None", verbose_name="<strong>Youth Education</strong>", blank=True)
    purpose8 = MultiSelectField(choices=options8, default="None", verbose_name="<strong>Volunteering</strong>", blank=True)
    purpose9 = MultiSelectField(choices=options9, default="None", verbose_name="<strong>Other</strong>", blank=True)
    major_purpose = models.CharField(max_length=264, default="None", verbose_name="Major Purpose")

    choices = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]
    gender = models.CharField(max_length=100, choices=choices, verbose_name="Gender", blank=False)

    ##Additional Info
    nums = [
        ("0", '0'),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5 or above", "5 or above"),
    ]
    household_number = models.CharField(max_length=3000, choices=nums, verbose_name="Number of People in Household", blank=False)

    dob = models.CharField(max_length=10, help_text='Please provide in the following format: MM/DD/YYY', verbose_name="Date of Birth", blank=False)

    race_choices = [
        ("White", "White"),
        ("Black/Afro America", "Black/Afro American"),
        ("Hispanic", "Hispanic"),
        ("Asian", "Asian"),
        ("Mixed", "Mixed"),
        ("Other", "Other"),
    ]

    race = models.CharField(max_length=3000, choices=race_choices, verbose_name="Ethnicity", blank=False)

    status = [
        ("Single","Single"),
        ("Divorced","Divorced"),
        ("Widowed","Widowed"),
        ("Married","Married"),
    ]

    marital_status = models.CharField(max_length=3000, choices=status, verbose_name="Matrial Status", blank=False)

    income = [
        ("under $25,000",'under $25,000'),
        ("$25,000 - $35,000",'$25,000 - $35,000'),
        ("$35,000 - $45,000",'$35,000 - $45,000'),
        ("$45,000 - $55,000",'$45,000 - $55,000'),
        ("$55,000 - $65,000",'$55,000 - $65,000'),
        ("$65,000 - $75,000",'$65,000 - $75,000'),
        ("$75,000 - $85,000",'$75,000 - $85,000'),
        ("over $85,000",'over $85,000'),
    ]

    household_income = models.CharField(max_length=100, choices=income, verbose_name="Household Income", blank=False)

    binary = [
        ("Yes","Yes"),("No","No")
    ]

    veteran = models.CharField(max_length=100, choices=binary, verbose_name="Are you a Veteran?", blank=False)

    disabled = models.CharField(max_length=100, choices=binary, verbose_name="Are you Disabled?", blank=False)

    def __str__(self):
        return self.first_name