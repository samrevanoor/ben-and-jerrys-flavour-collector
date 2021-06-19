from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flavour
from .forms import RecommendedToppingForm

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
  topping_form = RecommendedToppingForm()
  return render(request, 'flavours/detail.html', { 
    'flavour': flavour, 'topping_form': topping_form 
    })

class FlavourCreate(CreateView):
  model = Flavour
  fields = '__all__'
  success_url = '/flavours/'

class FlavourUpdate(UpdateView):
  model = Flavour
  fields = '__all__'

class FlavourDelete(DeleteView):
  model = Flavour
  success_url = '/flavours/'

def add_topping(request, flavour_id):
  form = RecommendedToppingForm(request.POST)
  if form.is_valid():
    new_topping = form.save(commit=False)
    new_topping.flavour_id = flavour_id
    new_topping.save()
  return redirect('detail', flavour_id=flavour_id)