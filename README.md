# eCommerce Website

Welcome to the **eCommerce Website** project. This is an online platform for buying and selling products. It includes both frontend and backend components, with functionality for user authentication, product browsing, and order management.

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Django URL Configuration](#django-url-configuration)

## Project Description

This is an eCommerce platform that allows users to browse, purchase, and manage orders for various products. The platform supports user registration and login functionality, allowing customers to access their account details, view their order history, and make purchases.

### Backend
The backend is built using **Django** (or another backend framework if you're using one) and handles data storage, user authentication, and product management.

### Frontend
The frontend of the platform is built with **HTML**, **CSS**, and **JavaScript** (or a JavaScript framework like React, if applicable).

## Technologies Used

- **Frontend**: 
  - HTML
  - CSS
  - JavaScript
  - React (or other frontend framework)
- **Backend**: 
  - Django (or other backend framework like Flask, Node.js, etc.)
- **Database**: 
  - SQLite (or PostgreSQL, MySQL, etc.)
- **Version Control**: 
  - Git

## Setup Instructions

To set up the project locally, follow the instructions below:

### 1. Clone the Repository

```bash
git clone https://github.com/Sahas2711/ecommerce-website.git
````

### 2. Install Dependencies

If you're using **Django** for the backend, make sure you have Python installed, then install the required Python packages:

```bash
cd ecommerce
pip install -r requirements.txt
```

For frontend dependencies, if you're using **npm** or **yarn** (for React or another JavaScript framework), run:

```bash
cd ecommerceweb
npm install  # or yarn install
```

### 3. Set Up the Database

For Django:

```bash
cd ecommerce
python manage.py migrate
```

### 4. Run the Development Server

For the backend (Django):

```bash
python manage.py runserver
```

For the frontend (if using React, for example):

```bash
cd ecommerceweb
npm start  # or yarn start
```

Visit `http://127.0.0.1:8000` for the backend and `http://localhost:3000` for the frontend (if using React or another frontend framework).

## Features

* **User Authentication**: Register, login, and manage accounts.
* **Product Catalog**: Browse through a wide range of products.
* **Order Management**: Users can add items to their cart and complete orders.
* **Admin Dashboard**: Admin can add, edit, and delete products.

## Contributing

We welcome contributions to the project. Please follow the steps below:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Submit a pull request.

Make sure to follow the code style and add relevant tests if applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Django URL Configuration

The following URL patterns are configured in the Django application:

### `urls.py` for the project

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerceweb/', include('ecommerceweb.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # This includes login, logout, etc.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### `urls.py` for the `ecommerceweb` app

```python
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  # Ensure the correct URL name
    path('product/create/', views.product_create, name='product_create'),
    path('product/update/<int:pk>/', views.product_edit, name='product_update'),
    path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('register/', views.register, name='register')
]
```

These URL patterns handle routes for product management, including listing products, creating, updating, and deleting products, as well as user registration and authentication views.


