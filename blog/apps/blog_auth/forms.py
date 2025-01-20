from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm (UserCreationForm):
    model= User
    fields=(
        'Username',
        'email',
        'password1',
        'password2',
    )