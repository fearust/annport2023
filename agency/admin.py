from django.contrib import admin
from agency.models import Announcer, Backdrops, Youtube, Gallery, AnnouncerTag, AnnouncerTag2, OnlineForm


class YoutubeInline(admin.StackedInline):
    model = Youtube
    extra = 1


class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 1


@admin.register(Announcer)
class AnnouncerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'fullname', 'announcerdisplay', 'announcermain']
    list_display_links = ['pk', 'fullname']
    inlines = (YoutubeInline, GalleryInline)

    def fullname(self, post):
        return '{} {}'.format(post.name, post.title)
    fullname.short_description = '전체이름'


@admin.register(Backdrops)
class BackdropsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'backdrop_name']
    list_display_links = ['pk', 'backdrop_name']


class OnlineFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'corp', 'phoneNumber', 'create_date', 'modify_date']


admin.site.register(AnnouncerTag)
admin.site.register(AnnouncerTag2)
admin.site.register(OnlineForm, OnlineFormAdmin)
