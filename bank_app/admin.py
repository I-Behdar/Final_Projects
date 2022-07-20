from django.contrib import admin

from bank_app.models import User, Account

admin.site.register(User)
admin.site.register(Account)
