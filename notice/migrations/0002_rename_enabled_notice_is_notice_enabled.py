from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notice", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notice",
            old_name="enabled",
            new_name="is_notice_enabled",
        ),
    ]
