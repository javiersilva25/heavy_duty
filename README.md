# Heavy Duty Gym

Aplicación web desarrollada en Django para la gestión integral de gimnasios, con funciones de e-commercey panel administrativo.

---

Descripción

Heavy Duty Gym permite administrar usuarios, productos, servicios y ventas del gimnasio.
Incluye autenticación, carrito de compras, panel admin y gestión de clases o entrenamientos.

---

Características

Usuarios: registro, login y roles (usuario/admin).
E-commerce: productos, carrito, total automático e inventario.
Gimnasio: clases, entrenadores, nutrición y contacto.
Admin: control completo desde el panel de Django.

---

Tecnologías

| Componente    | Tecnología       |
| ------------- | ---------------- |
| Framework     | Django 5.0.6     |
| Base de datos | MySQL            |
| Lenguaje      | Python           |
| Plantillas    | Django Templates |
| Autenticación | Django Auth      |

---

Instalación

# Clonar proyecto
git clone https://github.com/tu-usuario/heavy-duty-gym.git
cd heavy-duty-gym

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar base de datos MySQL
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

---

Estructura

heavy-duty-gym/
├── heavy_duty_gym/   
├── main/             
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── urls.py
├── static/
└── manage.py

---

Modelos

**Item**

name, description, price, image, category

**Cart**

user, created_at, items[]

CartItem

cart, item, quantity

ContactMessage

name, email, message, created_at

---

Autenticación

@login_required: acceso a carrito y operaciones.
@user_passes_test`: acceso admin a gestión de productos.

---
