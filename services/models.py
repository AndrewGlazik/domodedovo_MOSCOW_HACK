from django.db import models


class OperatingAirline(models.Model):
    """
    Справочник авиакомпаний
    """
    iata_code = models.CharField('Код iata', max_length=255)
    icao_code = models.CharField('Код icao', max_length=255)
    name = models.CharField('Название', max_length=255)
    services = models.ManyToManyField('Service', verbose_name='Сервисы', blank=True)

    class Meta:
        verbose_name = 'Авиакомпания'
        verbose_name_plural = 'Авиакомпании'


class FlightNumber(models.Model):
    """
    Справочник рейсов
    """
    flight = models.CharField('Рейс', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'


class Category(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Категория инвалидности'
        verbose_name_plural = 'Категории инвалидности'


class User(models.Model):
    """
    Пользователи
    """
    name = models.CharField('Код iata', max_length=255)
    surname = models.CharField('Код iata', max_length=255)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Service(models.Model):
    """
    Услуга
    """
    name = models.CharField('Код iata', max_length=255)
    surname = models.CharField('Код iata', max_length=255)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    meeting_time = models.DateTimeField("Дата встречи", blank=True, null=True)
    place = models.CharField("Место встречи", max_length=255)
    escort_features = models.CharField("Особенности сопровождения", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


# class