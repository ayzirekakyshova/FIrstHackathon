# from rest_framework.serializers import ModelSerializer
# from .models import Category,  Film 
# from .models import User, Comment 

# class CategorySerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = 'all'

#         def to_representation(self, instance):
#             rep = super().to_representation(instance)
#             rep['categories'] = instance.title
#             return rep

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = 'all'

# class FilmSerializer(ModelSerializer):
#     class Meta:
#         model = Film
#         fields = 'all'
#         def to_representation(self, instance):
#             rep = super().to_representation(instance)
#             rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data


# class CommentSerializer(ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = 'all'
        
#         def to_representation(self, instance):
#             rep = super().to_representation(instance)
#             rep['user'] = instance.user.email
#             rep['film'] = instance.movie.title
#             return rep

