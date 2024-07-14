from django.contrib import admin
from .models import Pet,Adopt,Review
# Register your models here.
admin.site.register(Pet)
admin.site.register(Adopt)
admin.site.register(Review)
