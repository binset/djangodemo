from django.contrib import admin

from . import models
from .models import Question
# Register your models here.

admin.site.register(models.Question)
admin.site.register(models.Choice)
