from django.shortcuts import render
from . models import db_1
# Create your views here.
def index(request):
    obj=db_1.objects.all()
    return render(request,"index.html",{'result':obj})