from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flavours/', views.flavours_index, name='index'),
    path('flavours/<int:flavour_id>', views.flavours_detail, name='detail'),
    path('flavours/create/', views.FlavourCreate.as_view(), name='flavours_create'),
    path('flavours/<int:pk>/update/', views.FlavourUpdate.as_view(), name='flavours_update'),
    path('flavours/<int:pk>/delete/', views.FlavourDelete.as_view(), name='flavours_delete'),
    path('flavours/<int:flavour_id>/add_topping', views.add_topping, name='add_topping'),
    path('flavours/<int:flavour_id>/assoc_vendor/<int:vendor_id>/', views.assoc_vendor, name='assoc_vendor'),
    path('flavours/<int:flavour_id>/unassoc_vendor/<int:vendor_id>/', views.unassoc_vendor, name='unassoc_vendor'),
    path('vendors/', views.VendorList.as_view(), name='vendors_index'),
    path('vendors/<int:pk>/', views.VendorDetail.as_view(), name='vendors_detail'),
    path('vendors/create/', views.VendorCreate.as_view(), name='vendors_create'),
    path('vendors/<int:pk>/update/', views.VendorUpdate.as_view(), name='vendors_update'),
    path('vendors/<int:pk>/delete/', views.VendorDelete.as_view(), name='vendors_delete'),
]