from rest_framework import serializers
from main.models import BTCAddress, ETHAddress


class BTCAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTCAddress
        fields = "__all__"


class ETHAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ETHAddress
        fields = "__all__"
