# Generated by Django 5.1.4 on 2025-02-21 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us_video', models.FileField(blank=True, null=True, upload_to='about_us_videos/')),
            ],
        ),
    ]
