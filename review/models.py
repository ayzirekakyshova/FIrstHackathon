from django.db import models

class Comment(models.Model):
    #user_id = models.IntegerChoices()
    body = models.TextField
    craeted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class favorutie(models.Model):
        user_id = models.IntegerField
        film_id = models.IntegerField

# @property
# def average_rating(self):
#     ratings = self.ratings.all() 
#     values = []
#     for rating in ratings:
#         values.append(rating.value)
#         if values:
#             return sum(values) / len(values)
#         return 0

# class Meta:
#         ordering = ['id']

class Rating(models.Model):
    user_id = models.IntegerField
    film_id = models.IntegerField
    value = models.enums
