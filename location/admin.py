from django.contrib import admin
from location.models import Countries, States, Cities

# Register your models here.
admin.site.register(Countries)
admin.site.register(States)
admin.site.register(Cities)