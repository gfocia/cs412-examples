# Generated by Django 5.1.3 on 2024-12-03 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0003_statusmessage"),
    ]

    operations = [
        migrations.AddField(
            model_name="outfitidea",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="outfit_idea_images/"
            ),
        ),
    ]