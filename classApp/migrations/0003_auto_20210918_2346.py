# Generated by Django 2.0.7 on 2021-09-19 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0002_auto_20210918_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='Course_Number',
            field=models.IntegerField(),
        ),
    ]