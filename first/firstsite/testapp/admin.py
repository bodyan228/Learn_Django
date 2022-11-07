from django.contrib import admin
from .models import Rubrics, Article
from mptt.admin import MPTTModelAdmin


admin.site.register(Rubrics, MPTTModelAdmin)
admin.site.register(Article)
