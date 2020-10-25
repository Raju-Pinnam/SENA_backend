from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    SEX = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    username = models.CharField(max_length=254)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    sena_id = models.CharField(max_length=24)
    slug = models.SlugField(max_length=254, blank=True, unique=True)
    phone = models.CharField(max_length=24)
    gender = models.CharField(choices=SEX, max_length=10)
    current_location = models.TextField()
    home_location = models.TextField()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/profile_images/', blank=True)
    slug = models.SlugField(max_length=254, blank=True, unique=True)
    total_experience = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.user


class Job(models.Model):
    EMPLOYMENT_TYPE = (
        ('internship', 'Internship'),
        ('fulltime', 'Full Time'),
        ('parttime', 'Part Time')
    )
    company = models.CharField(max_length=254)
    employment_type = models.CharField(choices=EMPLOYMENT_TYPE, max_length=10)
    user_profile = models.ForeignKey(UserProfile, related_name='past_jobs', on_delete=models.CASCADE)
    job_start = models.DateField()
    job_end = models.DateField()
    designation = models.CharField(max_length=128)
    slug = models.SlugField(max_length=254)
    job_profile = models.CharField(max_length=254)

    def __str__(self):
        return self.user_profile
