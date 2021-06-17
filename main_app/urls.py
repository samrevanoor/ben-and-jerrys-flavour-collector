from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flavours/', views.flavours_index, name='index'),
    path('flavours/<int:flavour_id>', views.flavours_detail, name='detail'),
]