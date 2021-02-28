from rest_framework import routers, serializers, viewsets
from rest_framework.viewsets import ModelViewSet
from produto.prod_serializers import ProdutosSerializer, CategoriaSerializer
from produto.models import Produto, Categoria

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutosSerializer

