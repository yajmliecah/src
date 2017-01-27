from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc
from datetime import datetime


class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    logo = models.ImageField(verbose_name=_("Logo"))
    description = models.TextField(verbose_name=_("Description"))
        
    def __str__(self):
        return _("Brand %s") % self.name
        
             
class Spec(models.Model):
    CATEGORY = (
        ('CAR', 'Car'),
        ('MOTORCYCLE', 'MotorCycle'),
        ('VEHICLE', 'Vehicle')
    )
    TRANS = (
        ('AUTOMATIC', 'Automatic'),
        ('MANUAL', 'Manual')
    )
    CONDITION = (
        ('NEW', 'New'),
        ('USED', 'Used'),
    )
    FUEL = (
        ('DIESEL', 'Diesel'),
        ('ELECTRO', 'Electro'),
        ('GASOLINE', 'Gasoline')
    )
    SELLER_TYPE = (
        ('DEALER', 'Dealer'),
        ('PRIVATE', 'Private')
    )
    LIFESTYLES = (
        ('FAMILY', 'Family'),
        ('LUXURY', 'Luxury'),
        ('OFFROAD', 'Offroad')
    )
    name = models.CharField(max_length=100, unique=True, verbose_name=_("name"))
    slug = models.SlugField(unique=True, null=True)
    brand = models.ForeignKey(Brand, verbose_name=_("brand"), related_name='specs')
    condition = models.CharField(max_length=100, choices=CONDITION)
    category = models.CharField(max_length=50, choices=CATEGORY, verbose_name=_("category"), default='')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    details = models.TextField(blank=True, verbose_name=_("details"), help_text=_("Enter car details"))
    location = models.CharField(max_length=100, verbose_name=_("locations"), default='')
    transmission = models.CharField(max_length=100, choices=TRANS, verbose_name=_("transmission"), default='')
    fuel = models.CharField(max_length=100, choices=FUEL, default='')
    lifestyle = models.CharField(max_length=100, choices=LIFESTYLES, null=True)
    seller_type = models.CharField(max_length=100, choices=SELLER_TYPE, default='')
    mileage = models.CharField(max_length=100, default='')
    color_family = models.CharField(max_length=100, default='')
    
    class Meta:
        verbose_name = _("Spec")
        verbose_name_plural = _("Specs")
        ordering = ["-id"]

    def __str__(self):
        return str(self.name)
        
#    def was_built(self):
#       return self.build.date() == datetime.date.today()
        
        































