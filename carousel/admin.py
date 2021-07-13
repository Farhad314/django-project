from django.contrib import admin
from .models import Post,Slider
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'short_description',
        'thumbnail',
    
    ]
admin.site.register(Post,PostAdmin)
class SliderAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'thumbnail',
        'short_discription'
    ]

admin.site.register(Slider, SliderAdmin)