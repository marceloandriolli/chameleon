from django.db import models
from django.contrib.postgres.fields import JSONField



class FieldModel(models.Model):
    TEXT = 'txt'
    DATE = 'dt'
    NUMBER = 'num'
    EMUN = 'enum'

    TYPES = (
        (TEXT , 'Text'),
        (DATE, 'Date'),
        (NUMBER,'Number'),
        (EMUN, 'Enum'),
    )
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=4, choices=TYPES, default=TEXT)
    property = JSONField(null=True)

    def __str__(self):
        return self.name



class RiskTypeModel(models.Model):
    name = models.CharField(max_length=20)
    fields = models.ManyToManyField(FieldModel)

    def __str__(self):
        return self.name