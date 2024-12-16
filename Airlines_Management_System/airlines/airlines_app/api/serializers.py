from rest_framework import serializers # type: ignore
from airlines_app.models import Airplane, Flight, Reservation
from datetime import datetime
import hashlib

# MODELSERIALIZER
class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ["created_at", "reservation_code"]

    created_at = serializers.SerializerMethodField()
    def get_created_at(self, obj):
        return obj.created_at.strftime("%d-%m-%Y %H:%M:%S")

    def generate_reservation_code(self, passenger_name, created_at):
        unique_string = f"{passenger_name}-{created_at}"
        hash_code = hashlib.md5(unique_string.encode()).hexdigest()[:10].upper()
        return hash_code

    def create(self, validated_data):
        passenger_name = validated_data.get("passenger_name")
        created_at = validated_data.get("created_at", None)
        if not created_at:
            created_at = datetime.now()
        validated_data["reservation_code"] = self.generate_reservation_code(passenger_name, created_at)
        return super().create(validated_data)

    def validate(self, data):
        request = self.context.get("request")
        instance = self.instance
        new_flight = data.get("flight", None)

        if request.method == "POST":
            flight = data.get("flight")

            if flight and flight.reservations.filter(status=True).count() >= flight.airplane.capacity:
                raise serializers.ValidationError(
                    {f"In this Flight Number {flight}": "Unfortunately, no seats available!"}
                )

        elif request.method == "PATCH":
            if new_flight and instance and instance.flight != new_flight:
                if new_flight.reservations.filter(status=True).count() >= new_flight.airplane.capacity:
                    raise serializers.ValidationError(
                        {f"In this Flight Number {new_flight}": "Unfortunately, no seats available!"}
                    )
    
        return data       

# Validators for SERIALIZER BELOW
def length_check(value):
    if len(value) < 2:
        raise serializers.ValidationError("City description is too short")
    else:
        return value   
# SERIALIZER
class FlightSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    flight_number = serializers.CharField()
    departure = serializers.CharField(validators=[length_check])
    destination = serializers.CharField(validators=[length_check])
    departure_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", input_formats=["%d-%m-%Y %H:%M:%S"])
    arrival_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", input_formats=["%d-%m-%Y %H:%M:%S"])
    airplane_id = serializers.PrimaryKeyRelatedField(queryset=Airplane.objects.all(), write_only=True)
    airplane = serializers.SerializerMethodField(read_only=True)
    flight_duration = serializers.SerializerMethodField() 
    reservations=ReservationSerializer(many=True, read_only=True)

    def get_airplane(self,object):
        return object.airplane.pk

    def create(self, validated_data):     
        return Flight.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.flight_number = validated_data.get("flight_number", instance.flight_number)
        instance.departure = validated_data.get("departure", instance.departure)
        instance.destination = validated_data.get("destination", instance.destination)
        instance.departure_time = validated_data.get("departure_time", instance.departure_time)
        instance.arrival_time = validated_data.get("arrival_time", instance.arrival_time)
        instance.destination = validated_data.get("destination", instance.destination)
        instance.save()
        return instance
    
    # Object-level validation
    def validate(self, data):
        if data["departure"] == data["destination"]:
            raise serializers.ValidationError("Same airport was chosen!")
        elif data["departure_time"] >= data["arrival_time"]:
            raise serializers.ValidationError("Time travel hasn't been invented yet!")
        else:
            return data
    # Field-level validation
    def validate_flight_number(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Flight Number is too short")
        else:
            return value
    def validate_departure_time(self, value):
        today = datetime.today().replace(tzinfo=None)
        if value.replace(tzinfo=None) < today:
            raise serializers.ValidationError("Flight date cannot be in the past.")
        else:
            return value
        
    def get_flight_duration(self, object):
        if object.arrival_time and object.departure_time:
            duration = object.arrival_time - object.departure_time
            total_seconds = int(duration.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            return f"{hours} hours {minutes} minutes"
        return "Invalid time was provided"
          
  # MODELSERIALIZER
class AirplaneSerializer(serializers.ModelSerializer):
    flights = FlightSerializer(many=True, read_only=True)
    class Meta:
        model = Airplane
        fields = "__all__" 