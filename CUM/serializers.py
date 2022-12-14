from rest_framework import serializers

from .models import Category, Item


def is_simbol(value):
    for i in value:
        if i not in '!@#$%^&*':
            raise serializers.ValidationError(' В названии не должно быть данных символов')


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=200)

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.name = validated_data['description']
        instance.save()
        return instance


class ItemSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    category_id = serializers.IntegerField()
    price = serializers.IntegerField()
    QR = serializers.CharField(max_length=20)

    class Meta:
        validators = [serializers.UniqueTogetherValidator(Item.objects.all(), fields=['item_id'], )]

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['Item_id']
        instance.name = validated_data['name']
        instance.name = validated_data['category_id']
        instance.name = validated_data['price']
        instance.name = validated_data['QR']
        instance.save()
        return instance
