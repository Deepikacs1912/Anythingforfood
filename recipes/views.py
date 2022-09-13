from http.client import HTTPResponse
from re import template
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe,Ingredient
from .serializers import RecipeSerializer,IngredientSerializer
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import Http404,HttpResponse
from django.shortcuts import redirect
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view

from . import serializers
# Create your views here.

class RecipeAPIView(APIView):
    renderer_classes=[TemplateHTMLRenderer]
    #to render below html on calling of this view
    template_name='recipes/all_recipes.html'
    def get(self,request,*args,**kwargs):
        
        #recipes=Recipe.objects.filter(id=request.user.id)
        recipes=Recipe.objects.all()
        # print(recipes)
        serializer=RecipeSerializer(recipes,many=True)
        return Response({'serializer': serializer},status=status.HTTP_200_OK)


# class CreateRecipeView(generics.GenericAPIView):
    # renderer_classes=[TemplateHTMLRenderer]
    # template_name='recipes/Newrecipe.html'
    # template_name='recipes/newform.html'
    # def get(self,request,*args,**kwargs):
    #     form = RecipeForm(request.POST)
    #     return Response({'form':form})
#     def get(self,request,*args,**kwargs):
#          return render(request,'recipes/newform.html')  

#     def post(self,request,*args, **kwargs):
#         # form = RecipeForm(request.POST)
        
#         # if form.is_valid():
            
#         serializer= RecipeSerializer.create(request.data)
#         print(serializer.is_valid())
#         # else:
#             # print("form not validated")
#         return redirect('recipes/all_recipes.html')
#         # s=form.is_valid()
#         # if s:
#         #     return Response({'data':s})
#         # return Response({'form':form})
#         # data=request.data.get()
#         # print(data)
#         # serializer= RecipeSerializer(data=data)
#         # if serializer.is_valid(raise_exception=True):
#         #     serializer.save()
#         #     print("okay")
#         #     return Response(data=serializer.data)
#         # else:
#         #     print("bye")
    
#         # return Response({"error":"Recipe not created successfully"})
@login_required(login_url='login')
@api_view(['POST','GET'])
def newrecipe(request):
    
    if request.method=='POST':
        print("view called")
        name=request.POST['name']
        cooking_time=request.POST['cooking_time']
        description=request.POST['description']
        image=request.POST['image']
        
        # ingredients=request.POST['ingredients']
        ingredients=request.POST.getlist('ingredients')
        
        print("display ingr")
        print(ingredients)
        recipe=Recipe.create(name=name,cooking_time=cooking_time,description=description,image=image,ingredients=ingredients)
        # print(recipe)
        # i=Ingredient.objects.filter(name=ingredients).values('name')
        #i=Ingredient.set(name=ingredients)

        #print(i)
        #recipe=Recipe.objects.create(name=name,cooking_time=cooking_time,description=description,image=image,ingredients=i)
#       serializer=RecipeSerializer.create(request,name,cooking_time)
        messages.success(request,'Data has been submitted')
#         # form=RecipeForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()             
#     #         return redirect('index')
#     # else:
#     #     form =RecipeForm()
#     # context = {'form': form}
    l=Ingredient.objects.values_list('name', flat=True)
    context={'list_ing':l}
    return render(request, 'recipes/newform.html',context)

class DetailRecipeAPIView(APIView):
    renderer_classes=[TemplateHTMLRenderer]
    template_name='recipes/detail_recipe.html'
    def get_object(self,pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404
    def get(self,request,pk,*args,**kwargs):
        recipe=self.get_object(pk)
        serializer=RecipeSerializer(recipe)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)

def searchrecipe(request):
    return render(request,'recipes/search.html')




