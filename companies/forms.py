from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import CustomUser
from .models import SellerProfile, Certification, Video, Product, ProductImage,SubCategory


from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class SellerSignupForm(UserCreationForm):
    # Seller profile fields
    company_name = forms.CharField(required=True)
    company_address = forms.CharField(widget=forms.Textarea, required=True)
    website_url = forms.URLField(required=True)
    fields_of_work = forms.ChoiceField(choices=SellerProfile._meta.get_field('fields_of_work').choices, required=True)
    company_description = forms.CharField(widget=forms.Textarea, required=True)
    company_location = forms.CharField(required=True)
    year_established = forms.IntegerField(required=True)
    company_size = forms.IntegerField(required=False)
    contact_email = forms.EmailField(required=True)
    company_logo = forms.ImageField(required=False)

    # Additional fields
    full_name = forms.CharField(required=True)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)), required=True)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=True)
    phone_number = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    country = forms.CharField(required=True)

    # New field for contract confirmation
    accepted_terms = forms.BooleanField(required=True, label="I accept the terms and conditions")

    # New username field
    username = forms.CharField(required=True, max_length=150)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        # Set user type as seller
        user.email = self.cleaned_data['email_address'] 
        user.user_type = "seller"

        if commit:
            user.save()
            SellerProfile.objects.create(
                user=user,
                company_name=self.cleaned_data['company_name'],
                company_address=self.cleaned_data['company_address'],
                website_url=self.cleaned_data['website_url'],
                fields_of_work=self.cleaned_data['fields_of_work'],
                company_description=self.cleaned_data['company_description'],
                company_location=self.cleaned_data['company_location'],
                year_established=self.cleaned_data['year_established'],
                company_size=self.cleaned_data['company_size'],
                contact_email=self.cleaned_data['contact_email'],
                company_logo=self.cleaned_data.get('company_logo'),
                full_name=self.cleaned_data['full_name'],
                date_of_birth=self.cleaned_data['date_of_birth'],
                gender=self.cleaned_data['gender'],
                phone_number=self.cleaned_data['phone_number'],
                email_address=self.cleaned_data['email_address'],
                address=self.cleaned_data['address'],
                country=self.cleaned_data['country'],
                company_license=self.cleaned_data['company_license'],
                id_card=self.cleaned_data.get('id_card'),
                passport=self.cleaned_data.get('passport'),
                certificates=self.cleaned_data.get('certificates'),
                tax_registration=self.cleaned_data.get('tax_registration'),
                utility_bill=self.cleaned_data.get('utility_bill'),
                bank_statement=self.cleaned_data.get('bank_statement'),
                accepted_terms=self.cleaned_data['accepted_terms']
            )
        return user



class SellerLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))












class SellerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = SellerProfile
        exclude = ['company_logo', 'company_license', 'tax_registration', 'utility_bill',
                    'bank_statement', 'user', 'company_address', 'full_name',
                      'date_of_birth', 'gender', 'phone_number', 'email_address', 'address', 'country','profile_views'
                  ]





class SellerProfileDocumentUpdateForm(forms.ModelForm):
    class Meta:
        model = SellerProfile
        fields = ['company_logo', 'company_license', 'tax_registration', 'utility_bill', 'bank_statement','id_card','passport']





class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['title', 'description', 'image']





class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video_file'] 







class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'origin', 'description', 'availability', 'category', 'subcategory']
    
    # Dynamically update subcategories based on selected category
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # If category is not selected or invalid, do nothing
        else:
            self.fields['subcategory'].queryset = SubCategory.objects.none()



class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']