# Generated by Django 4.2.7 on 2024-04-06 09:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("billsystem2", "0002_signup"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="signup",
            new_name="signups",
        ),
    ]
