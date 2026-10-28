from django.shortcuts import render

# Create your views here.
from .models import Category, Photo

def portfolio_home(request):
    # Extragem toate categoriile și toate fotografiile din baza de date
    categories = Category.objects.all()
    photos = Photo.objects.all()
    
    # Le trimitem către template-ul HTML
    return render(request, 'core/index.html', {
        'categories': categories,
        'photos': photos
    })
