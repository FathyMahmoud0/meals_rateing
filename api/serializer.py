from rest_framework import serializers
from .models import Meal,Rate

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
        
class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'