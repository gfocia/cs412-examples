# Generated by Django 4.2.16 on 2024-11-03 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mini_fb", "0005_profile_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
    ]
