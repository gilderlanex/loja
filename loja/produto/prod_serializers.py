from rest_framework.serializers import ModelSerializer
from produto.models import Produto, Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','desc']

class ProdutosSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','desc_produto','preco', 'modelo_produto','categoria']

