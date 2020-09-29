from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser,
PermissionsMixin,
BaseUserManager
)

class UserProfileManager(BaseUserManager):
    """ Manager for user profile """

    def create_user(self, email, name, password = None):
        """ Create a new sier profile """
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password) # to encrypt pass
        user.save()

        return user

    def create_superuser(self, email, password):
        """Create a superuser with the given details"""
        user = self.create_user(email, name, password)
        # self is automatically passed when you call a class fn

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user



# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ UserProfile Model """

    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve user full name"""
        return self.name

    def get_short_name(self):
        """ Retrieve user short name"""
        return self.name

    def __str__(self):
        """ Retrieve string representation of this model"""
        return self.email
