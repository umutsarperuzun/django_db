from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    footballer_data=models.Footballers.objects.all()
    footballer_context={"footballers":footballer_data}
    return render(request,'db_app/index.html',context=footballer_context)