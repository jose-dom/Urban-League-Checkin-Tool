from django.shortcuts import render, redirect
from .forms  import NewUserForm
from .models import Visitor, Visit
from django.contrib import messages
import datetime
import uuid

##Second Form
'''
def index(request):
    form = FirstTimeUserForm()
    first_name, last_name, email, purpose1, purpose2, purpose3, purpose4, purpose5, purpose6, purpose7, purpose8, time = request.session['first_name'], request.session['last_name'], request.session['email'], request.session['purpose1'], request.session['purpose2'], request.session['purpose3'], request.session['purpose4'], request.session['purpose5'], request.session['purpose6'], request.session['purpose7'], request.session['purpose8'], request.session['time']
    if request.method == "POST":
        form = FirstTimeUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            visitor = Visitor.objects.order_by()[len(Visitor.objects.order_by())-1]
            address = visitor.address
            gender = visitor.gender
            referral = visitor.referral

            for p in purpose1:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    uid=str(uuid.uuid1()), time=time,
                    referral=referral, purpose=p
                )
                t.save()
            for p in purpose2:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    uid=str(uuid.uuid1()), time=time,
                    referral=referral, purpose=p
                )
                t.save()
            for p in purpose3:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    uid=str(uuid.uuid1()), time=time,
                    referral=referral, purpose=p
                )
                t.save()
            for p in purpose4:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    uid=str(uuid.uuid1()), time=time,
                    referral=referral, purpose=p
                )
                t.save()
            for p in purpose5:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    uid=str(uuid.uuid1()), time=time,
                    referral=referral, purpose=p
                )
                t.save()
            for p in purpose6:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    uid=str(uuid.uuid1()), time=time,
                    referral=referral, purpose=p
                )
                t.save()
            for p in purpose7:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    uid=str(uuid.uuid1()), time=time,
                    referral=referral, purpose=p
                )
                t.save()
            for p in purpose8:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    uid=str(uuid.uuid1()), time=time,
                    referral=referral, purpose=p
                )
                t.save()


        messages.success(request, f'You have successfully checked in!')
        return redirect('user')

    return render(request, 'visitors/index.html', context={'form': form})
'''

##First Form
def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            visitor = Visitor.objects.order_by()[len(Visitor.objects.order_by())-1]
            first_name = visitor.first_name
            last_name = visitor.last_name
            email = visitor.email
            address = visitor.address
            phone_number = visitor.phone_number
            city = visitor.city
            gender = visitor.gender
            referral = visitor.referral

            ##Additional Fields
            dob = visitor.dob
            household_income = visitor.household_income
            household_number = visitor.household_number
            race = visitor.race
            marital_status = visitor.marital_status
            veteran = visitor.veteran
            disabled = visitor.disabled
            
            ##Purpose
            purpose1 = visitor.purpose1
            purpose2 = visitor.purpose2
            purpose3 = visitor.purpose3
            purpose4 = visitor.purpose4
            purpose5 = visitor.purpose5
            purpose6 = visitor.purpose6
            purpose7 = visitor.purpose7
            purpose8 = visitor.purpose8
            purpose9 = visitor.purpose9

            currentDT = datetime.datetime.now()
            date = str(currentDT.strftime("%m/%d/%Y"))
            time = str(currentDT.strftime("%I:%M:%S %p"))
            '''
            if (purpose1 == "None") and (purpose2 == "None") and (purpose3 =="None") and (purpose4 == "None") and (purpose5 == "None") and (purpose6 == "None") and (purpose7 == "None") and (purpose8 == "None"):
                messages.warning(request, f'Error! Please fill out the form completely and select a purpose for coming in')
            else:
                print(purpose1)
            '''
            for p in purpose1:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    city=city, uid=str(uuid.uuid1()), date=date, time=time,
                    referral=referral, purpose=p, major_purpose="Employment Assistance",
                    phone_number=phone_number, dob=dob, household_income=household_income,
                    household_number=household_number, race=race,
                    marital_status=marital_status, veteran=veteran, disabled=disabled
                    )
                t.save()
            for p in purpose2:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    city=city, uid=str(uuid.uuid1()), date=date, time=time,
                    referral=referral, purpose=p, major_purpose="Training Programs",
                    phone_number=phone_number, dob=dob, household_income=household_income,
                    household_number=household_number, race=race,
                    marital_status=marital_status, veteran=veteran, disabled=disabled
                    )
                t.save()
            for p in purpose3:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    city=city, uid=str(uuid.uuid1()), date=date, time=time,
                    referral=referral, purpose=p, major_purpose="Financial Information",
                    phone_number=phone_number, dob=dob, household_income=household_income,
                    household_number=household_number, race=race,
                    marital_status=marital_status, veteran=veteran, disabled=disabled
                    )
                t.save()
            for p in purpose4:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    city=city, uid=str(uuid.uuid1()), date=date, time=time,
                    referral=referral, purpose=p, major_purpose="Workshops",
                    phone_number=phone_number, dob=dob, household_income=household_income,
                    household_number=household_number, race=race,
                    marital_status=marital_status, veteran=veteran, disabled=disabled
                    )
                t.save()
            for p in purpose5:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    city=city, uid=str(uuid.uuid1()), date=date, time=time,
                    referral=referral, purpose=p, major_purpose="Housing or Rental Assistance",
                    phone_number=phone_number, dob=dob, household_income=household_income,
                    household_number=household_number, race=race,
                    marital_status=marital_status, veteran=veteran, disabled=disabled
                    )
                t.save()
            for p in purpose6:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    city=city, uid=str(uuid.uuid1()), date=date, time=time,
                    referral=referral, purpose=p, major_purpose="Young Adult Programs / Youth Programs",
                    phone_number=phone_number, dob=dob, household_income=household_income,
                    household_number=household_number, race=race,
                    marital_status=marital_status, veteran=veteran, disabled=disabled
                    )
                t.save()
            for p in purpose7:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    city=city, uid=str(uuid.uuid1()), date=date, time=time,
                    referral=referral, purpose=p, major_purpose="Youth Education",
                    phone_number=phone_number, dob=dob, household_income=household_income,
                    household_number=household_number, race=race,
                    marital_status=marital_status, veteran=veteran, disabled=disabled
                    )
                t.save()
            for p in purpose8:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    city=city, uid=str(uuid.uuid1()), date=date, time=time,
                    referral=referral, purpose=p, major_purpose="Volunteering",
                    phone_number=phone_number, dob=dob, household_income=household_income,
                    household_number=household_number, race=race,
                    marital_status=marital_status, veteran=veteran, disabled=disabled
                    )
                t.save()
            for p in purpose9:
                t = Visit(
                    first_name=first_name, last_name=last_name,
                    email=email, gender=gender, address=address,
                    city=city, uid=str(uuid.uuid1()), date=date, time=time,
                    referral=referral, purpose=p, major_purpose="Other",
                    phone_number=phone_number, dob=dob, household_income=household_income,
                    household_number=household_number, race=race,
                    marital_status=marital_status, veteran=veteran, disabled=disabled
                    )
                t.save()
            messages.success(request, f'You have successfully checked in!')
            return redirect('user')
        else:
            print('ERROR FORM INVALID')
            messages.warning(request, f'Error! Please fill out the form completely and select a purpose for coming in')
    return render(request, 'visitors/users.html', {'form': form})
