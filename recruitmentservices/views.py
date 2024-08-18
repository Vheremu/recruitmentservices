import time,datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from recruitersite.models import Vaccancy
def index(request):
    vaccancies=Vaccancy.objects.all()
    my_dict = {'vaccancies':vaccancies}
    return render(request,'recruitmentservices/index.html',context=my_dict)
