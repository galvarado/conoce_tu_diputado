from django.contrib import admin
from main.models import Representative, DataBaseFile

class RepresentativeAdmin(admin.ModelAdmin):
    pass

class DataBaseFileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Representative, RepresentativeAdmin)
admin.site.register(DataBaseFile, DataBaseFileAdmin)

