from django.contrib import admin
from django.utils.html import format_html
from django import forms

from .models import SellerProfile, Catalogue, Certification, CataloguePage, Video,ProductImage, Product, Category, SubCategory

# class SellerProfileAdmin(admin.ModelAdmin):
#     list_display = ['company_name', 'is_in_catalogue']
#     list_filter = ['is_in_catalogue']
#     search_fields = [' company_name', 'company_location']

#     def activate_in_catalogue(self, request, queryset):
#         queryset.update(is_in_catalogue=True)
#     activate_in_catalogue.short_description = "Activate selected companies in the catalogue"
    
#     def deactivate_from_catalogue(self, request, queryset):
#         queryset.update(is_in_catalogue=False)
#     deactivate_from_catalogue.short_description = "Deactivate selected companies from the catalogue"
    
#     actions = [activate_in_catalogue, deactivate_from_catalogue]



# class CatalogueAdmin(admin.ModelAdmin):
#     list_display = ['SellerProfile', 'added_on']
#     search_fields = ['company__name']

# admin.site.register(Catalogue, CatalogueAdmin)



admin.site.register(SellerProfile) 
# admin.site.register(SellerProfile,SellerProfileAdmin) 
admin.site.register(Certification)





class CataloguePageAdmin(admin.ModelAdmin):
    list_display = ('page_number', 'page_image')
    filter_horizontal = ('sellers',)

admin.site.register(Catalogue)
admin.site.register(CataloguePage, CataloguePageAdmin)


admin.site.register(Video)
# admin.site.register(ProductImage)
admin.site.register(Product)





# Create a custom form for the ProductImage model
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product', 'image', 'image_title']  # Include all necessary fields

    def clean_image(self):
        image = self.cleaned_data.get('image', None)
        if not image:
            return image  # Don't modify if no image is uploaded
        return image

class ProductImageAdmin(admin.ModelAdmin):
    form = ProductImageForm
    list_display = ('get_image', 'get_company_name', 'product')

    fieldsets = (
        (None, {
            'fields': ('product', 'image', 'image_title')
        }),
    )
    list_filter = ('product',)

    def get_image(self, obj):
        if obj.image:
            return format_html('<a href="{}" target="_blank"><img src="{}" style="width: 50px; height: auto;" /></a>', obj.image.url, obj.image.url)
        return "No Image"
    get_image.short_description = 'Image'
    
    def get_company_name(self, obj):
        return obj.product.SellerProfile.company_name if obj.product and obj.product.SellerProfile else 'No Company'
    get_company_name.short_description = 'Seller Company Name'

    # This allows you to save the model, including replacing the image
    def save_model(self, request, obj, form, change):
        if form.cleaned_data['image']:
            obj.image = form.cleaned_data['image']  # Allow image to be replaced if uploaded
        obj.save()

# Register the custom admin for ProductImage
admin.site.register(ProductImage, ProductImageAdmin)




class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'icon')  # Display icon in list view
    search_fields = ('name', 'category__name', 'icon')  # Allow search by icon as well
    list_filter = ('category',)  # Filter by category
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'icon')
        }),
    )

admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category)
