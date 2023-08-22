# blog-app

# week4_project

# Django Blog Project

This is a Django project with two apps, 'blog' and 'users', designed to create a blog platform. It includes JWT (JSON Web Token) authentication for user login and logout, along with models for blog posts and comments.

## Table of Contents
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Prerequisites](#prerequisites)
- [Authentication](#authentication)
- [Models](#models)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)

## Project Structure

The project is organized as follows:

- `blog`: The blog app.
- `users`: The users app.
- `jwt_utils`: Utility functions for JWT token generation.
- `requirements.txt`:Dependencies needed to be installed beforehand.
- `manage.py`: Django management script.

## Getting Started


### Installation

1. Clone the repository:

   The first thing to do is to clone the repository:

        $ git clone https://github.com/pandemic07/blog-app.git


2. Create a virtual environment to install dependencies in and activate it:

         $ pip install virtualenv
         $ virtalenv env_name
         $ source path/bin/activate   eg. source /home/your_name/Environments/env_name/bin/activate

### Prerequisites

Before you begin, ensure you have the following requirements installed:

        (env)$ pip install -r requirements.txt

3. Apply database migrations:

        $ python manage.py migrate



## Authentication

JWT (JSON Web Token) authentication is implemented for user login and logout. Tokens are generated using the pyjwt library.It doesn't uses any * __3rd party library__ *

## Models

  ### Blog Post
Title: The title of the blog post.
Content: The content of the blog post.
Author: The user who authored the blog post.
Created At: Timestamp indicating when the blog post was created.
Updated At: Timestamp indicating when the blog post was last updated.
  ### Comment
Content: The content of the comment.
Author: The user who authored the comment.
Created At: Timestamp indicating when the comment was created.
Updated At: Timestamp indicating when the comment was last updated.

## API Endpoints

- POST /api/register/: User login endpoint to obtain JWT token.
- POST /api/login/: User login endpoint to obtain JWT token.
- POST /api/logout/: User logout endpoint.
- POST /api/create-blog-post/: Create a new blog post.
- POST /api/posts/{post_id}/comments/: Create a comment on a blog post.
- GET /api/list-blog-posts/: List all blog posts.
- GET /api/comments/{post_id}: List all comments on a specific blog post.
- PATCH, PUT /api/posts/{post_id}/: Perform update on a blog post.



## Usage 

To start the development server, run:

    $ python manage.py runserver
    
Access the Django admin panel at http://localhost:8000/admin/ to manage users, blog posts, and comments.

Refer to the API documentation  for detailed API usage instructions.
  [API documentation](https://documenter.getpostman.com/view/26013106/2s9Y5U1Qv6)
