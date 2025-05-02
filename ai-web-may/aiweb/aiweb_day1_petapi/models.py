from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    allergy = models.CharField(max_length=100, blank=True, null=True)
    appearance = models.TextField()
    pet_image = models.ImageField(upload_to='pets/', blank=True, null=True)

    def __str__(self):
        return self.name




