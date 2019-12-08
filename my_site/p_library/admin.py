from django.contrib import admin
from p_library.models import Book, Author, Redaction, Friend


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'redaction')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass
# Register your models here.
