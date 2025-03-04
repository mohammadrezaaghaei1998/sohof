from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('product', views.product, name='product'),
    path('log_reg', views.log_reg, name='log_reg'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),

    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),

    path('logout/', views.user_logout, name='logout'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist_view'),
    path('remove-from-wishlist/', views.remove_from_wishlist, name='remove_from_wishlist'),


    path('change-password/', views.change_password, name='change_password'),


    path('restrictions/', views.restrictions, name='restrictions'),


    path('search/', views.search_view, name='search'),    

    # path('subcategory/<int:subcategory_id>/', views.subcategory_products_view, name='subcategory_products'),



    # path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    # path('filter-products/', views.filter_products, name='filter-products'),
   


]