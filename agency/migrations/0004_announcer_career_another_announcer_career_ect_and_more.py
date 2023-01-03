# Generated by Django 4.1.4 on 2023-01-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_onlineform'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcer',
            name='career_another',
            field=models.TextField(null=True, verbose_name='방송,모델,강의,통역 경력'),
        ),
        migrations.AddField(
            model_name='announcer',
            name='career_ect',
            field=models.TextField(null=True, verbose_name='기타 경력'),
        ),
        migrations.AddField(
            model_name='announcer',
            name='career_event',
            field=models.TextField(null=True, verbose_name='행사MC 경력'),
        ),
        migrations.AlterField(
            model_name='announcer',
            name='description',
            field=models.TextField(null=True, verbose_name='설명'),
        ),
    ]
