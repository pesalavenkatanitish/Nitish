from django.contrib import admin
from testapp.models import MoviesInformation
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['release_date','MovieName','Hero','Heroine','Rating']
admin.site.register(MoviesInformation,MovieAdmin)
