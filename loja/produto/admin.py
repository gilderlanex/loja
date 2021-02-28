from django.contrib import admin

# Register your models here.
from produto.models import Produto, Categoria

admin.site.register(Produto)
admin.site.register(Categoria)