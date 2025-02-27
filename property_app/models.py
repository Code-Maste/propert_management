from django.db import models

Type = (
    ('Property', 'Property'),
    ('House', 'House'),
    ('Commercial', 'Commercial'),
)

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100, choices=Type)
    description = models.TextField()
    number_of_units = models.IntegerField()




    def __str__(self):
        return self.name

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    rent = models.IntegerField()
    is_available = models.BooleanField(default=True)

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    units = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.IntegerField()


