from django.contrib import admin


from .models import Book, Author, Editorial
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    '''
        Admin View for Author
    '''
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name',)


admin.site.register(Author, AuthorAdmin)


class EditorialInline(admin.TabularInline):
    '''
    Tabular Inline View for Editorial
    '''
    model = Book.editorials.through
    verbose_name = 'Editorial'
    verbose_name_plural = 'Editorials'
    extra = 0


class BookAdmin(admin.ModelAdmin):
    '''
        Admin View for Book
    '''
    list_display = ('title', 'registered_by', 'created_at',)
    search_fields = ('title',)
    inlines = (EditorialInline,)


admin.site.register(Book, BookAdmin)


class EditorialAdmin(admin.ModelAdmin):
    '''
        Admin View for Editorial
    '''
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Editorial, EditorialAdmin)
