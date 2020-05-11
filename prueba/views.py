from rest_framework import renderers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response

from prueba.models import clients, bills, products
from prueba.serializers import clientsSerializer, billsSerializer, productSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def detallesCliente(request, pk):
    try:
        cliente = clients.objects.get(pk=pk)
    except clients.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = clientsSerializer(cliente)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = clientsSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        serializer = clientsSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def detallesProducto(request, pk):
    try:
        producto = products.objects.get(pk=pk)
    except products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = productSerializer(producto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = productSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        serializer = productSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def detallesFacturas(request, pk):
    try:
        facturas = bills.objects.get(pk=pk)
    except bills.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = billsSerializer(facturas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = billsSerializer(facturas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        serializer = billsSerializer(facturas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        facturas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = clients.objects.all()
    serializer_class = clientsSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        cliente = self.get_object()
        return Response(cliente.highlighted)

    def perform_create(self, serializer):
        serializer.save()


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = products.objects.all()
    serializer_class = productSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        producto = self.get_object()
        return Response(producto.highlighted)

    def perform_create(self, serializer):
        serializer.save()


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = bills.objects.all()
    serializer_class = billsSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        factura = self.get_object()
        return Response(factura.highlighted)

    def perform_create(self, serializer):
        serializer.save()
