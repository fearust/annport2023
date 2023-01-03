from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


event_image_path = PathAndRename('academy/event_image/')
success_image_path = PathAndRename('academy/success_image/')


class Notice(models.Model):
    title = models.CharField('제목', max_length=200)
    contents = RichTextUploadingField('내용', blank=True, null=True)
    display = models.BooleanField('홈페이지노출여부', default=True)
    create_date = models.DateTimeField('생성시간', auto_now_add=True)
    modify_date = models.DateTimeField('수정시간', auto_now=True)
    class Meta:
        verbose_name = _("공지사항")
        verbose_name_plural = _("공지사항")

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField('제목', max_length=200)
    image = ProcessedImageField(verbose_name='타이틀이미지',
                                upload_to=event_image_path,
                                processors=[ResizeToFit(1200, 1200)],
                                format='JPEG',
                                options={'quality': 80},
                                blank=True,
                                null=True)
    contents = RichTextUploadingField('내용', blank=True, null=True)
    display = models.BooleanField('홈페이지노출여부', default=True)
    event_start = models.DateField('이벤트 시작', blank=True, null=True)
    event_end = models.DateField('이벤트 종료', blank=True, null=True)
    create_date = models.DateTimeField('생성시간', auto_now_add=True)
    modify_date = models.DateTimeField('수정시간', auto_now=True)
    class Meta:
        verbose_name = _("이벤트")
        verbose_name_plural = _("이벤트")

    def __str__(self):
        return self.title


class Success(models.Model):
    title = models.CharField('제목', max_length=200)
    image = ProcessedImageField(verbose_name='타이틀이미지',
                                upload_to=success_image_path,
                                processors=[ResizeToFit(1200, 1200)],
                                format='JPEG',
                                options={'quality': 80},
                                blank=True,
                                null=True)
    contents = RichTextUploadingField('내용', blank=True, null=True)
    display = models.BooleanField('홈페이지노출여부', default=True)
    create_date = models.DateTimeField('생성시간', auto_now_add=True)
    modify_date = models.DateTimeField('수정시간', auto_now=True)
    class Meta:
        verbose_name = _("합격자")
        verbose_name_plural = _("합격자")

    def __str__(self):
        return self.title


class OnlineForm(models.Model):
    name = models.CharField('성함', max_length=50)
    phoneNumber = models.CharField('연락처', max_length=20)
    email = models.EmailField('이메일', blank=True)
    customer_memo = models.TextField('문의내용', blank=True)
    staff_memo = models.TextField('스탭메모', blank=True)
    create_date = models.DateTimeField('생성시간', auto_now_add=True)
    modify_date = models.DateTimeField('수정시간', auto_now=True)
    class Meta:
        verbose_name = _("_문의")
        verbose_name_plural = _("_문의")

    def __str__(self):
        return f'{self.name} {self.phoneNumber}'
