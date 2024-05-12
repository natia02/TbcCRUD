from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    categories = models.ManyToManyField(
        to='EasyStock.Category',
        related_name='products',
        verbose_name=_('Categories'))
    name = models.CharField(max_length=100, verbose_name=_('Product Name'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    quantity = models.IntegerField(verbose_name=_('Quantity'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
