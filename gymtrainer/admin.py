from django.contrib import admin
from .models import Gymslot
from .models import Venue
from .models import Event
from .models import MyClubUser

# Register your models here.
admin.site.register(Gymslot)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(MyClubUser)
