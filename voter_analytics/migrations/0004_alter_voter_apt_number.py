# Generated by Django 5.1.3 on 2024-11-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voter_analytics", "0003_voter_apt_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="voter",
            name="apt_number",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]