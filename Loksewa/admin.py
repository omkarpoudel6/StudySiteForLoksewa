from django.contrib import admin
from .models import Category,Questions,Answer

# Register your models here.
admin.site.register(Category)
admin.site.register(Questions)
admin.site.register(Answer)