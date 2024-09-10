# Generated by Django 4.2.16 on 2024-09-10 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "layer_web_map",
            "0003_layerwebmap_datetime_format_layerwebmap_on_click_url_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="layerwebmap",
            name="update_color",
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="layerwebmap",
            name="update_legend",
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="layerwebmap",
            name="update_transparency",
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
