from rest_framework import generics, mixins
from .serializers import ProductSerializer
from .models import Product


class ProductView(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailView(generics.GenericAPIView,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)