from django.contrib import admin
from .models import Gem, Attribute, Chain

# Register your models here.
admin.site.register(Gem)
admin.site.register(Attribute)
admin.site.register(Chain)