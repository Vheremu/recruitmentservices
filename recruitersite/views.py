import time,datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Vaccancy
from django.contrib.auth.models import User
def index(request):
    user=request.user
    vaccancies=0
    try:
        vaccancies=Vaccancy.objects.filter(user=user)
        print('vacancies found')
    except:
        print('failed to get vaccancies')
        vaccancies=0
    my_dict = {'vaccancies':vaccancies}
    return render(request,'recruitersite/index.html',context=my_dict)
def expired(request):
    now = datetime.datetime.now()
    user=request.user
    vaccancies=0
    buffer=set()
    try:
        vaccancies=Vaccancy.objects.filter(user=user)
        for vaccancy in vaccancies:
            expiry_date = datetime.datetime(vaccancy.expiry_date.year,vaccancy.expiry_date.month,vaccancy.expiry_date.day,vaccancy.expiry_date.hour,vaccancy.expiry_date.minute,vaccancy.expiry_date.second)
            time_left=expiry_date-now
            if int(time_left.total_seconds())<=0:
                buffer.add(vaccancy)
        print('vacancies found')
        
    except:
        print('failed to get vaccancies')
        vaccancies=0
    print(buffer)
    vaccancies=buffer
    my_dict = {'vaccancies':vaccancies}
    return render(request,'recruitersite/expired.html',context=my_dict)
def active(request):
    now = datetime.datetime.now()
    user=request.user
    vaccancies=0
    buffer=set()
    try:
        vaccancies=Vaccancy.objects.filter(user=user)
        for vaccancy in vaccancies:
            expiry_date = datetime.datetime(vaccancy.expiry_date.year,vaccancy.expiry_date.month,vaccancy.expiry_date.day,vaccancy.expiry_date.hour,vaccancy.expiry_date.minute,vaccancy.expiry_date.second)
            time_left=expiry_date-now
            if int(time_left.total_seconds())>=0:
                buffer.add(vaccancy)
        print('vacancies found')
        
    except:
        print('failed to get vaccancies')
        vaccancies=0
    print(buffer)
    vaccancies=buffer
    my_dict = {'vaccancies':vaccancies}
    return render(request,'recruitersite/active.html',context=my_dict)
def view(request):
    vaccancy=request.POST.get('vaccancy')
    vaccancy=Vaccancy.objects.get(vaccancyid=int(vaccancy))
    my_dict = {'vaccancy':vaccancy}
    return render(request,'recruitersite/view.html',context=my_dict)
def add(request):
    
    if request.POST:
        now = datetime.datetime.now()
        title=request.POST.get('title')
        employment_type=request.POST.get('employment_type')
        expiry_date=request.POST.get('expiry_date')
        recruiter=request.POST.get('recruiter')
        location=request.POST.get('location')
        duration=request.POST.get('duration')
        responsibilities=request.POST.get('responsibilities')
        attributes=request.POST.get('attributes')
        requirements=request.POST.get('requirements')
        offer=request.POST.get('offer')
        if not title or not expiry_date or not employment_type:
            errorss=1
            my_dict = {'errorss':errorss,'title':title,'employment_type':employment_type,'recruiter':recruiter,'location':location,'duration':duration,'responsibilities':responsibilities,'attributes':attributes,'requirements':requirements,'offer':offer}
            return render(request,'recruitersite/add.html',context=my_dict)
        else:
            try:
                
                vaccancy=Vaccancy.objects.create(user=request.user,title=title,date_posted=now,expiry_date=expiry_date,recruiter=recruiter,employmenttype=employment_type,location=location,dutation=duration,responsibilities=responsibilities,attributes=attributes,requirements=requirements,offer=offer)
                print('vaccancy added while logged in')
            except:
                
                user=User.objects.get(id=1)
                vaccancy=Vaccancy.objects.create(user=user,title=title,date_posted=now,expiry_date=expiry_date,recruiter=recruiter,employmenttype=employment_type,location=location,dutation=duration,responsibilities=responsibilities,attributes=attributes,requirements=requirements,offer=offer)
                print('vaccancy added while logged out')
            success=1
            my_dict = {'success':success,'vaccancy':vaccancy}
            return render(request,'recruitersite/add.html',context=my_dict)
    my_dict = {}
    return render(request,'recruitersite/add.html',context=my_dict)
