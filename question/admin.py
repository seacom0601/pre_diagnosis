from django.contrib import admin
from .models import Sickpart, Option, Question

# Register your models here.
admin.site.register(Sickpart)
admin.site.register(Option)
admin.site.register(Question)