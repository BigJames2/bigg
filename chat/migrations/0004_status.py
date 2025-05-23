# Generated by Django 5.0.6 on 2025-03-02 08:38

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chatroom_chatmessage_delete_message'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status_type', models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('video', 'Video')], default='text', max_length=10)),
                ('content', models.TextField(blank=True, null=True)),
                ('media', models.FileField(blank=True, null=True, upload_to='status_media/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
