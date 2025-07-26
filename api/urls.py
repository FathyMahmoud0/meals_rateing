from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# from rest_framework import router


router = DefaultRouter()
router.register('meal', views.MealViewSet)
router.register('rate', views.RateViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('',include(router.urls)),
    path('list/',views.ListView.as_view())
]
