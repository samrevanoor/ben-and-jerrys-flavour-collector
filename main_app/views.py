from django.shortcuts import render
from .models import Flavour

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def flavours_index(request):
  flavours = Flavour.objects.all()
  return render(request, 'flavours/index.html', { 'flavours': flavours })

def flavours_detail(request, flavour_id):
  flavour = Flavour.objects.get(id=flavour_id)
  return render(request, 'flavours/detail.html', { 'flavour': flavour })