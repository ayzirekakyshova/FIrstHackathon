# from django.db import models

# class Category(models.Model):
#     title = models.CharField(max_length=70)
#     def __str__(self):
#         return self.title


# class Film(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     year = models.PositiveIntegerField()
#     poster = models.ImageField()
#     runtime = models.PositiveIntegerField()
#     cast = models.TextField()

# class Comment(models.Model):
#     user_id = models.IntegerChoices()
#     body = models.TextField
#     craeted_at = models.DateTimeField()
#     updated_at = models.DateTimeField()


#     @property
#     def average_rating(self):
#         ratings = self.ratings.all() 
#         values = []
#         for rating in ratings:
#             values.append(rating.value)
#         if values:
#             return sum(values) / len(values)
#         return 0

#     class Meta:
#         ordering = ['id']

#     def __str__(self):
#         return f'{self.body}'
