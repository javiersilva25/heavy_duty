from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm, ContactForm
from .models import Item, Cart, CartItem
from django.contrib.auth.decorators import user_passes_test
from .models import Item
from .forms import ItemForm
from django.core.mail import send_mail
from django.conf import settings
import ssl

def home(request):
    item_count = 0
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        item_count = cart.cartitem_set.count()
    items = Item.objects.all()
    
    services = {
        'entrenamiento_personalizado': Item.objects.get(id=1),
        'nutricion_y_dieta': Item.objects.get(id=2),
        'clases_en_grupo': Item.objects.get(id=3)
    }
    
    return render(request, 'main/index.html', {'items': items, 'item_count': item_count, 'services': services})

def admin_check(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(admin_check)
def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio o a donde prefieras
    else:
        form = ItemForm(instance=item)
    return render(request, 'main/update_item.html', {'form': form, 'item': item})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    item_count = cart.cartitem_set.count()
    return render(request, 'main/cart.html', {'cart': cart, 'item_count': item_count})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu mensaje ha sido enviado con éxito.')
            return redirect('contact')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def nosotros(request):
    return render(request, 'main/nosotros.html')

