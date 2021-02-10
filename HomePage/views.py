from django.shortcuts import render
from . import models
# Create your views here.
def HomePage_List (request):
    HomePages = models.HomePage.objects.all().order_by('date')

    return render (request , 'HomePage/HomePage_List.html',{'HomePages':HomePages} )
