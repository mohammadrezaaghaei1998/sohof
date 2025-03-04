from django.db import models
from accounts.models import CustomUser
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now, timedelta
from django.db.models import Sum
# Create your models here.



# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     is_company = models.BooleanField(default=False)  



class SellerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="seller_profile")
    company_name = models.CharField(max_length=255, null=False, blank=False,default='Sohof')
    company_address = models.TextField(null=False, blank=False,default="No address provided")
    website_url = models.URLField(blank=False, null=False,default='www.example.com')
    fields_of_work = models.CharField(max_length=255, choices=[
        ('technology', 'Technology'),
        ('consulting', 'Consulting'),
        ('manufacturing', 'Manufacturing'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('finance', 'Finance'),
        ('agriculture', 'Agriculture'),
        ('automotive', 'Automotive'),
        ('construction', 'Construction'),
        ('real-estate', 'Real Estate'),
        ('retail', 'Retail'),
        ('hospitality', 'Hospitality'),
        ('entertainment', 'Entertainment'),
        ('logistics', 'Logistics'),
        ('transportation', 'Transportation'),
        ('energy', 'Energy'),
        ('environmental-services', 'Environmental Services'),
        ('telecommunications', 'Telecommunications'),
        ('food-and-beverage', 'Food and Beverage'),
        ('pharmaceuticals', 'Pharmaceuticals'),
        ('media', 'Media'),
        ('arts-and-culture', 'Arts and Culture'),
        ('sports', 'Sports'),
        ('legal-services', 'Legal Services'),
        ('nonprofit', 'Nonprofit'),
        ('government', 'Government'),
        ('mining', 'Mining'),
        ('aerospace', 'Aerospace'),
        ('defense', 'Defense'),
        ('fashion', 'Fashion'),
        ('beauty-and-cosmetics', 'Beauty and Cosmetics'),
        ('cleaning-services', 'Cleaning Services'),
        ('technology-services', 'Technology Services'),
        ('cybersecurity', 'Cybersecurity'),
        ('blockchain-and-cryptocurrency', 'Blockchain and Cryptocurrency'),
        ('e-commerce', 'E-Commerce'),
        ('venture-capital', 'Venture Capital'),
        ('insurance', 'Insurance'),
        ('event-management', 'Event Management'),
        ('travel-and-tourism', 'Travel and Tourism'),
        ('petroleum', 'Petroleum'),
        ('biotechnology', 'Biotechnology'),
        ('research-and-development', 'Research and Development'),
        ('engineering', 'Engineering'),
        ('human-resources', 'Human Resources'),
        ('business-services', 'Business Services'),
        ('printing-and-publishing', 'Printing and Publishing'),
        ('handicrafts', 'Handicrafts'),
        ('marine-industry', 'Marine Industry'),
        ('architecture', 'Architecture'),
        ('interior-design', 'Interior Design'),
        ('artificial-intelligence', 'Artificial Intelligence'),
        ('robotics', 'Robotics'),
        ('gaming', 'Gaming'),
        ('fitness-and-wellness', 'Fitness and Wellness'),
        ('personal-care', 'Personal Care'),
        ('luxury-goods', 'Luxury Goods'),
        ('forestry', 'Forestry'),
        ('security-services', 'Security Services'),
        ('aviation', 'Aviation'),
        ('childcare', 'Childcare'),
        ('translation-services', 'Translation Services'),
        ('antiques-and-collectibles', 'Antiques and Collectibles'),
        ('recycling', 'Recycling'),
        ('marine-tourism', 'Marine Tourism')
    ], blank=False, null=False, default='technology')
    company_description = models.TextField(null=False, blank=False,default='company_description')
    company_location = models.CharField(max_length=255, null=False, blank=False, default='Unknown location')
    year_established = models.PositiveIntegerField( null=False, blank=False, default=2000)
    company_size = models.PositiveIntegerField(blank=True, null=True, default=0)
    contact_email = models.EmailField(null=False, blank=False, default='contact@example.com')
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    
    # Additional fields
    full_name = models.CharField(max_length=255, null=False, blank=False, default='John Doe')
    date_of_birth = models.DateField(null=False, blank=False, default=date(1900, 1, 1))
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], null=False, blank=False,default='Male')
    phone_number = models.CharField(max_length=20, null=False, blank=False, default='+968 2020 2020')
    email_address = models.EmailField( null=False, blank=False,default="No address provided")
    address = models.CharField(max_length=255, null=False, blank=False,default="No address provided")
    country = models.CharField(max_length=255, null=False, blank=False, default='Oman')

    # Upload fields
    company_license = models.FileField(upload_to='uploads/company_licenses/', null=False, blank=False, default='uploads/company_licenses/default_license.pdf')
    id_card = models.FileField(upload_to='uploads/id_cards/', blank=True, null=True)
    passport = models.FileField(upload_to='uploads/passports/', blank=True, null=True)
    certificates = models.FileField(upload_to='uploads/certificates/', blank=True, null=True)
    tax_registration = models.FileField(upload_to='uploads/tax_registration/', blank=True, null=True)
    utility_bill = models.FileField(upload_to='uploads/utility_bills/', blank=True, null=True)
    bank_statement = models.FileField(upload_to='uploads/bank_statements/', blank=True, null=True)

    # New field for contract confirmation
    accepted_terms = models.BooleanField(default=False, help_text="Indicates if the user has accepted the terms and conditions.", null=False, blank=False)




    # Rest info for seller dashboard
    accepted_languages = models.CharField(max_length=255, blank=True, null=True)
    floor_space = models.FloatField(blank=True, null=True)  
    years_exporting = models.IntegerField(blank=True, null=True)
    annual_export_revenue = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)  
    years_in_industry = models.IntegerField(blank=True, null=True)

    # Production Details
    production_lines = models.IntegerField(blank=True, null=True)
    production_machines = models.IntegerField(blank=True, null=True)
    product_support_traceability = models.BooleanField(blank=True, null=True)
    product_inspection_method = models.TextField(blank=True, null=True)
    quality_control_on_lines = models.BooleanField(blank=True, null=True)
    qa_qc_inspectors = models.IntegerField(blank=True, null=True)

    # Markets and Partners
    main_markets = models.TextField(blank=True, null=True)
    supply_chain_partners = models.TextField(blank=True, null=True)
    main_client_types = models.TextField(blank=True, null=True)

 
    # R&D
    rd_engineer_education_levels = models.CharField(max_length=255, blank=True, null=True)
    rd_engineers = models.IntegerField(blank=True, null=True)
    customization_options = models.TextField(blank=True, null=True)
    new_products_last_year = models.IntegerField(blank=True, null=True)

    # Social Media
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    other_social_media = models.JSONField(blank=True, null=True)


 
    # Contact Information
    export_manager_name = models.CharField(max_length=255, blank=True, null=True)
    responsible_person_name = models.CharField(max_length=255, blank=True, null=True)
    company_phone = models.CharField(max_length=20, blank=True, null=True)
    company_fax = models.CharField(max_length=20, blank=True, null=True)
    company_location = models.CharField(max_length=255, blank=True, null=True)


    # Catalogue Flag
    is_in_catalogue = models.BooleanField(default=False)


    # Track profile views
    profile_views = models.PositiveIntegerField(default=0)  
    daily_views = models.PositiveIntegerField(default=0)  
    weekly_views = models.PositiveIntegerField(default=0)

    is_verified = models.BooleanField(default=False)
    is_gold = models.BooleanField(default=False)


    def update_views(self):
        """
        Update the total, daily, and weekly profile views.
        """
        today = now().date()
        week_start = today - timedelta(days=6)  

        self.profile_views += 1

        views_today = ProfileViewLog.objects.filter(seller=self, date=today).count()
        self.daily_views = views_today

        views_week = ProfileViewLog.objects.filter(seller=self, date__gte=week_start).count()
        self.weekly_views = views_week

        self.save()


    def calculate_percentage_change(self):
        """
        Calculate the percentage change in profile views over the last 30 days.
        """
        today = now().date()
        thirty_days_ago = today - timedelta(days=30)

        old_views = ProfileViewLog.objects.filter(seller=self, date__gte=thirty_days_ago).count()
        current_views = self.profile_views

        print(f"Debug: Old Views = {old_views}, Current Views = {current_views}")  

        if old_views == 0:  
            if current_views > 0:
                print("Debug: No previous views, but current views exist. Returning 100% increase.")
                return 100  
            else:
                print("Debug: No views at all. Returning 0% change.")
                return 0  

        percentage_change = ((current_views - old_views) / old_views) * 100
        print(f"Debug: Percentage Change = {percentage_change}%")

        return percentage_change





    def __str__(self):
        return f"Seller Profile: {self.company_name} ({self.user.username})"






