from django.db import models

# Create your models here.



class Advertisement(models.Model):
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    website = models.URLField()
    image = models.ImageField(upload_to='advertisements/')

    def __str__(self):
        return self.company_name
