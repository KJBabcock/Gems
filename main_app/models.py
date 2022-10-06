from django.db import models

# Create your models here.
class Gem(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    bio = models.TextField(max_length=1000)
    verified_gem = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Attribute(models.Model):

    title = models.CharField(max_length=150)
    value = models.IntegerField(default=0)
    gem = models.ForeignKey(Gem, on_delete=models.CASCADE, related_name="attributes")

    def __str__(self):
        return self.title

class Chain(models.Model):

    title = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    attributes = models.ManyToManyField(Attribute)

    def __str__(self):
        return self.title

