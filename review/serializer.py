from rest_framework.serializers import ModelSerializer

from .models import Comment,favorutie, Rating


class CommentCourseSerializer(ModelSerializer):

    class Meta:
        model = Comment
        exclude = ('author',)


    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user

        return attrs


class RatingCinemaSerializer(ModelSerializer):

    class Meta:
        model = Rating
        exclude = ('author',)


    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user

        return attrs


class FavoritesCinemaSerializer(ModelSerializer):

    class Meta:
        model = favorutie
        exclude = ('author',)


    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user

        return attrs