from .models import Category
from socialmedia .models import SocialMediaLinks

def categories_processor(request):
    categories = Category.objects.prefetch_related('subcategories')
    return {'categories': categories}




def social_media_links(request):
    links = SocialMediaLinks.objects.all()
    return {'social_media_links': links}