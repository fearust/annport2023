# Generated by Django 4.1.4 on 2022-12-28 23:57

import academy.models
import ckeditor_uploader.fields
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=academy.models.PathAndRename('academy/event_image/'), verbose_name='타이틀이미지')),
                ('contents', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='내용')),
                ('display', models.BooleanField(default=True, verbose_name='홈페이지노출여부')),
                ('event_start', models.DateField(blank=True, null=True, verbose_name='이벤트 시작')),
                ('event_end', models.DateField(blank=True, null=True, verbose_name='이벤트 종료')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('contents', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='내용')),
                ('display', models.BooleanField(default=True, verbose_name='홈페이지노출여부')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='성함')),
                ('phoneNumber', models.CharField(max_length=20, verbose_name='연락처')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='이메일')),
                ('customer_memo', models.TextField(blank=True, verbose_name='문의내용')),
                ('staff_memo', models.TextField(blank=True, verbose_name='스탭메모')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
            ],
        ),
        migrations.CreateModel(
            name='Success',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=academy.models.PathAndRename('academy/success_image/'), verbose_name='타이틀이미지')),
                ('contents', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='내용')),
                ('display', models.BooleanField(default=True, verbose_name='홈페이지노출여부')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
            ],
        ),
    ]
