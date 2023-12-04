import uuid

from django.db import models
from itemtypes.models import ItemType
from providers.models import Provider

class ItemBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        abstract = True