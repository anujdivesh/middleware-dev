# Generated by Django 4.2.16 on 2024-09-25 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submenu_3", "0003_alter_submenu3_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="submenu3",
            name="on_click_url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
