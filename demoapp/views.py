from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj_team=Team.objects.all()
    return render(request,"index.html",{'result':obj, 'team':obj_team})

def home(request):
    return render(request,"index.html")
