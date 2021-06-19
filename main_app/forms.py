from django.forms import ModelForm
from .models import RecommendedTopping

class RecommendedToppingForm(ModelForm):
  class Meta:
    model = RecommendedTopping
    fields = ['topping', 'quantity']