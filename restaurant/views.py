from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random
# Create your views here.

image = "https://img.hoodline.com/2024/1/raising-canes-serves-up-its-signature-chicken-tenders-at-new-downtown-crossing-location-in-boston-1.webp"

# This view represents the main page with basic information about the restaurant 
def main(request): 

    template_name = "restaurant/main.html"

    context = { 
        'image': image, 
    }

    return render(request, template_name, context)

# This view will display an online order form 
def order(request):

    template_name = "restaurant/order.html"

    return render(request, template_name)

# This view will display a conformation page after the order is placed 
def confirmation(request):

    template_name = "restaurant/confirmation.html"

    return render(request, template_name)

# This view will handle the form submission, new for assignment 4 
def submit(request):
    '''
    Handle the form submission. 
    Read out the form data. 
    Generate a response.
    '''
    template_name = 'restaurant/confirmation.html'
    # print(request)
    
    # check if the request is a POST (vs GET)
    if request.POST:

        name = request.POST.get('name')

        selected_items = request.POST.getlist('options') 

        box_combo_option = request.POST.get('box_combo_option')
        if 'The Box Combo' in selected_items and box_combo_option:
            selected_items.append(f"{box_combo_option} for The Box Combo")

        formatted_items = ', '.join(selected_items)


        # package the data up to be used in response
        context = {
            'name': name,
            'selected_items': formatted_items,
        }

        # generate a response
        return render(request, template_name, context)

    ## GET lands down here: no return statements!

    # this is an OK solution: a graceful failure
    # return HttpResponse("Nope.")

    # if the client got here by making a GET on this URL, send back the form
    # use this template to produce the response

    # this is a "better solution", but shows the wrong URL
    # template_name = 'formdata/form.html'
    # return render(request, template_name)

    # this is the "best" solution: redirect to the correct URL
    return redirect("show_form")