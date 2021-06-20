from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Flavour, Vendor
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
  available_vendors = Vendor.objects.exclude(id__in = flavour.vendors.all().values_list('id'))
  topping_form = RecommendedToppingForm()
  return render(request, 'flavours/detail.html', { 
    'flavour': flavour, 'topping_form': topping_form,
    'vendors': available_vendors
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

class VendorList(ListView):
  model = Vendor

class VendorDetail(DetailView):
  model = Vendor

class VendorCreate(CreateView):
  model = Vendor
  fields = '__all__'

class VendorUpdate(UpdateView):
  model = Vendor
  fields = ['name', 'address']

class VendorDelete(DeleteView):
  model = Vendor
  success_url = '/vendors/'

def assoc_vendor(request, flavour_id, vendor_id):
  Flavour.objects.get(id=flavour_id).vendors.add(vendor_id)
  return redirect('detail', flavour_id=flavour_id)

def unassoc_vendor(request, flavour_id, vendor_id):
  Flavour.objects.get(id=flavour_id).vendors.remove(vendor_id)
  return redirect('detail', flavour_id=flavour_id)