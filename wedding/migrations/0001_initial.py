# Generated by Django 4.1.4 on 2022-12-28 23:57

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import wedding.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backdrops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=wedding.models.PathAndRename('wedding/profile_backdrop/'), verbose_name='배경사진')),
                ('backdrop_name', models.CharField(blank=True, max_length=50, verbose_name='배경이미지제목')),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bride', models.CharField(blank=True, max_length=20, verbose_name='신부님 성함')),
                ('groom', models.CharField(blank=True, max_length=20, verbose_name='신랑님 성함')),
                ('bride_phone', models.CharField(blank=True, max_length=20, verbose_name='신부님 연락처')),
                ('groom_phone', models.CharField(blank=True, max_length=20, verbose_name='신랑님 연락처')),
                ('wedding_date', models.CharField(blank=True, max_length=100, null=True, verbose_name='본식 날짜,시간')),
                ('wedding_place', models.CharField(blank=True, max_length=50, verbose_name='본식 장소')),
                ('officiator', models.BooleanField(default=False, verbose_name='주례')),
                ('wedding_reception', models.BooleanField(default=False, verbose_name='2부 진행')),
                ('email_addr', models.EmailField(blank=True, max_length=254, verbose_name='메일주소')),
                ('wish_mc', models.CharField(blank=True, max_length=100, verbose_name='희망 사회자')),
                ('customer_memo', models.TextField(blank=True, verbose_name='고객 메모')),
                ('staff_memo', models.TextField(blank=True, verbose_name='스탭 메모')),
                ('create_date', models.DateTimeField(verbose_name='문의시간')),
            ],
        ),
        migrations.CreateModel(
            name='Mc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('title', models.CharField(max_length=20, verbose_name='호칭')),
                ('description', models.TextField(verbose_name='설명')),
                ('profile_photo', models.ImageField(upload_to=wedding.models.PathAndRename('wedding/profile_photo/'), verbose_name='프로필사진')),
                ('profile', models.TextField(blank=True, verbose_name='프로필')),
                ('mcdisplay', models.BooleanField(default=True, verbose_name='홈페이지노출여부')),
                ('mcmain', models.BooleanField(default=False, verbose_name='메인사회자')),
                ('profile_backdrop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wedding.backdrops')),
            ],
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=20, verbose_name='유튜브일련번호')),
                ('wedding_mc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding.mc')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=wedding.models.PathAndRename('wedding/gallery/'), verbose_name='사회자사진')),
                ('wedding_mc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding.mc')),
            ],
        ),
    ]
