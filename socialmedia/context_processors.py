from .models import SocialMediaLinks




def social_media_links(request):
    links = SocialMediaLinks.objects.all()
    return {'social_media_links': links}