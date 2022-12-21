# from django.contrib import admin
# from .models import Category, Film
# from review.models import Comment, Rating


# class RatingInline(admin.TabularInline):
#     model = Rating

# class CommentInline(admin.TabularInline):
#     model = Comment

# class FilmAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category']
#     list_filter = ['category']
#     search_fields = ['title', 'description']
#     inlines = [CommentInline, RatingInline]

# admin.site.register(Category)
# admin.site.register(Film, FilmAdmin)


