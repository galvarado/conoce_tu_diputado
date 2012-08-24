from django.contrib import admin
from main.models import Representative

class RepresentativeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Representative, RepresentativeAdmin)
