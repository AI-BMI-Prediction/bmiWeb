# Generated by Django 3.2.16 on 2022-12-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='label',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='predict_label',
            field=models.IntegerField(default=None),
        ),
    ]