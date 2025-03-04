from django.db import models

# Booking Table
class Booking (models.Model):
    name        = models.CharField(max_length=255)
    noOfGuests  = models.IntegerField()
    bookingDate = models.DateField()

# Menu Table
class MenuItem (models.Model):
    title       = models.CharField(max_length=255)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    inventory   = models.IntegerField()

    #add the following method in Menu class
    def __str__(self):
        return f'{self.title} : {str(self.price)}'