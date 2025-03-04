from django.urls import path
from . import views

urlpatterns = [
   
    path('seller_detail/<int:seller_id>/', views.seller_detail, name='seller_detail'),
    path('seller_dashboard', views.seller_dashboard, name='seller_dashboard'),
    path('company_registeration', views.company_registeration, name='company_registeration'),
    path('company_signup', views.company_signup, name='company_signup'),
    path('company_login', views.company_login, name='company_login'),
    path('seller_change_password/', views.seller_change_password, name='seller_change_password'),
    path('restriction', views.restriction, name='restriction'),


    path('catalogues', views.catalogues, name='catalogues'),
    path('catalogue_detail/<int:catalogue_id>/', views.catalogue_detail, name='catalogue_detail'),
    path('page_detail/<int:page_id>/', views.page_detail, name='page_detail'),
    path('catalogue_download/<int:catalogue_id>/', views.download_catalogue, name='catalogue_download'),
    path('catalogue/<int:catalogue_id>/increase-view/', views.increase_catalogue_view, name='increase_catalogue_view'),



    path('submit-business-info/', views.submit_business_info, name='submit_business_info'),
    path('manage-documents/', views.manage_documents, name='manage_documents'),
    path('manage_certifications/', views.manage_certifications, name='manage_certifications'),
    path('remove_certification/<int:cert_id>/', views.remove_certification, name='remove_certification'),





    path('add_video/', views.add_video, name='add_video'),
    path('remove_video/<int:video_id>/', views.remove_video, name='remove_video'),



    path('add-product/', views.add_product, name='add_product'),
    path('remove-product/<int:product_id>/', views.remove_product, name='remove_product'),
    path('edit-product/', views.edit_product, name='edit_product'),


    path('get_subcategories/<int:category_id>/', views.get_subcategories, name='get_subcategories'),



    path('subcategory/<int:subcategory_id>/', views.subcategory_products_view, name='subcategory_products'),
]


