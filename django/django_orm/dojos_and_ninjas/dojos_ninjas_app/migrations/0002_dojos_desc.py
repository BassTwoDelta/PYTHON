# Generated by Django 2.2.4 on 2020-06-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojos_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default='old dojo', verbose_name='old dojo'),
            preserve_default=False,
        ),
    ]
