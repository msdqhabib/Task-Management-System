# Task Management System

Task Management System is a web application designed to streamline task management and collaboration within teams or organizations. Its primary purpose is to provide users with a centralized platform for creating, assigning, tracking, and completing tasks efficiently.

## Technologies Used

- Python
- Django
- PostgreSQL
- HTML/CSS
- JavaScript
- Bootstrap
- AWS

## Apps and Features

### Authentication App

**Purpose:** Provides user authentication and authorization functionalities.

**Features:**

- User registration
- User login
- Logout
- User profile management

### Core App

**Purpose:** Contains core functionalities and utilities used across the project.

**Features:**

- Common Utilities
- Base templates

### Tasks App

**Purpose:** Manages tasks and to-dos within the application.

**Features:**

- CRUD operations for tasks
- Assigning tasks to users
- Filtering tasks based on status, priority, etc.
- Sorting Tasks

### Teams App

**Purpose:** Handles team management and collaboration features.

**Features:**

- Creating, updating, and deleting teams
- Adding/removing members to/from teams
- Team-specific tasks and discussions

## Running the Project

1. **Installing Dependencies:**

   - Ensure Python and virtualenv are installed on your system.
   - Install virtualenv using the following command:
     ```
     python -m pip install virtualenv
     ```

2. **Creating and Activating Virtual Environment:**

   - Create a virtual environment named project_env using the command:
     ```
     python -m venv project_env
     ```
   - Activate the virtual environment based on your operating system:
     - Windows: `project_env\Scripts\activate`
     - macOS/Linux: `source project_env/bin/activate`

3. **Installing Dependencies:**

   - Navigate to the project directory containing requirements.txt.
   - Install all dependencies using the command:
     ```
     pip install -r requirements.txt
     ```

4. **Running the Migrations:**

   - Run migrations and migrate.
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Run Development Server:**
   ```
    python manage.py runserver
   ```

## Notes

- This documentation provides a basic overview and setup guide. For more detailed instructions or troubleshooting, refer to the Django documentation or reach out to the project maintainers.
- Feel free to customize the application further according to your specific requirements and preferences.
- Contributions, bug reports, and feedback are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on GitHub.
