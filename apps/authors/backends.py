from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        User = get_user_model()
        try:
            if username:
                user = User.objects.get(username=username)
            else:
                user = User.objects.get(email=email)

        except User.DoesNotExist:
            return None

        else:
            if user.check_password(password):
                return user
        return None
