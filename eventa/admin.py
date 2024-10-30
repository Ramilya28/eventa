from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Participant, Meeting

admin.site.register(Participant)
admin.site.register(Meeting)
