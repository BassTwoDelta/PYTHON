# Generated by Django 2.2.4 on 2020-06-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='description',
            field=models.CharField(default='No Description', max_length=255),
            preserve_default=False,
        ),
    ]
