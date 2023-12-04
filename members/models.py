import uuid

from django.db import models
from datetime import date
from math import floor

# Create your models here.
class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=50)
    number = models.IntegerField()
    birth = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    @property
    def age(self):
        today = date.today()
        datetime_diff = today - self.birth
        return floor(datetime_diff.days / 365)
    
    @property
    def fullname(self):
        return f'{self.name} {self.surname}'
