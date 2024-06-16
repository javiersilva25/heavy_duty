from django.contrib import admin
from .models import Item, Cart, CartItem

# Registrar el modelo Item en el sitio de administración
admin.site.register(Item)

# Opcionalmente, también puedes registrar los otros modelos si es necesario
admin.site.register(Cart)
admin.site.register(CartItem)
