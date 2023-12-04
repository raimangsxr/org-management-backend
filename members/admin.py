from django.contrib import admin
from .models import Member

@admin.register(Member)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'name', 'surname', 'age', 'birth', 'created']
