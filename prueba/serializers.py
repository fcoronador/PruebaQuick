from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from prueba.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User


class clientsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    document = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=30)
    contra = serializers.CharField(max_length=200)
    class Meta:
        model = clients
        fields = ['id','document','first_name','last_name',
                  'email','contra']

    def create(self, validated_data):
        return clients.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.document = validated_data.get('document', instance.document)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.contra = validated_data.get('contra', instance.contra)
        instance.save()
        return instance


class productSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=200)
    attribute4 = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.attribute4 = validated_data.get('attribute4', instance.attribute4)
        instance.save()
        return instance

    class Meta:
        model = products
        fields = ['id','name','description','attribute4']

class billsSerializer(serializers.ModelSerializer):
    client_id=clients.objects.get
    company_name = serializers.CharField(max_length=30)
    nit = serializers.IntegerField()
    code = serializers.IntegerField()

    def create(self, validated_data):
        return bills.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.nit = validated_data.get('nit', instance.nit)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance
    class Meta:
        model = bills
        fields = ['client_id','nit','code','company_name']

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password','email',
                  "last_login", "is_superuser",
                  "username" , "first_name", "is_staff",
                  "is_active" , "date_joined" ,"last_name"]


    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']))
        user.set_password(validated_data['password'])
        user.save()
        return user

class bills_productsSerializer(serializers.ModelSerializer):
    bill_id = bills.objects.get
    product_id = products.objects.get
    class Meta:
        model = bills_products

#-----------------------------------------------------


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, usuarios):
        token = super().get_token(usuarios)

        # Add custom claims
        token['email'] = usuarios.email
        # ...
        return token