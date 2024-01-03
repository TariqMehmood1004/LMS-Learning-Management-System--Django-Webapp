# Generated by Django 4.2.5 on 2024-01-03 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]