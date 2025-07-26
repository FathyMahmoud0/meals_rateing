from django.shortcuts import render
from .models import Meal,Rate
from .serializer import MealSerializer,RateSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class MealViewSet(viewsets.ModelViewSet):
    
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    @action(detail = True,methods = ['post'])
    def meal_rate(self,request,pk):
        
        if 'stars' in request.data:
            meal = Meal.objects.get(id = pk)
            username = request.data['username']
            stars = request.data ['stars']
            user = User.objects.get(user = username)
            
            try:
                
                rating = Rate.objects.get(user = user.id ,meal = meal.id)
                rating.stars = stars
                rating.save()
                serializer = RateSerializer(rating,many = False)
                
                json = {
                    'message' : 'data is updated',
                    'data' : serializer.data
                     
                }
                return Response(json)
            except:
                rating = Rate.objects.create(user = user.id ,meal = meal.id,stars=stars)
                serializer = RateSerializer(rating,many = False)
                json = {
                    'message' : 'data is created',
                    'data' : serializer.data
                }
                return Response(json)
    
    
    
    
    
class RateViewSet(viewsets.ModelViewSet):
    
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ListView(generics.ListCreateAPIView):
    model= Meal
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    

    
    
    