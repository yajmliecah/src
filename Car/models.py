from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc
from Car.forms import SpecForm
import datetime


class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    logo = models.ImageField(null=True)
    

class Condition(models.Model):
    new = models.BooleanField(default=False)
    used = models.BooleanField(default=False)


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
    name = models.CharField(max_length=100, unique=True, verbose_name=_("name"))
    slug = models.SlugField(unique=True, null=True)
    brand = models.ForeignKey(Brand, verbose_name=_("brand"), related_name='specs')
    condition = models.ForeignKey(Condition, related_name='specs')
    category = models.CharField(max_length=50, choices=CATEGORY, verbose_name=_("type"))
    date_submitted = models.DateTimeField(auto_now_add=True, verbose_name=_("date submitted"))
    price = models.DecimalField(max_digits=9, decimal_places=2)
    details = models.TextField(blank=True, verbose_name=_("details"), help_text=_("Enter car details"))
    location = models.CharField(max_length=100, verbose_name=_("locations"))
    transmission =models.CharField(max_length=100, choices=TRANS, verbose_name=_("transmission"))
    fuel = models.CharField(max_length=100)
    seller_type =models.CharField(max_length=100)
    build =models.DateField()
    mileage = models.CharField(max_length=100)
    color_family = models.CharField(max_length=100)
    lifestyle =models.CharField(max_length=100)
    
    class Meta:
        verbose_name = _("Spec")
        verbose_name_plural = _("Specs")
        ordering = ["-id"]

    def __str__(self):
        return _("Spec %s") % self.name

    def save(self, *args, **kwargs):
        self.date_submitted = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Spec, self).save(args, kwargs)































