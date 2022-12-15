from django.contrib import admin

from .models import ChatRoomsList, UserMessage

# Register your models here.
admin.site.register([ChatRoomsList,UserMessage])

