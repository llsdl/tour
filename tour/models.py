from django.db import models


class Country(models.Model):
    name = models.CharField(verbose_name='наименование', max_length=255, null=True, blank=False)

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(verbose_name='название', max_length=255, null=True, blank=False)
    country = models.ForeignKey(to=Country, verbose_name='страна', null=True, blank=False)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return '{} ({})'.format(self.name, self.country.name)


class Flight(models.Model):
    departure_time = models.DateTimeField(verbose_name='дата отправки', null=True, blank=False)
    arrival_time = models.DateTimeField(verbose_name='дата прибытия', null=True, blank=False)
    departure_city = models.ForeignKey(to=City, verbose_name='место отправки', null=True, blank=False,
            related_name='flight_from')
    arrival_city = models.ForeignKey(to=City, verbose_name='место прибытия', null=True, blank=False,
            related_name='flight_to')

    class Meta:
        verbose_name = 'рейс'
        verbose_name_plural = 'рейсы'

    def __str__(self):
        return '{} ({}) - {} ({})'.format(self.departure_city, self.departure_time, self.arrival_city, self.arrival_time)


class Tour(models.Model):
    flight_to = models.OneToOneField(to=Flight, verbose_name='рейс туда', related_name='check_in_tour')
    flight_from = models.OneToOneField(to=Flight, verbose_name='рейс оттуда', related_name='check_out_tour')
    price = models.FloatField(verbose_name='стоимость', null=True, blank=False)

    class Meta:
        verbose_name = 'тур'
        verbose_name_plural = 'туры'

    #def duration(self):
        #return self.flight_to.departure_time - self.flight_from.arrival_time

    #def __str__(self):
        #return '{} ({} дней)'.format(self.flight_to.arrival_city, self.duration)

    @property
    def duration(self):
        return self.flight_from.departure_time - self.flight_to.arrival_time

    def __str__(self):
        return '{} ({} дней)'.format(self.flight_to.arrival_city, self.duration.days)


