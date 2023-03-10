# Generated by Django 4.1.4 on 2022-12-29 00:05

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncerTag2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': '에이전시태그2',
                'verbose_name_plural': '에이전시태그2',
            },
        ),
        migrations.AlterModelOptions(
            name='announcer',
            options={'verbose_name': '아나운서', 'verbose_name_plural': '아나운서'},
        ),
        migrations.AlterModelOptions(
            name='announcertag',
            options={'verbose_name': '에이전시태그1', 'verbose_name_plural': '에이전시태그1'},
        ),
        migrations.AlterModelOptions(
            name='backdrops',
            options={'verbose_name': '배경', 'verbose_name_plural': '배경'},
        ),
        migrations.CreateModel(
            name='TaggedAnnouncer2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='agency.announcertag2')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='announcer',
            name='tags2',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='agency.TaggedAnnouncer2', to='agency.AnnouncerTag2', verbose_name='Tags'),
        ),
    ]
