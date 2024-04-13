# Django Ninja Project

This guide details the steps to set up and run the Django application with Django Ninja using Poetry for dependency management. Follow these instructions to get the project up and running on your local machine.

## Prerequisites

- **Python 3.11**: Ensure Python 3.11 is installed and set as the global version in your development environment. We recommend using `pyenv` for managing Python versions.
- **Poetry**: This project uses Poetry for dependency management. If you haven't installed Poetry yet, follow the instructions on Poetry's official documentation.

## Setup Instructions

after clone the project

### 1. Setting Up Python 3.11 with `pyenv`

If you haven't installed Python 3.11, use `pyenv` to install and set it as your global Python version:

```bash
pyenv install 3.11.8 # Skip if already installed
pyenv local 3.11.8
```

### 2. Install Poetry

Install Poetry globally using pip:

```bash
pip install poetry
```

### 3. Activate the Poetry Environment

Navigate to the project directory and activate the Poetry environment:

```bash
poetry shell
```

This command will either create a new virtual environment for the project or activate an existing one.

### 4. Install Project Dependencies

With the virtual environment activated, install the project dependencies:

```bash
poetry install
```

### 5. Running the Development Server

Once the dependencies are installed, you can start the Django development server by running:

```bash
python manage.py runserver
```

## Accessing the Application

After the server starts, you can access the main application by visiting [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser. The Django Ninja API can be interacted with at [http://127.0.0.1:8000/api/hello](http://127.0.0.1:8000/api/hello), which will display a "Hello, world!" message.

## Additional Information

- **Poetry Commands**: For more commands and options available with Poetry, refer to the [Poetry documentation](https://python-poetry.org/docs/).
- **Django Commands**: For a list of common Django management commands, visit the [Django documentation](https://docs.djangoproject.com/en/3.2/ref/django-admin/).

## Troubleshooting

If you encounter any issues during setup or running the project, ensure that:
- You are using Python 3.11.8 as specified.
- You have activated the Poetry shell before running `poetry install` and `python manage.py runserver`.
- All dependencies were successfully installed without errors.

## VS Code Settings

on `.vscode/settings.json`

```json
{
  "editor.defaultFormatter": "ms-python.black-formatter",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

## Creating Django Applications

To create a new Django application, follow the steps below. Please ensure to replace `app_name` with the actual name of your application.

1. **Create a new directory**: Navigate to the `apps` folder and create a new directory. The name of this directory should be the same as your `app_name`.

2. **Initialize the Django application**: Run the following command in your terminal:

```bash
django-admin startapp app_name apps/app_name
```

## Configuring Django Applications

In your Django application, you will need to set up a configuration class in the `apps.py` file. Here's an example of how to do this:

```python
from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.app_name"
```
The name of this should be the same as your `app_name`.

## In settings.py

INSTALLED_APPS

```python
INSTALLED_APPS = [
    ...
    "apps.app_name",
]
```
