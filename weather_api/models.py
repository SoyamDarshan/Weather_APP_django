from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

"""
Assuming rainfall will never be in negative.
Year will only be from 1900 to 4000.
Months are as usual limited to 1 to 12.
No Restriction on Country names so that we can add data for other countries later.
(could have used choices for keeping just UK, Scotland, England and Wales) 
Assuming data for a particular pair of year and month will be same.(This will also handle the duplicate records)
"""


class RainfallData(models.Model):
    country_name = models.CharField(max_length=50)
    value = models.FloatField(validators=[
            MinValueValidator(0.0)
        ])
    year = models.IntegerField(validators=[
            MaxValueValidator(4000),
            MinValueValidator(1900)
        ])
    month = models.IntegerField(validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ])
    date_val = models.DateField(null=True)

    class Meta:
        unique_together = ('year', 'month', 'country_name')

    def __str__(self):
        return self.country_name + " " + str(self.year) + "-" + str(self.month)


class TmaxData(models.Model):
    country_name = models.CharField(max_length=50)
    value = models.FloatField()
    year = models.IntegerField(validators=[
            MaxValueValidator(4000),
            MinValueValidator(1900)
        ])
    month = models.IntegerField(validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ])
    date_val = models.DateField(null=True)

    class Meta:
        unique_together = ('year', 'month', 'country_name')

    def __str__(self):
        return self.country_name + " " + str(self.year) + "-" + str(self.month)


class TminData(models.Model):
    country_name = models.CharField(max_length=50)
    value = models.FloatField()
    year = models.IntegerField(validators=[
            MaxValueValidator(4000),
            MinValueValidator(1900)
        ])
    month = models.IntegerField(validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ])
    date_val = models.DateField(null=True)

    class Meta:
        unique_together = ('year', 'month', 'country_name')

    def __str__(self):
        return self.country_name + " " + str(self.year) + "-" + str(self.month)
