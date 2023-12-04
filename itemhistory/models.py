from django.db import models
from itembase.models import ItemBase
from members.models import Member

class ItemHistory(ItemBase):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
