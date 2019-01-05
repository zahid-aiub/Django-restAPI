"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from myApp import views
from rest_framework.routers import SimpleRouter
from myApp.views import ProductViewSet

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)

# urlpatterns = [
#     #path('api/', include('myApp.urls')),
#     # url(r'^test', views.get_permissions),
#     url('', include(router.urls)),
#     # url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
# ]