class ProfileViewLog(models.Model):
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE, related_name="view_logs")
    date = models.DateField(auto_now_add=True)


class Video(models.Model):
    SellerProfile = models.ForeignKey('SellerProfile', related_name='sellerprofileVideos', on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='seller_dashboard_videos/', blank=True, null=True)
    video_title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.video_title or self.SellerProfile.company_name
    

    
class Certification(models.Model):
    SellerProfile = models.ForeignKey('SellerProfile', related_name='sellerprofileCertifications', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='sellerprofilecertifications/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or "No Title Provided"







class Catalogue(models.Model):
    SellerProfile = models.ForeignKey('SellerProfile', related_name='sellerprofilecatalogue', on_delete=models.CASCADE, null=True , blank=True)
    added_on = models.DateField(auto_now_add=True)

    publish_date = models.DateField(null=False, blank=False, default=timezone.now)
    creator = models.CharField(max_length=255, null=False, blank=False, default="Sohof")
    language = models.CharField(max_length=50, null=False, blank=False, default="English")
    download_count = models.PositiveIntegerField(default=0)
    pages = models.PositiveIntegerField(default=50) 
    companies = models.PositiveIntegerField(default=100) 
    cover_image = models.ImageField(upload_to='catalogues/covers/', blank=True, null=True) 
    view_count = models.PositiveIntegerField(default=0) 


    # def __str__(self):
    #     return f"Catalogue Entry for {self.SellerProfile.company_name}"


class CataloguePage(models.Model):
    catalogue = models.ForeignKey(Catalogue, related_name='catalogue_pages', on_delete=models.CASCADE)  
    page_image = models.ImageField(upload_to='catalogue_pages/', blank=True, null=True)
    sellers = models.ManyToManyField(SellerProfile, related_name='catalogue_pages')
    page_number = models.PositiveIntegerField(default=1) 

    def __str__(self):
        return f"Page {self.page_number}"






class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
         return self.name or "No Name Provided"

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True, help_text="Font Awesome icon class (e.g., 'fa-pagelines')")

    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
          return self.name or "No Name Provided"

class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    origin = models.CharField(max_length=255, blank=True, null=True)
    popularity = models.PositiveIntegerField(default=0)

    availability_choices = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock')
    ]

    availability = models.CharField(max_length=20, choices=availability_choices, blank=True, null=True)
    SellerProfile = models.ForeignKey(SellerProfile, related_name='products', on_delete=models.CASCADE, blank=True, null=True)

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=None , null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE, default=None , null=True, blank=True)

    def increase_views(self):
        self.views += 1
        self.save()

    def __str__(self):
        return self.name or "No Name Provided"







class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=False, null=False)
    image_title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.image_title or "No Title Provided"





