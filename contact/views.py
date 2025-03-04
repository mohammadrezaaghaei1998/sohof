from django.shortcuts import render,redirect
from .forms import ContactUsForm
from django.contrib import messages

# Create your views here.




from django.http import JsonResponse

def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)  # Bind the POST data to the form
        if form.is_valid():
            form.save()  # Save the form to the database
            return JsonResponse({
                'status': 'success',
                'message': 'Your message has been sent successfully!'
            })
        else:
            # If there are form errors, return them as JSON
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = error_list
            return JsonResponse({
                'status': 'error',
                'errors': errors
            })
    else:
        form = ContactUsForm()  # Empty form for GET request
    return render(request, 'first/aboutus.html', {'form': form})
