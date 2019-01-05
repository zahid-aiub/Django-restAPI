from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import BasePermission
from myApp.models import Product, Category
from myApp.serializer import ProductSerializer, CategorySerializer
# Create your views here.

class AuthenticatedUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AuthenticatedUserPermission, )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AuthenticatedUserPermission, )