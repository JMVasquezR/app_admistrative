from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND)
from rest_framework.views import APIView

from backend.api.serializers import InfractionSerializer, InfractionDetailSerializer
from backend.models.infractions import Infraction
from backend.models.persons import Person
from backend.models.vehicles import Vehicle


class ChargeInfractionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = InfractionSerializer(data=request.data)

        if serializer.is_valid():
            plate_number = serializer.validated_data.get('plate_number')

            try:
                Vehicle.objects.get(plate_number=plate_number)
            except Vehicle.DoesNotExist:
                return Response(
                    {"error": f"Vehículo con placa {plate_number} no encontrado."}, status=HTTP_404_NOT_FOUND
                )

            serializer.save(official=request.user.official)
            data = {
                "message": "Infracción registrada correctamente",
            }
            return Response(data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_404_NOT_FOUND)


class ListInfractionForEmailView(APIView):
    def get(self, request, email, format=None):
        try:
            person = Person.objects.get(email=email)
        except Person.DoesNotExist:
            return Response(
                {"error": "Persona con este correo electrónico no encontrada."}, status=HTTP_404_NOT_FOUND
            )

        infracciones = Infraction.objects.filter(vehicle__person=person)
        serializer = InfractionDetailSerializer(infracciones, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
