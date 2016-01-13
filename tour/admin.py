from django.contrib import admin
from .models import Country, City, Flight, Tour


class CountryAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class FlightAdmin(admin.ModelAdmin):
    pass


class TourAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Tour, TourAdmin)
