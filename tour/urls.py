from django.conf.urls import url, include
from .views import ToursListView


urlpatterns = [
    url(r'^$', ToursListView.as_view(), name='list'),
    ]