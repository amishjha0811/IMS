# Inventory Management System (IMS)

A desktop-based Inventory Management System built with Python and Tkinter. This application helps manage employees, suppliers, product categories, products, billing, and sales for a retail or wholesale business.

## Features

- **Login System**: Secure login for employees and admins, with password reset via email.
- **Employee Management**: Add, update, delete, and search employee records.
- **Supplier Management**: Manage supplier details and invoices.
- **Category Management**: Add and delete product categories.
- **Product Management**: Manage products, including category and supplier assignment.
- **Billing**: Create and print customer bills, manage a shopping cart, and update inventory.
- **Sales Tracking**: View and search past sales/bills.
- **Dashboards**: Separate dashboards for admin and employees, showing statistics and navigation menus.

## Directory Structure

- `main.py` / `DashBoard.py`: Main entry points for the application.
- `login.py`: Handles user authentication and password reset.
- `employee.py`, `supplier.py`, `category.py`, `product.py`, `sales.py`: CRUD operations for each entity.
- `billing.py`: Handles billing and cart management.
- `create_db.py`: Initializes the SQLite database and tables.
- `bill/`: Stores generated bill text files.
- `image/`: Contains all image assets used in the UI.
- `email_pass.py`: Stores email credentials for password reset (should be kept secure).
- `launcher.vbs`: Windows script to launch the application with a double-click.

## Database

The application uses SQLite (`ims.db`). The database is initialized with the following tables:
- `employee`: Stores employee details.
- `supplier`: Stores supplier details.
- `category`: Stores product categories.
- `product`: Stores product information.

## How to Run

1. **Install Requirements:**
   - Python 3.x
   - [Pillow](https://pypi.org/project/Pillow/) (for image handling)
   - Install Pillow with:
     ```bash
     pip install pillow
     ```
2. **Initialize the Database:**
   - Run `create_db.py` once to create the necessary tables:
     ```bash
     python create_db.py
     ```
3. **Start the Application:**
   - Double-click `launcher.vbs` (on Windows) or run:
     ```bash
     python login.py
     ```
   - Log in as an admin or employee.

## Security Note

- The file `email_pass.py` contains plain text email credentials. For production, use environment variables or a secure vault.

## Credits

- Developed by Aj & Cj. 
