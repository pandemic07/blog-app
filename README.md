# blog-app

# week4_project

# Django Blog Project

This is a Django project with two apps, 'blog' and 'users', designed to create a blog platform. It includes JWT (JSON Web Token) authentication for user login and logout, along with models for blog posts and comments.

## Table of Contents
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Authentication](#authentication)
- [Models](#models)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project is organized as follows:

- `blog`: The blog app.
- `users`: The users app.
- `jwt_utils`: Utility functions for JWT token generation.
- `manage.py`: Django management script.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following requirements installed:

- Python (3.x)
- Django (3.x)
- Django REST framework (optional, for API development)
- PyJWT (for JWT token generation)
- Other dependencies as needed

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/django-blog-project.git
   cd django-blog-project


    
    
Deployed GET, POST, PATCH and DELETE API's to handle all the cases required.



The first thing to do is to clone the repository:

        $ git clone https://github.com/pandemic07/week4_project.git
Create a virtual environment to install dependencies in and activate it:

         $ pip install virtualenv
         $ virtalenv env_name
         $ source path/bin/activate  like source /home/your_name/Environments/env_name/bin/activate
Then install the dependencies:

        (env)$ pip install -r requirements.txt
Once pip has finished downloading the dependencies:

        (env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000

Now you can see the link for Employee and Devices and perform CRUD operations
