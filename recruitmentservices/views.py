import time,datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from recruitersite.models import Vaccancy,Application,Comment,Testimonial
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
def index(request):
    
    now = datetime.datetime.now()
    user=request.user
    vaccancies=0
    buffer=set()
    try:
        vaccancies=Vaccancy.objects.all()
        for vaccancy in vaccancies:
            expiry_date = datetime.datetime(vaccancy.expiry_date.year,vaccancy.expiry_date.month,vaccancy.expiry_date.day,vaccancy.expiry_date.hour,vaccancy.expiry_date.minute,vaccancy.expiry_date.second)
            time_left=expiry_date-now
            if int(time_left.total_seconds())>=0:
                buffer.add(vaccancy)
        print('vacancies found')
        
    except:
        vaccancies=0
    vaccancies=buffer
    my_dict = {'vaccancies':vaccancies}
    return render(request,'recruitmentservices/index.html',context=my_dict)
def apply(request):
    vaccancy=request.POST.get('vaccancy')
    vaccancy=Vaccancy.objects.get(vaccancyid=int(vaccancy))
    user=request.user
    loggedin=0
    print(user.id)
    if user.id:
        loggedin=1
        
    if 'application' in request.POST:
        if 'cv' in request.FILES:
            user=0
            try:
                user=request.user
                application=Application()
                
                application.user=user
                application.cv=request.FILES['cv']
                application.vaccancy=vaccancy
                application.save()
                print('application submited while logged in')
            except:
                application=Application()
                application.cv=request.FILES['cv']
                application.vaccancy=vaccancy
                user=User.objects.get(id=1)
                application.user=user
                application.save()
                print('application submited while logged out')
            
            return HttpResponseRedirect(reverse('index'))
        else:
            error=1
            my_dict={'vaccancy':vaccancy,'error':error,'loggedin':loggedin}
            return render(request,'recruitmentservices/apply.html',context=my_dict)
    else:
        print('not a cv submition')
    my_dict={'vaccancy':vaccancy,'loggedin':loggedin}
    return render(request,'recruitmentservices/apply.html',context=my_dict)
def aboutus(request):

    my_dict = {}
    return render(request,'recruitmentservices/aboutus.html',context=my_dict)
def feedback(request):
    print(request.POST)
    user=request.user
    comment = request.POST.get('comment')
    jobs = request.POST.get('jobs')
    recruitment= request.POST.get('recruitment')
    if request.POST:
        if comment:
            print('comment recieved')
            if user.id:
                print(user.id)
                try:
                    Comment.objects.create(comment=comment,jobs=int(jobs),recruitment=int(recruitment),user=user)
                    return HttpResponseRedirect(reverse('index'))
                except:
                    print('user did not enter either jobs rating or recruitment rating')
                try:
                    Comment.objects.create(comment=comment,jobs=0,recruitment=int(recruitment),user=user)
                    return HttpResponseRedirect(reverse('index'))
                except:
                    print('user did not enter recruitment rating')
                    
                try:
                    Comment.objects.create(comment=comment,jobs=int(jobs),recruitment=0,user=user)
                    return HttpResponseRedirect(reverse('index'))
                except:
                    print('user did not enter jobs rating')
                    
                try:
                    Comment.objects.create(comment=comment,jobs=0,recruitment=0,user=user)
                    return HttpResponseRedirect(reverse('index'))
                except:
                    print('there is an error')
            else:
                print(user)
                user=User.objects.get(id=1)
                print(user)
                try:
                    Comment.objects.create(comment=comment,jobs=int(jobs),recruitment=int(recruitment),user=user)
                    return HttpResponseRedirect(reverse('index'))
                except:
                    print('user did not enter either jobs rating or recruitment rating')
                try:
                    Comment.objects.create(comment=comment,jobs=0,recruitment=int(recruitment),user=user)
                    return HttpResponseRedirect(reverse('index'))
                except:
                    print('user did not enter recruitment rating')
                    
                try:
                    Comment.objects.create(comment=comment,jobs=int(jobs),recruitment=0,user=user)
                    return HttpResponseRedirect(reverse('index'))
                except:
                    print('user did not enter jobs rating')
                    
                try:
                    Comment.objects.create(comment=comment,jobs=0,recruitment=0,user=user)
                    return HttpResponseRedirect(reverse('index'))
                except:
                    print('there is an error')
                
                    
                
                
        else:
            comment='please leave a comment in comment section'
            my_dict = {'comment':comment}
            return render(request,'recruitmentservices/feedback.html',context=my_dict)

    my_dict = {}
    return render(request,'recruitmentservices/feedback.html',context=my_dict)
def testimonials(request):
    testimonial=request.POST.get('testimonial')
    if request.POST:
        if testimonial:
            now=datetime.datetime.now()
            user=request.user
            print(now)
            try:
                testimony=Testimonial()
                if user.id:
                    testimony.user=user
                else:
                    testimony.user=User.objects.get(id=1)
                testimony.testimony=testimonial
                testimony.date_posted=now
                testimony.save()
                return HttpResponseRedirect(reverse('testimonials'))
            except:
                testimony=Testimonial()
                testimony.user=User.objects.get(id=1)
                testimony.testimony=testimonial
                testimony.date_posted=now
                testimony.save()
                return HttpResponseRedirect(reverse('testimonials'))
                
        else:
            return HttpResponseRedirect(reverse('testimonials'))
    testimonials=Testimonial.objects.all()
    my_dict = {'testimonials':testimonials}
    return render(request,'recruitmentservices/testimonials.html',context=my_dict)