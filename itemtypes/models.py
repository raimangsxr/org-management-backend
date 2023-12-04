import uuid

from django.db import models

class ItemType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']