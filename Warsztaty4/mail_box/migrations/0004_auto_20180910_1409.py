# Generated by Django 2.0.3 on 2018-09-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_box', '0003_auto_20180910_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='flat_no',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='house_no',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
