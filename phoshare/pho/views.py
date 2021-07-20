from django.shortcuts import render
from .models import Category, Location, Image

def index(request):
    images=Image.objects.all()
    locations=Location.get_locations()
    return render(request, 'index.html', {'images':images[::-1], 'locations':locations})

def search_category(request):
    if 'imagesearch' in request.GET and request.GET['imagesearch']:
        category = request.GET.get('imagesearch')
        searched_images=Image.search_by_category(category)
        message=f'{category}'
        print(searched_images)
        return render(request, 'search_results.html', {'message':message, 'images':searched_images})
    else:
        message='Search any image?'
        return render(request, 'search_results.html', {'message':message})

def image_location(request, location):
    images=Image.filter_by_location(location)
    return render(request, 'location.html', {'location_images': images})