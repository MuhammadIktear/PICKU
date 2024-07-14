from django.db import models
from django.contrib.auth.models import User
from filter.models import Species,Breed,Color,Size,Sex,Status

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pet_images/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rehoming_fee = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    details = models.TextField()

    def __str__(self):
        return self.name

class Adopt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    adopt_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name}"
