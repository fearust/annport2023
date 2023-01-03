from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from academy.models import Notice, Event, Success, OnlineForm

# Register your models here.


class NoticeAdminForm(forms.ModelForm):
    contents = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Notice
        fields = '__all__'


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'modify_date', 'display']
    form = NoticeAdminForm


class EventAdminForm(forms.ModelForm):
    contents = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Event
        fields = '__all__'


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'modify_date', 'display']
    form = EventAdminForm


class SuccessAdminForm(forms.ModelForm):
    contents = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Success
        fields = '__all__'


class SuccessAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'modify_date', 'display']
    form = SuccessAdminForm


class OnlineFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'phoneNumber', 'create_date', 'modify_date']


admin.site.register(Notice, NoticeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Success, SuccessAdmin)
admin.site.register(OnlineForm, OnlineFormAdmin)