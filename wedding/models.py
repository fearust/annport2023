from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase
from uuid import uuid4
from django.utils.deconstruct import deconstructible
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


backdrop_path = PathAndRename('wedding/profile_backdrop/')
mc_path = PathAndRename('wedding/profile_photo/')
gallery_path = PathAndRename('wedding/gallery/')
homepage_path = PathAndRename('wedding/homepage/')


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


class McTag(TagBase):
    class Meta:
        verbose_name = _("사회자태그")
        verbose_name_plural = _("사회자태그")


class TaggedMc(GenericTaggedItemBase):
    tag = models.ForeignKey(
        McTag,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )


class Mc(models.Model):
    name = models.CharField('이름', max_length=10)
    title = models.CharField('호칭', max_length=20)
    tags = TaggableManager(through=TaggedMc)
    description = models.TextField('설명')
    profile_photo = models.ImageField('프로필사진', upload_to=mc_path)
    profile_backdrop = models.ForeignKey(Backdrops, on_delete=models.SET_NULL, null=True)
    profile = models.TextField('프로필', blank=True)
    mcdisplay = models.BooleanField('홈페이지노출여부', default=True)
    mcmain = models.BooleanField('메인사회자', default=False)
    class Meta:
        verbose_name = _("사회자")
        verbose_name_plural = _("사회자")

    def __str__(self):
        return self.name


class Gallery(models.Model):
    wedding_mc = models.ForeignKey(Mc, on_delete=models.CASCADE)
    image = ProcessedImageField(verbose_name='사회자사진',
                                upload_to=gallery_path,
                                processors=[ResizeToFit(1700, 1700)],
                                format='JPEG',
                                options={'quality': 80})


class Youtube(models.Model):
    wedding_mc = models.ForeignKey(Mc, on_delete=models.CASCADE)
    url = models.CharField('유튜브일련번호', max_length=20)


class Cast(models.Model):
    bride = models.CharField('신부님 성함', max_length=20, blank=True)
    groom = models.CharField('신랑님 성함', max_length=20, blank=True)
    bride_phone = models.CharField('신부님 연락처', max_length=20, blank=True)
    groom_phone = models.CharField('신랑님 연락처', max_length=20, blank=True)
    wedding_date = models.CharField('본식 날짜,시간', max_length=100, null=True, blank=True)
    wedding_place = models.CharField('본식 장소', max_length=50, blank=True)
    officiator = models.BooleanField('주례', default=False)
    wedding_reception = models.BooleanField('2부 진행', default=False)
    email_addr = models.EmailField('메일주소', blank=True)
    wish_mc = models.CharField('희망 사회자', max_length=100, blank=True)
    customer_memo = models.TextField('고객 메모', blank=True)
    staff_memo = models.TextField('스탭 메모', blank=True)
    create_date = models.DateTimeField('문의시간')
    class Meta:
        verbose_name = _("_문의")
        verbose_name_plural = _("_문의")
