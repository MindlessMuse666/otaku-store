from django.db import models
from django.conf import settings
from apps.products.models import Product
from apps.core.models import TimeStampedModel


class Cart(TimeStampedModel):
    """
    Модель корзины покупок
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='cart'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя {self.user.email}'

    @property
    def total_price(self):
        """
        Общая стоимость товаров в корзине
        """
        return sum(item.total_price for item in self.items.all())

    @property
    def total_items(self):
        """
        Общее количество товаров в корзине
        """
        return sum(item.quantity for item in self.items.all())


class CartItem(TimeStampedModel):
    """
    Модель элемента корзины
    """
    cart = models.ForeignKey(
        Cart,
        verbose_name='Корзина',
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Товар',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField('Количество', default=1)

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'
        unique_together = ['cart', 'product']

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    @property
    def total_price(self):
        """
        Общая стоимость элемента корзины
        """
        return self.product.price * self.quantity 