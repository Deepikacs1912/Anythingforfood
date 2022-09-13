
from posixpath import basename
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('all/',views.RecipeAPIView.as_view(),name='all-recipe'),
    path('<int:pk>/',views.DetailRecipeAPIView.as_view(),name='detail-recipe'),
    # 
    # path('newrecipe/',views.CreateRecipeView.as_view(),name='new-recipe'),
    path('newrecipe/',views.newrecipe,name='new-recipe'),
    path('searchrecipe/',views.searchrecipe,name='search-recipe'),

]

