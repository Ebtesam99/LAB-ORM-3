from django.contrib import admin
from .models import Blog , Review

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title' , 'content' ,'is_published', 'published_at', 'category' )
    list_filter = ('category',)

class ReviewModel(admin.ModelAdmin):

    list_display = ('firstName' , 'lastName', 'comment', 'rating')
    list_filter = ('blog',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Review, ReviewModel)
