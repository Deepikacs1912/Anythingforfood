from dataclasses import fields
from rest_framework import serializers
from .models import Recipe,Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields=['name','type']
    def create(self,validated_data):
        return Ingredient.objects.create(**validated_data)

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['id','name', 'cooking_time', 'description', 'image', 'ingredients']
        depth=1
    def create(self,validated_data):
        print("create called")
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        return super().update(instance, validated_data)()

