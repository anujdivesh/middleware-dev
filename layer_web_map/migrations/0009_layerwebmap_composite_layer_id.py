# Generated by Django 4.2.16 on 2024-09-24 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("layer_web_map", "0008_layerwebmap_has_depth_layerwebmap_has_height_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="layerwebmap",
            name="composite_layer_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
