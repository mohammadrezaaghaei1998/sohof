# Generated by Django 5.1.4 on 2025-03-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_aboutusvideo_delete_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_page_video', models.FileField(blank=True, null=True, upload_to='home_page_video/')),
            ],
        ),
    ]
