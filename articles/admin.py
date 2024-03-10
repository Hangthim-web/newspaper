from django.contrib import admin

from articles.models import Article, Comment


# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
