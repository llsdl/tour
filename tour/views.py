from django.views.generic import ListView
from .models import Tour, Country, City


class ToursListView(ListView):
    model = Tour
    context_object_name = 'tours'

    def get_context_data(self, **kwargs):
        context = super(ToursListView, self).get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        context['cities'] = City.objects.all()
        return context

    def get_queryset(self, **kwargs):

        if self.request.GET.get('from_city', False):
            from_city_id = int(self.request.GET.get('from_city'), 0)
            from_city = City.objects.get(pk=from_city_id)

        if self.request.GET.get('from_city', False):
            destination_country_id = int(self.request.GET.get('destination_country', 0))
            destination_country = Country.objects.get(pk=destination_country_id)

        return super(ToursListView, self).get_queryset(**kwargs)
