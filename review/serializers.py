# from rest_framework.serializers import ModelSerializer

# from .models import Comment, Rating , FavoriteFilm


# class CommentSerializer(ModelSerializer):

#     class Meta:
#         model = Comment
#         exclude = ('author',)


#     def validate(self, attrs):
#         attrs =  super().validate(attrs)
#         request = self.context.get('request')
#         attrs['author'] = request.user

#         return attrs
        
    
# class RatingSerializer(ModelSerializer):

#     class Meta:
#         model = Rating
#         exclude = ('author',)


#     def validate(self, attrs):
#         attrs =  super().validate(attrs)
#         request = self.context.get('request')
#         attrs['author'] = request.user

#         return attrs


# class FavoritesFilmSerializer(ModelSerializer):

#     class Meta:
#         model = FavoriteFilm
#         exclude = ('author',)


#     def validate(self, attrs):
#         attrs =  super().validate(attrs)
#         request = self.context.get('request')
#         attrs['author'] = request.user

#         return attrs