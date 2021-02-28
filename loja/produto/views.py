from django.core import serializers
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from produto.models import Produto


def index(request):
    produto = serializers.serialize("json", Produto.objects.all())
    return HttpResponse(produto)

