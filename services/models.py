from django.db import models


class OperatingAirline(models.Model):
    """
    Справочник авиакомпаний
    """
    iata_code = models.CharField('Код iata', max_length=255)
    icao_code = models.CharField('Код icao', max_length=255)
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Авиакомпания'
        verbose_name_plural = 'Авиакомпании'


class FlightNumber(models.Model):
    """
    Справочник рейсов
    """
    airline_code = models.CharField('Рейс', max_length=255)

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'


class User(models.Model):
    """
    Пользователи
    """
    name = models.CharField('Код iata', max_length=255)
    surname = models.CharField('Код iata', max_length=255)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Service(models.Model):
    """
    Услуга
    """
    name = models.CharField('Код iata', max_length=255)
