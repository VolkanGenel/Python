from rest_framework import serializers # type: ignore
from watchlist_app.models import WatchList, StreamPlatform

# MODELSERIALIZER
class WatchListSerializer(serializers.ModelSerializer):
    len_title = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id', 'name', "description", "active"]
        # exclude = ["name"] // name alanını alma anlamına gelir.
    
    def get_len_title(self, object):
        length = len(object.title)
        return length    

# Validators for SERIALIZER BELOW
def length_check(value):
    if len(value) < 2:
        raise serializers.ValidationError("Description is too short")
    else:
        return value   
# SERIALIZER
class StreamPlatformSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    about = serializers.CharField(validators=[length_check])
    website = serializers.CharField()

    def create(self, validated_data):     
        return StreamPlatform.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.website = validated_data.get('website', instance.website)
        instance.save()
        return instance
    
    # Object-level validation
    def validate(self, data):
        if data["name"] == data["about"]:
            raise serializers.ValidationError("Name and About should be different")
        else:
            return data
    # Field-level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value


# #SerializerMethodField
    # def get_len_name(self, object):
    #     length = len(object.name)
    #     return length

    # # Object-level validation
    # def validate(self, data):
    #     if data["name"] == data["description"]:
    #         raise serializers.ValidationError("Name and Description should be different")
    #     else:
    #         return data
    # # Field-level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value    

# SERIALIZER
# # Validators
# def length_check(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Description is too short")
#     else:
#         return value        

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[length_check])
#     active = serializers.BooleanField()

#     def create(self, validated_data):     
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # Object-level validation
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Name and Description should be different")
#         else:
#             return data
#     # Field-level validation
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         else:
#             return value