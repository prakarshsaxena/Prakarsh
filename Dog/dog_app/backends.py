#from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    
    def authenticate(self, request, username=None, password=None):
        try:
            User = get_user_model()
            user = User.objects.get(email=username)

        except User.MultipleObjectsReturned:
            user = User.objects.filter(email=username).order_by('id').first()
        except User.DoesNotExist:
            return None
        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            User = get_user_model()
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class MobileBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None):
        try:
            User = get_user_model()
            user = User.objects.get(phone=username)

        except User.MultipleObjectsReturned:
            user = User.objects.filter(phone=username).order_by('id').first()
        except User.DoesNotExist:
            return None
        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            User = get_user_model()
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

"""
class CustomUserAuth(object):

    def authenticate(self, username=None, password=None):
        try:
            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except CustomUser.DoesNotExist:
            return None
"""