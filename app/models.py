from django.db import models

class Agent(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
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

class Company(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title
