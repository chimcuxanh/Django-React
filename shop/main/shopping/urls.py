from django.urls import path,include
from .views import *
from rest_framework import routers
# khi xu dung viewsets thi xu dung router
route = routers.DefaultRouter()
route.register("category",CategoryView,basename="category")

urlpatterns = [
    path('product/',ProductView.as_view(),name="product"),
    path('product/<int:id>/',ProductView.as_view(),name="product"),
    path("",include(route.urls))
]