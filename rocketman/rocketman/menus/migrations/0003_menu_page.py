# Generated by Django 3.1.2 on 2020-10-17 17:48

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='page',
            field=modelcluster.fields.ParentalKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='menus.menu'),
            preserve_default=False,
        ),
    ]
