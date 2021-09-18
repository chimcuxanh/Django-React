from rest_framework import viewsets,generics,mixins
from .serializers import *
from .models import *
from rest_framework.response import Response


class ProductView(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer
    lookup_field = "id"

    def get(self,request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)


class CategoryView(viewsets.ViewSet):
    def list(self,request):
        query = Category.objects.all().order_by("id")
        serializers = CategorySerializer(query,many=True).data
        return Response(serializers)

    def retrieve(self,request,pk=None):
        query = Category.objects.get(id=pk)
        serializers = CategorySerializer(query)
        serializers_data = serializers.data
        data=[]
        category_product = Product.objects.filter(category_id=serializers_data['id'])
        category_product_serializers = ProductSerializer(category_product,many=True,context={'request': request})
        serializers_data["category_product"] = category_product_serializers.data
        data.append(serializers_data)
        return  Response(data)
