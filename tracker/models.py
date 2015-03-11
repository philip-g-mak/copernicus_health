from django.db import models

# Create your models here.

FORM = [('tab', 'Tablets'), ('cap', 'Capsules'), ('inj', 'Injections')]
FREQ = [('d', 'Daily'), ('w', 'Weekly')]


class Medication(models.Model):
    owner = models.ForeignKey('auth.User', related_name='medications')
    rx_name = models.CharField(max_length=180)
    formulation = models.CharField(choices=FORM, default='tab', max_length=180)
    total_quantity = models.IntegerField()
    take_quantity = models.IntegerField()
    prn = models.BooleanField(default=False)
    freq = models.CharField(choices=FREQ, default='d', max_length=180)

    class Meta:
        ordering = ('rx_name',)

    def save(self, *args, **kwargs):
        super(Medication, self).save(*args, **kwargs)


class Personal(models.Model):
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    address1 = models.CharField(max_length=180)
    address2 = models.CharField(max_length=180)
    city = models.CharField(max_length=180)
    state = models.CharField(max_length=180)
    zip = models.IntegerField()
