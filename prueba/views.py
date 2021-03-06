import csv

import jwt
from django.http import HttpResponse
from rest_framework import renderers
from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from prueba.serializers import *


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
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


@api_view(['POST'])
def login(request, format=None):
    if request.method == 'POST':
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            try:
                usuario = usuarios.objects.get(email=request.data['email'])
            except:
                return Response(data='No se encuentra el usuario', status=status.HTTP_400_BAD_REQUEST)
            serializerU = UsuariosSerializer(usuario)
            if serializerU.data['contra'] == request.data['contra']:
                encoded = jwt.encode(serializerU.data, 'secret', algorithm='HS256')
                return Response(data={"mensaje": "Los datos son correctos.  bienvenido {}"
                                .format(serializer.data['email']), "id": encoded},
                                status=status.HTTP_200_OK)
        return Response(data='Los datos no son correctos', status=status.HTTP_400_BAD_REQUEST)


# -------------------class
@api_view(['GET'])
def imprimir(request, format=None):
    if request.method == 'GET':

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        clientes = clients.objects.raw('SELECT c.id,c.first_name,c.last_name,count(b.client_id_id) as cont '
                                       'from prueba_clients c left join prueba_bills b '
                                       'on c.id=b.client_id_id group by c.id')
        for cliente in clientes:
            writer.writerow([cliente.id, cliente.first_name, cliente.last_name, cliente.cont])

    return response


# -------------ViewSET-----------------------------
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


class RegistroViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        User = self.get_object()
        return Response(User.highlighted)

    def perform_create(self, serializer):
        serializer.save()


# ------------------CUSTOM TOKEN----------------------------

class LoginView(TokenObtainPairView):
    serializer_class = TokenSerializer
    permission_classes = [permissions.AllowAny]
