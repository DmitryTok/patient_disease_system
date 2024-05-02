from django.contrib import admin
from disease.models import Doctor, Qualification, WorkPlace, Note, Recipe

admin.site.register(Doctor)
admin.site.register(Qualification)
admin.site.register(WorkPlace)
admin.site.register(Note)
admin.site.register(Recipe)
