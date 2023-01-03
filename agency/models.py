from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
import os


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


backdrop_path = PathAndRename('agency/profile_backdrop/')
agency_path = PathAndRename('agency/profile_photo/')
gallery_path = PathAndRename('agency/gallery/')


class Backdrops(models.Model):
    image = ProcessedImageField(verbose_name='배경사진',
                                upload_to=backdrop_path,
                                processors=[ResizeToFit(1200, 1200)],
                                format='JPEG',
                                options={'quality': 80})
    backdrop_name = models.CharField('배경이미지제목', max_length=50, blank=True)
    class Meta:
        verbose_name = _("배경")
        verbose_name_plural = _("배경")

    def __str__(self):
        return self.backdrop_name


class AnnouncerTag(TagBase):
    class Meta:
        verbose_name = _("에이전시태그1")
        verbose_name_plural = _("에이전시태그1")


class TaggedAnnouncer(GenericTaggedItemBase):
    tag = models.ForeignKey(
        AnnouncerTag,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )


class AnnouncerTag2(TagBase):
    class Meta:
        verbose_name = _("에이전시태그2")
        verbose_name_plural = _("에이전시태그2")


class TaggedAnnouncer2(GenericTaggedItemBase):
    tag = models.ForeignKey(
        AnnouncerTag2,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )


class Announcer(models.Model):
    name = models.CharField('이름', max_length=10)
    title = models.CharField('호칭', max_length=20)
    tags = TaggableManager(through=TaggedAnnouncer)
    tags2 = TaggableManager(through=TaggedAnnouncer2)
    description = models.TextField('설명', null=True)
    profile_photo = models.ImageField('프로필사진', upload_to=agency_path)
    profile_backdrop = models.ForeignKey(Backdrops, on_delete=models.SET_NULL, null=True)
    profile = models.TextField('프로필', blank=True)
    announcerdisplay = models.BooleanField('홈페이지노출여부', default=True)
    announcermain = models.BooleanField('메인아나운서', default=False)
    career_event = models.TextField('행사MC 경력', null=True)
    career_another = models.TextField('방송,모델,강의,통역 경력', null=True)
    career_ect = models.TextField('기타 경력', null=True)
    class Meta:
        verbose_name = _("아나운서")
        verbose_name_plural = _("아나운서")

    def __str__(self):
        return self.name


class Gallery(models.Model):
    wedding_mc = models.ForeignKey(Announcer, on_delete=models.CASCADE)
    image = ProcessedImageField(verbose_name='아나운서사진',
                                upload_to=gallery_path,
                                processors=[ResizeToFit(1700, 1700)],
                                format='JPEG',
                                options={'quality': 80})


class Youtube(models.Model):
    wedding_mc = models.ForeignKey(Announcer, on_delete=models.CASCADE)
    url = models.CharField('유튜브일련번호', max_length=20)


class OnlineForm(models.Model):
    name = models.CharField('성함', max_length=50)
    phoneNumber = models.CharField('연락처', max_length=20)
    corp = models.CharField('기업단체명', max_length=50)
    email = models.EmailField('이메일', blank=True)
    customer_memo = models.TextField('문의내용', blank=True)
    staff_memo = models.TextField('스탭메모', blank=True)
    create_date = models.DateTimeField('생성시간', auto_now_add=True)
    modify_date = models.DateTimeField('수정시간', auto_now=True)
    class Meta:
        verbose_name = _("_문의")
        verbose_name_plural = _("_문의")

    def __str__(self):
        return f'{self.name}({self.corp}) {self.phoneNumber}'
