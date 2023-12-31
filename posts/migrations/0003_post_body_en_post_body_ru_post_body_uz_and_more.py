# Generated by Django 4.2.4 on 2023-08-19 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_category_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='summary_en',
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='summary_ru',
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='summary_uz',
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_uz',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
