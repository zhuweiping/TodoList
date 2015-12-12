from __future__ import unicode_literals

from django.contrib import admin
from mytodo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'todo', 'priority', 'flag', 'pubtime')
    list_filter = ('pubtime',)
    ordering = ('-pubtime',)


admin.site.register(Todo, TodoAdmin)