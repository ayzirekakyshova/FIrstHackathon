from django.db import models

class Comment(models.Model):
    #user_id = models.IntegerChoices()
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
        return f'{self.course}'

