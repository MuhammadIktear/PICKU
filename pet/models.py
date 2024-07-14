from django.db import models
from django.contrib.auth.models import User
from .constants import SEX, SIZE, SPECIES, COLOR, BREED, STATUS

class UserBankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} - Balance: {self.balance}"

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES)
    breed = models.CharField(max_length=100, choices=BREED)
    color = models.CharField(max_length=20, choices=COLOR)
    size = models.CharField(max_length=20, choices=SIZE)
    sex = models.CharField(max_length=10, choices=SEX)
    image = models.ImageField(upload_to='pet_images/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rehoming_fee = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS)

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
