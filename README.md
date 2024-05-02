# Tbc CRUD

This project implements CRUD (Create, Read, Update, Delete) operations for managing products using Django Rest Framework.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/natia02/TbcCRUD.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run migrations:
   ```bash
   python manage.py migrate
   ```

2. Start the development server:
   ```bash
   python manage.py runserver
   ```

3. Access the endpoints:
   - Product Create endpoint: `/product/create/`
   - Detailed info endpoint: `/product/<product_id>/`
   - Product listing: `/products/`
   - Endpoint to delete the product: `/product/<product_id>/delete/`
   - Change endpoint (update): `/product/<product_id>/update/`

## API Endpoints

- **Product Create:** `POST /product/create/`
- **Category Create:** `POST /category/create`
- **Detailed info:** `GET /product/<product_id>/`
- **Product Listing:** `GET /products/`
- **Delete Product:** `DELETE /product/<product_id>/delete/`
- **Update Product:** `PATCH /product/<product_id>/update/`
