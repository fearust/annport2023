# Generated by Django 4.1.4 on 2022-12-28 23:57

import agency.models
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('title', models.CharField(max_length=20, verbose_name='호칭')),
                ('description', models.TextField(verbose_name='설명')),
                ('profile_photo', models.ImageField(upload_to=agency.models.PathAndRename('agency/profile_photo/'), verbose_name='프로필사진')),
                ('profile', models.TextField(blank=True, verbose_name='프로필')),
                ('announcerdisplay', models.BooleanField(default=True, verbose_name='홈페이지노출여부')),
                ('announcermain', models.BooleanField(default=False, verbose_name='메인아나운서')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncerTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': '에이전시태그',
                'verbose_name_plural': '에이전시태그',
            },
        ),
        migrations.CreateModel(
            name='Backdrops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=agency.models.PathAndRename('agency/profile_backdrop/'), verbose_name='배경사진')),
                ('backdrop_name', models.CharField(blank=True, max_length=50, verbose_name='배경이미지제목')),
            ],
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=20, verbose_name='유튜브일련번호')),
                ('wedding_mc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.announcer')),
            ],
        ),
        migrations.CreateModel(
            name='TaggedAnnouncer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='agency.announcertag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=agency.models.PathAndRename('agency/gallery/'), verbose_name='아나운서사진')),
                ('wedding_mc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.announcer')),
            ],
        ),
        migrations.AddField(
            model_name='announcer',
            name='profile_backdrop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agency.backdrops'),
        ),
        migrations.AddField(
            model_name='announcer',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='agency.TaggedAnnouncer', to='agency.AnnouncerTag', verbose_name='Tags'),
        ),
    ]
