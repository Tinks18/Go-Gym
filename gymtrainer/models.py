from django.db import models

# Create your models here.


class Gymslot(models.Model):
    firstname = models.CharField('First Name', max_length=50, null=False, blank=False)
    lastname = models.CharField('Last Name', max_length=50, null=False, blank=False)
    slot_date = models.CharField('Event Date', max_length=10)
    slot_time = models.CharField('Event Time', max_length=10)
    submit = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return self.firstname + "  " + self.lastname + "  " + self.slot_date + "  " + self.slot_time
