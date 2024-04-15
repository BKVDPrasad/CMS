from rest_framework import serializers

from app3.models import Item


class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=5, decimal_places=2, )
    class Meta:
        model = Item
        fields = "__all__"

    def validate_name(self, sname):
        if sname.isnumeric():
            raise serializers.ValidationError('name must be string')
        return sname
    # def validate(self, attrs):
    #     if not attrs['price'].isdecimal():
    #         raise serializers.ValidationError('number must be numeric')
