from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import BuyerLoginForm, BuyerSignupForm
from accounts.models import CustomUser
from django.contrib import messages
from companies.models import Product,Product, SellerProfile,Catalogue
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import BuyerProfile , Wishlist,Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from about_us.models import AboutUsVideo, HomePageVideo
from companies .models import Category
from socialmedia.models import SocialMediaLinks
from django.contrib.auth.decorators import login_required
from .forms import  BuyerProfileForm
from advertising.models import Advertisement
# Create your views here.



def index(request):
    socialmedia = SocialMediaLinks.objects.all()
    catalogues = Catalogue.objects.all() 
    categories = Category.objects.all()
    homepagevideos = HomePageVideo.objects.all()
    advertisement = Advertisement.objects.all()
    return render(request, 'first/index.html', {'catalogues': catalogues , 'categories': categories ,'socialmedia' : socialmedia , 'homepagevideos' : homepagevideos ,'advertisement' : advertisement})



def aboutus(request):
    socialmedia = SocialMediaLinks.objects.all()
    aboutusvideos = AboutUsVideo.objects.all()
    return render(request, 'first/aboutus.html', {'aboutusvideos': aboutusvideos ,'socialmedia' : socialmedia})



def product(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 6) 

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    total_products = Product.objects.count()  

    return render(request, 'first/product.html', {'products': products, 'total_products': total_products})



def product_detail(request, product_id):
    socialmedia = SocialMediaLinks.objects.all()
    product = get_object_or_404(Product, id=product_id)
    seller = product.SellerProfile 

    return render(request, 'first/product_detail.html', {
        'product': product,
        'seller': seller,
        'socialmedia' : socialmedia
    })









# def log_reg(request):
#     if request.user.is_authenticated and request.user.user_type == "seller":
#         return redirect('restrictions')
#     form = None  

#     if request.method == "POST":
#         if 'login' in request.POST:
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 if user.user_type == "buyer":
#                     login(request, user)
#                     messages.success(request, "Login successful! Welcome back.")
#                     return redirect("index")
#                 else:
#                     messages.error(request, "Invalid credentials for a buyer account.")
#             else:
#                 messages.error(request, "Invalid username or password.")
#         elif 'signup' in request.POST:
#             form = BuyerSignupForm(request.POST)
#             if form.is_valid():
#                 email = form.cleaned_data.get('email')
#                 if CustomUser.objects.filter(email=email).exists():
#                     messages.error(request, "This email is already registered. Please use a different email.")
#                 else:
#                     user = form.save(commit=False)
#                     user.user_type = "buyer"
#                     user.save()
#                     messages.success(request, "Signup successful! You can now log in.")
#                     return redirect("index")
#             else:
#                 messages.error(request, "There was an error with your signup form.")
#                 for field in form.errors:
#                     messages.error(request, f"{field.capitalize()} : {form.errors[field]}")
#     else:
#         form = BuyerLoginForm()  

#     return render(request, 'first/log_reg.html', {"form": form})


