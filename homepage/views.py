from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def home(request):
    return render(request, 'index.html', {})

def price(request):
    return render(request, 'pricing.html', {})

# views.py

from django.shortcuts import render, redirect
from .forms import ThreeDPrintOrderForm, LaserEngravingOrderForm

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ThreeDPrintOrderForm

@login_required
def three_d_print_order(request):
    if request.method == 'POST':
        form = ThreeDPrintOrderForm(request.POST, request.FILES)
        if form.is_valid():
            three_d_order = form.save(commit=False)
            three_d_order.user = request.user  # Set the user
            three_d_order.save()
            return redirect('/')  # Adjust the redirection as necessary
    else:
        form = ThreeDPrintOrderForm()
    return render(request, '3dprint.html', {'form': form})


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LaserEngravingOrderForm

@login_required
def laser_engraving_order(request):
    if request.method == 'POST':
        form = LaserEngravingOrderForm(request.POST, request.FILES)
        if form.is_valid():
            laser_order = form.save(commit=False)
            laser_order.user = request.user  # Set the user
            laser_order.save()
            return redirect('/')  # Adjust the redirection as necessary
    else:
        form = LaserEngravingOrderForm()
    return render(request, 'laser.html', {'form': form})
