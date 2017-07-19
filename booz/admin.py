from django.contrib import admin

# Register your models here.

from booz.models import Booz,Tag,Comment,Like


class BoozAdmin(admin.ModelAdmin):
    list_display = ('owner','text','subject_matter','created_on','total_likes')
    list_filter = ['created_on']
    search_fields = ['owner']


admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Booz,BoozAdmin)

