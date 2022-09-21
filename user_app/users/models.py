from tabnanny import verbose
from django.db import models
from datetime import datetime
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

    def was_relesed_last_week(self):
        if self.release_date < datetime.date(2019, 3, 3):
            return "Released before last week"
        else:
            return "Released this week"
    
    @property
    def get_full_name(self):
        return f"This is my website's full name: {self.name}"
    
    def get_absolute_url(self):
        return f"/websites/{self.id}"
    
    def save(self, *args, **kwargs):
        print("We are doing something else here...")
        super().save(*args, **kwargs)
    

    # class Meta:
    #     ordering = ['rating']
    #     db_table = 'website_custom_table_name'
    #     verbose_name = 'the website'
    #     verbose_name_plural = 'the websites'

    def __str__(self):
        return f'{self.name} {self.rating}'

class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)

