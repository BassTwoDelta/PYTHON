# Generated by Django 2.2.4 on 2020-06-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_review_app', '0003_item_wish_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='wish_list',
            field=models.ManyToManyField(related_name='wish_items', to='belt_review_app.User'),
        ),
    ]
