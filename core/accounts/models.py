from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is used as the unique identifier
    instead of usernames for authentication.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a regular user with the given email and password.
        
        Args:
            email (str): The email address of the user.
            password (str): The password for the user.
            **extra_fields: Additional fields to include when creating the user.
        
        Raises:
            ValueError: If the email is not provided.

        Returns:
            User: The created user instance.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        
        A superuser has elevated privileges such as is_superuser and is_staff 
        set to True by default.
        
        Args:
            email (str): The email address of the superuser.
            password (str): The password for the superuser.
            **extra_fields: Additional fields to include when creating the superuser.
        
        Raises:
            ValueError: If is_staff or is_superuser are not set to True.
        
        Returns:
            User: The created superuser instance.
        """
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model for the application.
    
    This model uses an email address as the unique identifier for authentication
    and includes additional fields such as first_name and status flags.
    """
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True, help_text="The date and time when the user was created.")
    updated_date = models.DateTimeField(auto_now=True, help_text="The date and time when the user was last updated.")

    def __str__(self):
        """
        String representation of the user object, typically the email address.
        """
        return self.email
