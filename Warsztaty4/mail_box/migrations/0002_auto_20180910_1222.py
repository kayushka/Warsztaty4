# Generated by Django 2.0.3 on 2018-09-10 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail_box', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='image',
        ),
        migrations.AlterField(
            model_name='person',
            name='adres',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mail_box.Address'),
        ),
    ]
