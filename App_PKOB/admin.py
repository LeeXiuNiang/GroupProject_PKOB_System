from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Victim),
admin.site.register(Request),
admin.site.register(Decline),
admin.site.register(Receive),



