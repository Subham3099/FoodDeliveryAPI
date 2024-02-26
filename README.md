
# Food Delivery API
Overview
This project is a Food Delivery API developed using Django, aimed at helping organizations manage their logistics operations efficiently. It includes functionalities for calculating pricing based on various parameters like zone, distance, and item type, as well as managing organizations, items, and pricing information.

## Features
Calculate Pricing: Calculate pricing based on zone, distance, and item type.
Organization Management: CRUD operations for managing organizations.
Item Management: CRUD operations for managing items.
Pricing Management: CRUD operations for managing pricing information.

## Installation
Prerequisites:

Python installed on your machine.
Django framework installed (pip install django).

Clone the Repository:
```bash
git clone <repository_url>
```

Navigate to Project Directory:
```bash
cd <project_directory>
```

Install Requirements:
```bash
pip install -r requirements.txt
```
Run Migrations:

```bash
python manage.py migrate
```

Create Superuser (Optional):

```bash
python manage.py createsuperuser
```

Run Development Server:

```bash
python manage.py runserver
```

## Usage
Access Admin Panel:

Navigate to http://localhost:8000/admin/
Log in with the superuser credentials created earlier.

## API Endpoints:

Calculate View: [http://localhost:8000/calculate/]
Organization List/Create: [http://localhost:8000/organization/list/] & [http://localhost:8000/organization/create/]
Item List/Create: [http://localhost:8000/item/list/] & [http://localhost:8000/item/create/]
Pricing List/Create: [http://localhost:8000/pricing/list/] & [http://localhost:8000/pricing/create/]

## API Documentation
Detailed API documentation can be found in the source code.

## Test Suite
Comprehensive test suite covering major functionalities and edge cases.
