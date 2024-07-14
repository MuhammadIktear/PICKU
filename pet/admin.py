from django.contrib import admin
from .models import Pet, Adopt, Review

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'color', 'size', 'sex', 'created_by', 'created_at', 'rehoming_fee', 'status')
    list_filter = ('species', 'breed', 'color', 'size', 'sex', 'status')
    search_fields = ('name', 'created_by__username')

@admin.register(Adopt)
class AdoptAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet', 'adopt_date')
    list_filter = ('adopt_date',)
    search_fields = ('user__username', 'pet__name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pet', 'user', 'name', 'email', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('pet__name', 'user__username', 'name', 'email')
