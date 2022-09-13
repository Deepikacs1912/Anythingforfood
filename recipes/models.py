from django.db import models
from PIL import Image
# Create your models here.
class Ingredient(models.Model):
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=30,default="NA")
    def __str__(self):
        return self.name
    @classmethod
    def create(cls,name,category="NA"):
        print("ingredient create caslled")
        new_ing=cls(name=name,category=category)
        new_ing.save()
        print(type(new_ing))
        return new_ing

class Recipe(models.Model):
    name=models.CharField(max_length=30)
    cooking_time=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(default=None,upload_to="recipe_images")
    ingredients=models.ManyToManyField(Ingredient,default=None)
    def __str__(self):
        return self.name
    @classmethod
    #customizing create method to solve many to many issue of ingredient-recipe
    def create(cls,**kwargs):
        r=cls(name=kwargs['name'],cooking_time=kwargs['cooking_time'],description=kwargs['description'],image=kwargs['image'])
        r.save()
        i=kwargs['ingredients']
        ing=Ingredient.objects.filter(name=i)
        if(not ing):
            I=Ingredient.create(i)
            r.ingredients.add(I)
        else:
            r.ingredients.set(ing)
        
        return r
    # def save(self,*args,**kwargs):
    #     super().save()
    #     img=Image.open(self.image.path)
    #     if img.height>200 or img.width>200:
    #         new_img=(200,200)
    #         img.thumbnail(new_img)
    #         img.save(self.image.path)

