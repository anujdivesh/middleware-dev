# Generated by Django 4.2.16 on 2024-09-17 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0005_alter_dataset_download_file_infix_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataset",
            name="convert_longitude",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
