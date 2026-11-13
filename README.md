# E-Commerce Backend API

A backend-only E-Commerce REST API developed using Python, Django, Django REST Framework, and MySQL.

This project provides essential backend functionalities for an online shopping application, including user authentication, product management, category management, shopping cart, and order management.

## Project Type

Backend REST API Development

## Technologies Used

- Python
- Django
- Django REST Framework
- MySQL
- JWT Authentication
- Simple JWT
- Django Filter
- Postman
- Git & GitHub

## Features

### 1. User Authentication

- Custom User Model using AbstractUser.
- User Registration.
- User Login using Email and Password.
- JWT Access Token and Refresh Token.
- Refresh Token Rotation.
- User Logout with Token Blacklisting.
- Authentication using Bearer Token.
- Customer and Admin Roles.

### 2. Category Management

- Create Category.
- View All Categories.
- Retrieve Single Category.
- Update Category.
- Delete Category.
- Category Name and Description.
- Category Creation Date.

### 3. Product Management

- Create Product.
- View All Products.
- Retrieve Single Product.
- Update Product.
- Delete Product.
- Product and Category Relationship.
- Product Name and Description.
- Product Price.
- Product Stock Management.
- Product Availability.

### 4. Product Filtering and Searching

- Filter Products by Category.
- Filter Products by Price.
- Filter Products by Availability.
- Search Products by Name.
- Search Products by Description.
- Order Products by Price.
- Order Products by Name.
- Order Products by Creation Date.
- Pagination.

### 5. Shopping Cart Management

- Create User Cart.
- Add Products to Cart.
- View Cart Details.
- Add Product Quantity.
- Update Quantity when the Same Product is Added.
- Validate Product Availability.
- Validate Product Stock.
- Calculate Item Total.
- Calculate Cart Total.

### 6. Order Management

- Create Order from Cart.
- View Customer Orders.
- View Single Order Details.
- Validate Product Stock before Order Creation.
- Calculate Order Total.
- Create Order Items.
- Reduce Product Stock after Successful Order.
- Clear Cart after Order Creation.
- Cancel Eligible Orders.
- Restore Product Stock after Cancellation.
- Admin can View All Orders.
- Admin can Update Order Status.
- Customer and Admin Role-Based Access.

## Project Structure

```text
E-Commerce/
│
├── shopping_website/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── register_account/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── products/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── cart/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── ordermanagement/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── README.md
└── .gitignore
```

## API Endpoints

### Authentication APIs

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| POST   | `/register/`          | User Registration    |
| POST   | `/login/`             | User Login           |
| POST   | `/logout/`            | User Logout          |
| POST   | `/api/token/refresh/` | Refresh Access Token |

### Category APIs

| Method     | Endpoint                   | Description              |
| ---------- | -------------------------- | ------------------------ |
| GET, POST  | `/products/category/`      | List and Create Category |
| GET        | `/products/category/<id>/` | Retrieve Category        |
| PUT, PATCH | `/products/category/<id>/` | Update Category          |
| DELETE     | `/products/category/<id>/` | Delete Category          |

### Product APIs

| Method     | Endpoint                   | Description              |
| ---------- | -------------------------- | ------------------------ |
| GET, POST  | `/products/products/`      | List and Create Products |
| GET        | `/products/products/<id>/` | Retrieve Product         |
| PUT, PATCH | `/products/products/<id>/` | Update Product           |
| DELETE     | `/products/products/<id>/` | Delete Product           |

### Cart APIs

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| GET    | `/api/cart/`     | View Cart           |
| POST   | `/api/cart/add/` | Add Product to Cart |

### Order APIs

| Method | Endpoint                                | Description               |
| ------ | --------------------------------------- | ------------------------- |
| POST   | `/api/orders/create/`                   | Create Order              |
| GET    | `/api/orders/`                          | View Customer Orders      |
| GET    | `/api/orders/<id>/`                     | View Single Order         |
| POST   | `/api/orders/<id>/cancel/`              | Cancel Order              |
| GET    | `/api/orders/admin/orders/`             | Admin View All Orders     |
| PATCH  | `/api/orders/admin/orders/<id>/status/` | Admin Update Order Status |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

```bash
cd E-Commerce
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Required Packages

```bash
pip install Django==6.1.2
pip install djangorestframework==3.18.3
pip install djangorestframework-simplejwt==5.5.1
pip install django-filter==26.2
pip install mysqlclient==2.3.0
```

### 5. Create MySQL Database

Open MySQL Workbench and execute:

```sql
CREATE DATABASE shop_db;
```

### 6. Configure Database

Open:

```text
shopping_website/settings.py
```

Configure your MySQL database name, username, password, host, and port.

Do not upload your actual database password or Django SECRET_KEY to a public GitHub repository.

### 7. Run Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 8. Create Superuser

```bash
python manage.py createsuperuser
```

### 9. Run Development Server

```bash
python manage.py runserver
```

Server URL:

```text
http://127.0.0.1:8000/
```

## JWT Authentication

This project uses JSON Web Token (JWT) authentication through Simple JWT.

Authentication Flow:

1. User registers an account.
2. User logs in with email and password.
3. Server generates Access Token and Refresh Token.
4. Access Token is used to access protected APIs.
5. Refresh Token is used to obtain a new Access Token.
6. Logout blacklists the Refresh Token.

For Postman API testing:

- Select Authorization.
- Choose Bearer Token.
- Paste the Access Token.

## Product Filtering Examples

Filter by Category:

```text
/products/products/?category=1
```

Filter by Price:

```text
/products/products/?price=500
```

Filter by Availability:

```text
/products/products/?is_available=true
```

Search Products:

```text
/products/products/?search=mobile
```

Order by Price:

```text
/products/products/?ordering=price
```

Order by Highest Price:

```text
/products/products/?ordering=-price
```

Pagination:

```text
/products/products/?page=2
```

## Permissions and Access Control

- JWT Authentication.
- Authenticated User Access.
- Customer Role.
- Admin Role.
- Customer Order Access Restriction.
- Admin Order Management Access.
- Protected API Endpoints.

**Note:** The current registration view does not explicitly allow unauthenticated access, even though first-time user registration normally should be public. Configure `AllowAny` on that view before using public registration.

## Future Improvements

The following features can be added in future versions:

- Payment Gateway Integration.
- Payment Management.
- Product Image Upload.
- Wishlist Management.
- Product Reviews and Ratings.
- Cart Item Update and Remove APIs.
- Swagger API Documentation.
- Automated API Testing.
- Project Deployment.

## Learning Outcomes

Through this project, I gained practical knowledge of:

- Python Backend Development.
- Django and Django REST Framework.
- REST API Development.
- Custom User Model.
- JWT Authentication.
- Serializers and API Views.
- MySQL Database Integration.
- Model Relationships.
- CRUD Operations.
- Filtering, Searching, and Ordering.
- Pagination.
- Permissions and Role-Based Access.
- Shopping Cart Management.
- Order Management.
- Stock Validation.
- API Testing using Postman.

## Author

Surya N

Developed as a Backend Development Project using Python and Django REST Framework.
