from rest_framework import serializers
from .models import CustomUser, Categories, NeworPopular, Products

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name']

# class UserCreateSerailizer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)   # we never want to return it back in API responses, even after registration.
#                                                         # You can write (send) it from the frontend.  But it will not be shown in API responses.

#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'name', 'password']

#     def create(self, validated_data):
#         return CustomUser.objects.create_user(
#             email = validated_data['email'],
#             name = validated_data['name'],
#             password = validated_data['password']
#         )

class CategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class NeworPuSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeworPopular
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    # popular_or_new = NeworPuSerializer(read_only = True)
    # Use ID for writing
    popular_or_new = serializers.PrimaryKeyRelatedField(
        queryset = NeworPopular.objects.all(), write_only = True
    )

    # Use nested read-only for reading
    popular_or_new_data = serializers.SerializerMethodField(read_only = True)
    def get_popular_or_new_data(self, obj):
        if obj.popular_or_new:
            return{
                "id": obj.popular_or_new.id,
                "name": obj.popular_or_new.name,
                "color": obj.popular_or_new.color,
            }
        return None

    class Meta:
        model = Products
        fields = '__all__'