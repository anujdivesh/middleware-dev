# Generated by Django 4.2.16 on 2024-09-17 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0006_dataset_convert_longitude"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataset",
            name="convert_longitude",
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
