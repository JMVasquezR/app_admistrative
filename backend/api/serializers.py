from rest_framework import serializers

from backend.models.infractions import Infraction
from backend.models.vehicles import Vehicle


class InfractionSerializer(serializers.ModelSerializer):
    plate_number = serializers.CharField(write_only=True)

    class Meta:
        model = Infraction
        fields = ['id', 'plate_number', 'comment', 'official']
        read_only_fields = ['id', 'official']

    def validate_plate_number(self, value):
        try:
            vehicle = Vehicle.objects.get(plate_number=value)
        except Vehicle.DoesNotExist:
            raise serializers.ValidationError(f"El vehículo con placa {value} no existe.")

        return vehicle

    def create(self, validated_data):
        plate_number = validated_data.pop('plate_number')
        vehicle = validated_data.pop('vehicle', None)
        if vehicle is None:
            vehicle = plate_number

        return Infraction.objects.create(vehicle=vehicle, **validated_data)


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['plate_number']


class InfractionDetailSerializer(serializers.ModelSerializer):
    plate_number = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()

    class Meta:
        model = Infraction
        fields = ['plate_number', 'comment', 'created']

    def get_plate_number(self, obj):
        return obj.vehicle.plate_number

    def get_created(self, obj):
        return obj.created.strftime("%Y-%m-%d %H:%M:%S")
