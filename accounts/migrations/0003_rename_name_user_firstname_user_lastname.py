# Generated by Django 5.0.6 on 2024-09-28 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.TextField(null=True),
        ),
    ]
