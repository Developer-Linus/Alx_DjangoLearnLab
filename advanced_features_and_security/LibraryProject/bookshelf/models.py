from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} {self.publication_year}"


class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo, email, password=None):
        if not email:
            raise ValueError('Email field is required')
        user = self.model(
            email = self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, date_of_birth, profile_photo, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null = True, blank = True)
    profile_photo = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email