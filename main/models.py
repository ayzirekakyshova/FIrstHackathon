from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=70)
    def __str__(self):
        return self.title

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)        


class Film(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    year = models.PositiveIntegerField()
    poster = models.ImageField()
    runtime = models.PositiveIntegerField()
    cast = models.TextField()

@property
def average_rating(self):
        Film = Film.objects.filter(course=self)
        values = []
        for poster in Film:
            values.append(Film.average_rating)
        if values:
            return sum(values) / len(values)
        return 0
    
def __str__(self) -> str:
        return f'{self.author} -> {self.title}'
