from django.contrib import admin

from .models import Flat, Complaint


@admin.register(Flat)
class SearchFlat(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owners_phonenumber', ]
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ['floor', 'rooms_number', 'has_balcony', 'new_building']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['complainer', 'flat']