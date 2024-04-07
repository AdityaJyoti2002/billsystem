
# Django Bill System 

This billing system is designed to streamline the invoicing process for on-counter transactions within a shopping mall. It enables cashiers to quickly generate and print invoices for purchases made by customers. The system ensures accuracy in including itemized lists of products, quantities, prices. With its intuitive interface, cashiers can efficiently process sales, providing customers with clear and professional invoices. 

![Logo](django.png)

# Installation

To install Django, you can follow these steps:

1. **Prerequisites**:
   - Ensure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. **Virtual Environment (optional but recommended)**:
   - It's recommended to create a virtual environment to isolate your Django project's dependencies. You can create a virtual environment using `venv` (built-in module in Python) or `virtualenv`.

   ```bash
   python -m venv myenv
   ```

   This command creates a virtual environment named `myenv` in the current directory.

3. **Activate Virtual Environment**:
   - Activate the virtual environment before installing Django.

   On Windows:
   ```bash
   myenv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   source myenv/bin/activate
   ```

4. **Install Django**:
   - Once your virtual environment is activated, you can install Django using pip (Python package manager). Run the following command:

   ```bash
   pip install django
   ```

   This command will download and install the latest stable version of Django and its dependencies.

5. **Verify Installation**:
   - After installation, you can verify Django installation by checking its version:

   ```bash
   django-admin --version
   ```

   This command should output the installed Django version.

That's it! You have successfully installed Django on your system. You can now start creating Django projects and applications.
To start using Django after installing it.

6. **Navigate to the Project Directory**:
   - After creating the project, navigate into the project directory:

     ```bash
     cd billsystem
     ```

3. **Run the Development Server**:
   - Start the Django development server by running the following command:

     ```bash
     python manage.py runserver
     ```

   - This will start the development server locally, and you'll see output similar to:
     ```
     Watching for file changes with StatReloader
     Performing system checks...

     System check identified no issues (0 silenced).
     April 07, 2024 - 12:00:00
     Django version x.x.x, using settings 'myproject.settings'
     Starting development server at http://127.0.0.1:8000/
     Quit the server with CONTROL-C.
     ```

