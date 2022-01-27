from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(UserData)
admin.site.register(Teams)
admin.site.register(Task)
admin.site.register(Events)

