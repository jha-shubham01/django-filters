
from .models import Category, RandomList
from .serializers import CategorySerializer, RandomListSerializer


# DRF
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Category Model ViewSet.
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]


class RandomListViewSet(viewsets.ModelViewSet):
    """
    RandomList Model ViewSet.
    """

    serializer_class = RandomListSerializer
    queryset = RandomList.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'id', "name"]
    search_fields = ["name"]
    ordering_fields = '__all__'