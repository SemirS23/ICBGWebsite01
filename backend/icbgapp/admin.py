from django.contrib import admin
from .models import Event, Contact

class EventModelAdmin(admin.ModelAdmin):
    list_display=('title', 'created_at', 'updated_at')
    search_fields=('title', 'description')

# Register your models here.
admin.site.register(Event, EventModelAdmin)
admin.site.register(Contact)