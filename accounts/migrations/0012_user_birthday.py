# Generated by Django 5.0.6 on 2024-09-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_gender_search_user_looking_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(max_length=20, null=True),
        ),
    ]
