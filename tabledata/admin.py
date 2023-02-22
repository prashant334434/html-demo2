from django.contrib import admin

from tabledata.models import tabledata
from tabledata.models import helps
class tabledataadmin(admin.ModelAdmin):
    list_display=('name','phone_no','city')

admin.site.register(tabledata,tabledataadmin)
class helpsadmin(admin.ModelAdmin):
    list_display=('name','phone_no','mess')

admin.site.register(helps,helpsadmin)
