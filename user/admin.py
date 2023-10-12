from django.contrib import admin
from user.models import User
from demo.admin import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )
    inlines = (BasketAdmin,)