def log_reg(request):
    if request.user.is_authenticated:
        if request.user.user_type == "seller":
            logout(request) 
            return redirect('restrictions')  

    form = None  

    if request.method == "POST":
        if 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.user_type == "buyer":
                    login(request, user)
                    messages.success(request, "Login successful! Welcome back.")
                    return redirect("index")
                else:
                    messages.error(request, "Invalid credentials for a buyer account.")
            else:
                messages.error(request, "Invalid username or password.")
        elif 'signup' in request.POST:
            form = BuyerSignupForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, "This email is already registered. Please use a different email.")
                else:
                    user = form.save(commit=False)
                    user.user_type = "buyer"
                    user.save()
                    messages.success(request, "Signup successful! You can now log in.")
                    return redirect("index")
            else:
                messages.error(request, "There was an error with your signup form.")
                for field in form.errors:
                    messages.error(request, f"{field.capitalize()} : {form.errors[field]}")
    else:
        form = BuyerLoginForm()  

    return render(request, 'first/log_reg.html', {"form": form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()  
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_dashboard') 
        else:
            messages.error(request, 'There was an error with your password change.')
    else:
        form = PasswordChangeForm(request.user)  

    return render(request, 'first/change_password.html', {'form': form})




def restrictions(request):
    socialmedia = SocialMediaLinks.objects.all()
    return render(request, 'first/restrictions.html',{ 'socialmedia' : socialmedia})





# def user_dashboard(request):
#     if not request.user.is_authenticated:
#         return redirect('log_reg')  

#     if hasattr(request.user, 'sellerprofile'):
#         return redirect('company_login')  

#     wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product', 'product__SellerProfile')

#     try:
#         user_profile = BuyerProfile.objects.get(user=request.user)
#     except BuyerProfile.DoesNotExist:
#         user_profile = BuyerProfile.objects.create(user=request.user)

#     if request.method == 'POST':
#         form = BuyerProfileForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully!")
#             return redirect('user_dashboard')
#     else:
#         form = BuyerProfileForm(instance=user_profile)

#     products = [item.product for item in wishlist_items]
#     return render(request, 'first/user_dashboard.html', {
#         'user_profile': user_profile,
#         'form': form,
#         'wishlist_items': wishlist_items,
#         'products': products,
#     })


def user_dashboard(request):
    socialmedia = SocialMediaLinks.objects.all()
    if not request.user.is_authenticated:
        return redirect('log_reg')  

    if hasattr(request.user, 'sellerprofile'):
        return redirect('company_login')  

    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product', 'product__SellerProfile')

    try:
        user_profile = BuyerProfile.objects.get(user=request.user)
    except BuyerProfile.DoesNotExist:
        user_profile = BuyerProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = BuyerProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # Update CustomUser fields
            request.user.username = form.cleaned_data['username']
            request.user.email = form.cleaned_data['email']
            request.user.save()

            # Save the profile
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('user_dashboard')
    else:
        form = BuyerProfileForm(instance=user_profile)

    products = [item.product for item in wishlist_items]
    return render(request, 'first/user_dashboard.html', {
        'user_profile': user_profile,
        'form': form,
        'wishlist_items': wishlist_items,
        'products': products,
        'socialmedia' : socialmedia
    })



def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("index") 













@csrf_exempt
@login_required
def add_to_wishlist(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        
        try:
            product = Product.objects.get(id=product_id)
            wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
            
            print(f'Product {product.name} added to wishlist.')  
            
            if created:
                return JsonResponse({'success': True, 'message': 'Product added to wishlist.'})
            else:
                return JsonResponse({'success': False, 'message': 'Product is already in your wishlist.'})
        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Product not found.'})

    return JsonResponse({'success': False, 'message': 'Invalid request.'})




@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    products_in_wishlist = [item.product for item in wishlist_items]


    
    return render(request, 'user_dashboard.html', {'products_in_wishlist': products_in_wishlist})







@csrf_exempt
@login_required
def remove_from_wishlist(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        try:
            wishlist_item = Wishlist.objects.get(user=request.user, product_id=product_id)
            wishlist_item.delete()
            return JsonResponse({'success': True, 'message': 'Removed from wishlist.'})
        except Wishlist.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Item not found in wishlist.'})

    return JsonResponse({'success': False, 'message': 'Invalid request.'})




def search_view(request):
    query = request.GET.get('q', '')

    if query:
        products = Product.objects.filter(name__icontains=query)
        categories = set(product.category for product in products if product.category)
        subcategories = set(product.subcategory for product in products if product.subcategory)
    else:
        products = Product.objects.none()
        categories = set()
        subcategories = set()

    return render(request, 'first/search_result.html', {
        'query': query,
        'products': products,
        'categories': categories,
        'subcategories': subcategories,
    })
