# Generated by Django 4.2.16 on 2024-09-25 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("submenu_3", "0004_submenu3_on_click_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="submenu3",
            old_name="on_click_url",
            new_name="display_title",
        ),
    ]
