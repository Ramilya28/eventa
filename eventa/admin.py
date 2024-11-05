from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Participant, Meeting, MeetingFile, MeetingResponse

admin.site.register(Participant)
admin.site.register(Meeting)
# admin.site.register(MeetingFile)
admin.site.register(MeetingResponse)

