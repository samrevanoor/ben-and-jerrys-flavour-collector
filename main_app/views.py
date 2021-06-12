from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Flavour:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description, rating):
    self.name = name
    self.type = type
    self.description = description
    self.rating = rating

flavours = [
  Flavour('Half Baked', 'dairy', 'Chocolate & vanilla ice creams with fudge brownies & gobs of chocolate chip cookie dough', 5),
  Flavour('Cherry Garcia', 'non-dairy', 'Cherry Non-Dairy Frozen Dessert with Cherries & Fudge Flakes', 2),
  Flavour('Chocolate Fudge Brownie', 'dairy', 'This flavour combines our chocolate ice cream with chunks of chewy, fudgy brownies.', 4)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def flavours_index(request):
  return render(request, 'flavours/index.html', { 'flavours': flavours })