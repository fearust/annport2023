# Generated by Django 4.1.4 on 2023-01-03 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': '이벤트', 'verbose_name_plural': '이벤트'},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name': '공지사항', 'verbose_name_plural': '공지사항'},
        ),
        migrations.AlterModelOptions(
            name='onlineform',
            options={'verbose_name': '_문의', 'verbose_name_plural': '_문의'},
        ),
        migrations.AlterModelOptions(
            name='success',
            options={'verbose_name': '합격자', 'verbose_name_plural': '합격자'},
        ),
    ]
