from django.contrib import admin

#Models 
from .models import Proyect
# Register your models here.
#admin.site.register(Proyect)

@admin.register(Proyect)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'updated')
    list_display_links = ('id','title',)
    #list_editable = ('title',)

    list_filter = ('title','created', 'updated')

    search_fields = ('title',)

    readonly_fields = ('created', 'updated')

    