from django.db import models

# Create your models here.


class SocialMediaLinks(models.Model):
    social_media_url = models.URLField(blank=False, null=False, default='https://www.instagram.com/')

    def __str__(self):
        return self.social_media_url
