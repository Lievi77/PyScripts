
# Register your models here with the admin
from django.contrib import admin

from .models import Question

admin.site.register(Question)