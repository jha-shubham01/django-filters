

from django.urls import path
from rest_framework.routers import DefaultRouter
from first import views


urlpatterns = []
router = DefaultRouter()
router.register("api/categories", views.CategoryViewSet, basename="categories")
router.register("api/random_list", views.RandomListViewSet, basename="random_list")
urlpatterns += router.urls