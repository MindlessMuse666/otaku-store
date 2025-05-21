from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.core.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    """
    Кастомная модель пользователя
    """
    email = models.EmailField('Email адрес', unique=True)
    phone = models.CharField('Телефон', max_length=15, blank=True)
    address = models.TextField('Адрес', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email 