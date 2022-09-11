from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    full_address = models.CharField(max_length=50, blank=False, null=False)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username 


class Service(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title