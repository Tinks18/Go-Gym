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

# class Venue(models.Model):
#     name = models.CharField('Venue Name', max_length=120)
#     address = models.CharField(max_length=320)
#     zip_code = models.CharField('ZIp Code', max_length=15)
#     phone = models.CharField('Contact Phone', max_length=120)
#     web = models.URLField('Website Address')
#     email_address = models.EmailField('Email Address')

#     def __str__(self):
#         return self.name


# class MyClubUser(models.Model):
#     first_name = models.CharField('First Name', max_length=120)
#     last_name = models.CharField('Last Name', max_length=120)
#     email_address = models.EmailField('User Email')

#     def __str__(self):
#         return self.first_name + " " + self.last_name

# class Event(models.Model):
#     name = models.CharField('Event Name', max_length=120)
#     event_date = models.DateTimeField('Event Date', max_length=120)
#     venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
#     # venue = models.CharField(max_length=120)
#     manager = models.CharField(max_length=120)
#     description = models.TextField(blank=True)
#     attendees = models.ManyToManyField(MyClubUser, blank=True)

#     def __str__(self):
#         return self.name
