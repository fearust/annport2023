# Generated by Django 4.1.4 on 2023-01-03 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_announcertag2_alter_announcer_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='성함')),
                ('phoneNumber', models.CharField(max_length=20, verbose_name='연락처')),
                ('corp', models.CharField(max_length=50, verbose_name='기업단체명')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='이메일')),
                ('customer_memo', models.TextField(blank=True, verbose_name='문의내용')),
                ('staff_memo', models.TextField(blank=True, verbose_name='스탭메모')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
            ],
            options={
                'verbose_name': '_문의',
                'verbose_name_plural': '_문의',
            },
        ),
    ]
