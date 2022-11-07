from django.contrib import admin
from .models import News, Category, Comment
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('author', 'body')


admin.site.register(Comment, CommentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
