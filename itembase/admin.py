from django.contrib import admin

class ItemBaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'name', 'surname', 'age', 'birth', 'created']