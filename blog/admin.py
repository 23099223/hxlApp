from django.contrib import admin
import blog.models as models


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('kindeditor/kindeditor-all-min.js',
              'kindeditor/lang/zh_CN.js',
              'kindeditor/config.js',)


admin.site.register(models.Article, BlogAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Tags)
