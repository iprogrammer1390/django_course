from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(verbose_name="the persons first name", max_length=30)
    last_name = models.CharField(verbose_name="the persons last name", max_length=30)
    cars = models.ManyToManyField('Car', verbose_name="the user's cars")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted'),
)
class Website(models.Model):
    name = models.CharField( max_length=50)
    url = models.URLField()
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.rating}'

class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)

