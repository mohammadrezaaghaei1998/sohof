# Generated by Django 5.1.4 on 2025-02-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_catalogue_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_url',
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='seller_dashboard_videos/'),
        ),
    ]
