from rest_framework import serializers

from prueba.models import clients, products, bills


class clientsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    document = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=30)
    contra = serializers.CharField(max_length=200)

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


class productSerializer(serializers.Serializer):
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


class billsSerializer(serializers.Serializer):
    client_id = serializers.IntegerField()
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
