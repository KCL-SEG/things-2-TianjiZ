from django.shortcuts import render
from .forms import ThingForm  # Import ThingForm from forms.py

def home(request):
    form = ThingForm()  # Create an instance of ThingForm
    return render(request, 'home.html', {'form': form})
