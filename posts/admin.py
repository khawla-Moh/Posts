from django.contrib import admin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
from .models import Posts,Comments,Category
# Register your models here.

class PostsAdmin(SummernoteModelAdmin):
    list_display=['name','publish_date','category']
    list_filter=['publish_date','category']



admin.site.register(Posts,PostsAdmin)
admin.site.register(Comments)
admin.site.register(Category)