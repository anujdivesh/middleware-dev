# Generated by Django 4.2.16 on 2024-09-25 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submenu_1", "0002_alter_submenu1_children"),
    ]

    operations = [
        migrations.AddField(
            model_name="submenu1",
            name="display_title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
