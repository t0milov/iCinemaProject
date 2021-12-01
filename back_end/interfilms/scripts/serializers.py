from rest_framework import serializers
# Файл используется для указания классов параметров при сериализации
from .models import origin, nodeList, coordinate, meta, linkList, startAt, endAt


class OriginSerializer(serializers.Serializer):
    width = serializers.IntegerField()
    length = serializers.IntegerField()

    def create(self, validated_data):
        return origin.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.width = validated_data.get('width', instance.width)
        instance.length = validated_data.get('length', instance.length)
        instance.save()

        return instance

class CoordinateSerializer(serializers.Serializer):
    x_coordinate = serializers.IntegerField()
    y_coordinate = serializers.IntegerField()

    def create(self, validated_data):
        return coordinate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.x_coordinate = validated_data.get('x_coordinate', instance.x_coordinate)
        instance.y_coordinate = validated_data.get('y_coordinate', instance.y_coordinate)
        instance.save()

        return instance

class MetaSerializer(serializers.Serializer):
    prop = serializers.CharField()
    name = serializers.CharField()

    def create(self, validated_data):
        return meta.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.prop = validated_data.get('prop', instance.prop)
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance

class NodeListSerializer(serializers.Serializer):
    id = serializers.CharField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    coordinate = CoordinateSerializer()
    meta = MetaSerializer()

    def create(self, validated_data):
        return nodeList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.width = validated_data.get('width', instance.width)
        instance.height = validated_data.get('height', instance.height)
        instance.coordinate = validated_data.get('coordinate', instance.coordinate)
        instance.meta = validated_data.get('meta', instance.meta)

        instance.save()

        return instance

class StartAtSerializer(serializers.Serializer):
    x_coordinate = serializers.IntegerField()
    y_coordinate = serializers.IntegerField()

    def create(self, validated_data):
        return startAt.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.x_coordinate = validated_data.get('x_coordinate', instance.x_coordinate)
        instance.y_coordinate = validated_data.get('y_coordinate', instance.y_coordinate)
        instance.save()

        return instance

class EndAtSerializer(serializers.Serializer):
    x_coordinate = serializers.IntegerField()
    y_coordinate = serializers.IntegerField()

    def create(self, validated_data):
        return endAt.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.x_coordinate = validated_data.get('x_coordinate', instance.x_coordinate)
        instance.y_coordinate = validated_data.get('y_coordinate', instance.y_coordinate)
        instance.save()

        return instance

class LinkListSerializer(serializers.Serializer):
    id = serializers.CharField()
    startId = serializers.CharField()
    endId = serializers.CharField()
    startAt = StartAtSerializer()
    endAt = EndAtSerializer()
    meta = serializers.CharField(default=None)

    class Meta:
        model = linkList
        fields = ('x_coordinate', 'y_coordinate')

    def create(self, validated_data):
        return linkList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.startId = validated_data.get('startId', instance.startId)
        instance.endId = validated_data.get('endId', instance.endId)
        instance.startAt = validated_data.get('startAt', instance.startAt)
        instance.endAt = validated_data.get('endAt', instance.endAt)
        instance.meta = validated_data.get('meta', instance.meta)
        instance.save()

        return instance

class CommonSerializer():
    origin = OriginSerializer()
    CoordinateSerializer()
    MetaSerializer()
    NodeListSerializer()
    StartAtSerializer()
    EndAtSerializer()
    LinkListSerializer()




