from django.db import models
from django.contrib.auth.models import AbstractUser
#from time import timezone
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from django.core.mail import send_mail
#from django.utils.translation import ugettext_lazy as _


class Dog(models.Model):
    name = models.CharField(max_length=45)
    breed = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']


class MyUser(AbstractUser):
    phone = models.IntegerField()








"""
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):

        now = timezone.now()

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254, blank=True)
    second_name = models.CharField(max_length=254, blank=True)
    email = models.EmailField(blank=True, unique=True)
    address1 = models.CharField(max_length=254, blank=True)
    address2 = models.CharField(max_length=254, blank=True)
    area_code = models.CharField(max_length=254, blank=True)
    country_code = models.CharField(max_length=10, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'address1', 'address2', 'area_code', 'country_code']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s" % urlquote(self.email)

    def get_full_name(self):

        full_name = '%s %s' % (self.first_name, self.second_name)
        return full_name.strip()

    def get_short_name(self):

        return self.first_name

    def email_user(self, subject, message, from_email=None):

        send_mail(subject, message, from_email, [self.email])

"""