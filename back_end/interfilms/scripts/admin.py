from django.contrib import admin

from .models import origin, nodeList, coordinate, meta, linkList, startAt, endAt

admin.site.register(origin)     # Регистрация модели
admin.site.register(nodeList)
admin.site.register(coordinate)
admin.site.register(meta)
admin.site.register(linkList)
admin.site.register(startAt)
admin.site.register(endAt)