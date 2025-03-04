from django.db import models

# Create your models here.




class AboutUsVideo(models.Model):
    about_us_video = models.FileField(upload_to='about_us_videos/', blank=True, null=True)

    def __str__(self):
        return str(self.about_us_video)  

class HomePageVideo(models.Model):
    home_page_video = models.FileField(upload_to='home_page_video/', blank=True, null=True)

    def __str__(self):
        return str(self.home_page_video)  
