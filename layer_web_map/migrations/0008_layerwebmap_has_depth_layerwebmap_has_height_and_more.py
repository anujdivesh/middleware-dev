# Generated by Django 4.2.16 on 2024-09-23 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "layer_web_map",
            "0007_layerwebmap_chart_style_layerwebmap_enable_chart_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="layerwebmap",
            name="has_depth",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="layerwebmap",
            name="has_height",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="layerwebmap",
            name="update_thredds",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
