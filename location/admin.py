from django.contrib import admin
from location.models import Countries, States, Cities

# Register your models here.

class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class CountryAdmin(ReadOnlyAdmin):
    search_fields = ('country_name',)


class StateAdmin(ReadOnlyAdmin):
    search_fields = ('state',)
    list_display = ("id_state", "state", "country_id")
    autocomplete_fields = ["country_id"]


class CityAdmin(ReadOnlyAdmin):
    # list_display = ("id_city", "city", "state_id")
    autocomplete_fields = ["state_id"]


admin.site.register(Countries, CountryAdmin)
admin.site.register(States, StateAdmin)
admin.site.register(Cities, CityAdmin)