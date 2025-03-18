# Task 1 - Setting Up a new Django Project
### Step 1: Project Setup
- Ensure that `django` is installed in the virtual environment or globally in the stystem.
- Navigate to the directory you want to host the project.
- Create a new django project called `django_blog` using the command:
```bash
django-admin startproject django_blog
```
- Navigate to your project directory and create a new Django app called `blog`. The command to use is 
```bash
python manage.py startapp blog
```
- Register the new app `blog` in the `INSTALLED_APPS` in the `django_blog/settings.py`.
```bash
INSTALLED_APPS = [
    #..........
    'blog'
]
```
### Step 2 : Database Configuration
- Configured my MySQL in the project.
- Install `python-decouple` to use for environment variables
```bash
pip install python-decouple
``` 
- create a `.env` file in the project directory and specify the varialbes:
```bash
DB_NAME=database_name
DB_USER=your_database_username
DB_PASSWORD=password
DB_HOST=host
DB_PORT=port_number
```
-import `decouple` and `os` packages in `django_blog/settings.py` using the commands:
```bash
import os
```
```bash
from decouple import Config
```
- Create an instance of `Config` to load environment variables using:
```bash
config = Config(repository=os.environ)
```
- In the `DATABASES` in the `django_blog/settings.py`, configure the settings of the database you want to use as:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
```
### Step 3 - Define Blog Model
- Define a `Post` model in `blog/models.py` with the following fields:
```bash
title: models.CharField(max_length=200)
content: models.TextField()
published_date: models.DateTimeField(auto_now_add=True)
author: models.ForeignKey to Django’s User model, with a relation to handle multiple posts by a single author.
```
- Run migrations to create the model in the database:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
### Step 4 - Set Up Static files
- **HTML**: Place the `base.html` file in the `blog/templates/blog/` directory.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Django Blog{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{% url 'home' %}">Home</a></li>
                <li><a href="{% url 'posts' %}">Blog Posts</a></li>
                <li><a href="{% url 'login' %}">Login</a></li>
                <li><a href="{% url 'register' %}">Register</a></li>
            </ul>
        </nav>
    </header>

    <div class="content">
        {% block content %}
        <!-- Page-specific content goes here -->
        {% endblock %}
    </div>

    <footer>
        <p>&copy; 2024 Django Blog</p>
    </footer>

    <script src="{% static 'js/scripts.js' %}"></script>
</body>
</html>
```
- **CSS**: Place the `styles.css` file in the `blog/static/css/` directory.
```css
/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333;
}

header {
    background-color: #333;
    padding: 10px;
    text-align: center;
}

header nav ul {
    list-style-type: none;
}

header nav ul li {
    display: inline;
    margin: 0 15px;
}

header nav ul li a {
    color: white;
    text-decoration: none;
    font-size: 18px;
}

.content {
    margin: 20px;
}

footer {
    text-align: center;
    margin-top: 50px;
    padding: 10px;
    background-color: #333;
    color: white;
}
```
- **JavaScript**: Place the `scripts.js` file in the `blog/static/js/` directory.
```javascript
// Basic example script to demonstrate dynamic behavior
document.addEventListener('DOMContentLoaded', function() {
    console.log('Blog page loaded');
});
```

- configure your project to properly serve static files in `django_blog/settings.py`:
```bash
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
    },
]
```
