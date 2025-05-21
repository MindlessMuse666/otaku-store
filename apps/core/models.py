from django.db import models


class TimeStampedModel(models.Model):
    """
    Абстрактная базовая модель с полями created и modified
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 