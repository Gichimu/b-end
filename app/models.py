from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=25)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    about_me = models.TextField()

    def __str__(self):
        return self.fname

class Property(models.Model):
    title = models.CharField(max_length=50)
    transaction_type = models.CharField(max_length=5)
    price = models.PositiveIntegerField(default=0)
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=50)
    description = models.TextField()
    bookmarked = models.BooleanField(default=False)

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



