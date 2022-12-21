from django.db import models
from django.contrib.auth import get_user_model
from main.models import Film

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='film', on_delete=models.CASCADE)
    body = models.TextField
    craeted_at = models.DateTimeField()
    updated_at = models.DateTimeField()


    @property
    def average_rating(self):
        ratings = self.ratings.all() 
        values = []
        for rating in ratings:
            values.append(rating.value)
        if values:
            return sum(values) / len(values)
        return 0

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.body}'

class LikeFilm(models.Model):
    author = models.ForeignKey(User,related_name='film_likes', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, related_name= 'likes',on_delete=models.CASCADE)

class LikeComment(models.Model):
    author = models.ForeignKey(User,related_name='comment_likes', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,related_name='likes', on_delete=models.CASCADE)
    
class Rating(models.Model):
    author = models.IntegerField(User, related_name='film_rating', on_delete=models.CASCADE)
    film = models.IntegerField(User, related_name='film', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

class FavoriteFilm(models.Model):
    author = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    film= models.ForeignKey(Film, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} -> {self.film}'

