# Django Two Factor Authentication

Django two-step verification app. Personal project to increase the security of user login in Django projects. The second verification is a 6-digit numeric code sent to the user after standard authentication.

When a new user (`AUTH_USER_MODEL`) is created, the token is created with a one-to-one key. **This authentication does not work for the admin page.**

## Installation

```bash
pip install git+https://github.com/Pkfilho95/Django-Two-Factor-Authentication.git
```

## Configuration

1. Define your `AUTH_USER_MODEL` in `settings.py`. By default, the `User` model is the Django authentication model.

2. Add `two_factor_auth` to the `INSTALLED_APPS` list in the `settings.py` file of your Django project:

```python
INSTALLED_APPS = [
    ...
    'two_factor_auth',
    ...
]
```

3. In the `urls.py` file, import the app views:

```python
from two_factor_auth.views import AuthView, TwoAuthView
```

4. Next, add two new urls using the `path` function:

```python
urlpatterns = [
    ...
    path('', AuthView.as_view(), name='Login'),
    path('verify/', TwoAuthView.as_view(), name='Verify'),
    ...
]
```
If you want a specific app to control these urls, open its `urls.py` file.

## AuthView

AuthView has three default variables defined.

1. `template_name [default = 'auth.html']`: is the html file that will be rendered when entering the url and will contain the login form. The names of the inputs need to be `username` and `password`.

2. `form_class [default = AuthenticationForm]`: is the class responsible for validating the form.

3. `success_url [default = '/verify/']`: is where you will be redirected after validation is correct.

⚠️ **Atention** ⚠️

1. You can change these parameters inside the `path`:

```python
urlpatterns = [
    ...
    path('', AuthView.as_view(template_name='login.html'), name='Login'),
    ...
]
```

2. `AuthenticationForm` is the default Django form class for authenticating users.

## TwoAuthView

TwoAuthView has three default variables defined.

1. `template_name [default = 'two_auth.html']`: is the html file that will be rendered when entering the url and will contain the token verification  form. The name of the input need to be `token`.

2. `form_class [default = TwoFactorAuthForm]`: is the class responsible for validating the form. Is a `forms.ModelForm` class, containing only the Meta class.

3. `success_url [default = settings.LOGIN_REDIRECT_URL]`: is where you will be redirected after validation is correct. Add `LOGIN_REDIRECT_URL` in the `settings.py` file of your Django project.

⚠️ **Atention** ⚠️

1. You can change these parameters inside the `path`:

```python
urlpatterns = [
    ...
    path('verify/', TwoAuthView.as_view(template_name='verify.html'), name='Verify'),
    ...
]
```

## Migrations

Before running your Django application, you need to ensure that the database migrations are applied correctly.

1. In the root directory of the project, run the following command to create the migrations:

```bash
py manage.py makemigrations two_factor_auth
```

2. Then run the following command to apply the migrations to the database::

```bash
py manage.py migrate two_factor_auth
```
