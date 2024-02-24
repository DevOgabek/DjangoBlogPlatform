# Django Blog Platform

The Django Blog Platform is a comprehensive web application designed for blogging purposes, built with Django framework. It empowers users with a range of functionalities including user authentication, profile management, and content creation.

## Live Demo

You can access a live demo of the Django Blog Platform by visiting [Demo Link](https://djangoblogplatform.pythonanywhere.com). Please note that this demo is for demonstration purposes only and may not reflect the latest changes or updates to the application.

Feel free to replace `[https://djangoblogplatform.pythonanywhere.com]` with the actual link to your live demo. If you don't have a live demo yet, you can host your Django application on platforms like Heroku or PythonAnywhere and provide the URL accordingly.

Make sure to keep the demo updated with the latest changes to your application for users to explore its functionalities effectively.

## Key Features

- **User Authentication**: Seamlessly register, login, and logout with secure authentication mechanisms.
- **Password Strength Validation**: Ensures password security by validating strength during registration.
- **User Profile Management**: View and update user profiles with personalized information.
- **Post Management**: Perform CRUD operations on posts including creation, reading, updating, and deletion.
- **Interactive Interface**: User-friendly error and success messages enhance user experience.

> [!TIP]
> Access the administrator profile with custom settings using the credentials: username `ogabekavazov` and password `123`.

## Requirements

- Python 3.x
- Django
- Pillow

## Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/DevOgabek/DjangoBlogPlatform.git
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Create Superuser:**

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the Server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the Application:**

    Visit `http://127.0.0.1:8000/` in your browser.

## Usage

1. **Sign Up:** Register by providing necessary details including username, email, first name, last name, and a strong password.
2. **Sign In:** Log in with your username and password.
3. **Create Post:** After logging in, create a new post by providing a title and content.
4. **View Post:** Click on a post title to read its content.
5. **Update Post:** Edit the title and content of your posts if you are the author.
6. **Delete Post:** Remove your posts if you are the author.
7. **View Profile:** Access your profile by clicking on your username. Update your personal information and bio.
8. **Sign Out:** Click on "Sign Out" to securely log out of your account.

## Credits

This application is developed by O'gabek.

## License

The project is licensed under the [MIT License](LICENSE).