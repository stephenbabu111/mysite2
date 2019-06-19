from django.contrib import admin
from myapp.models import fb_table,gmail_table

admin.site.register(fb_table)
admin.site.register(gmail_table)

