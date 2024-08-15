import time,datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
def index(request):
    my_dict = {}
    return render(request,'recruitmentservices/index.html',context=my_dict)
