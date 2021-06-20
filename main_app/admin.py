from django.contrib import admin
# import your models here
from .models import Flavour, RecommendedTopping, Vendor

# Register your models here
admin.site.register(Flavour)
admin.site.register(RecommendedTopping)
admin.site.register(Vendor)