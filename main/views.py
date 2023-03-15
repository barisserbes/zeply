import secrets

from django.http import Http404
from bitcoin import random_key, privtopub, pubtoaddr
from eth_account import Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import PrivateKey, BTCAddress, ETHAddress
from main.serializers import BTCAddressSerializer, ETHAddressSerializer


class BTCAddressView(APIView):
    def get_object(self, pk):
        try:
            return BTCAddress.objects.get(pk=pk)
        except BTCAddress.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BTCAddressSerializer(snippet)
        return Response(serializer.data)


class BTCAddressList(APIView):
    def get(self, request, format=None):
        snippets = BTCAddress.objects.all()
        serializer = BTCAddressSerializer(snippets, many=True)
        return Response(serializer.data)


class ETHAddressView(APIView):
    def get_object(self, pk):
        try:
            return ETHAddress.objects.get(pk=pk)
        except ETHAddress.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ETHAddressSerializer(snippet)
        return Response(serializer.data)


class ETHAddressList(APIView):
    def get(self, request, format=None):
        snippets = ETHAddress.objects.all()
        serializer = ETHAddressSerializer(snippets, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def btc_address(request):
    # I have created this endpoint to create the BTC address we need
    private_key = random_key()
    p_key = PrivateKey.objects.create(key=private_key)
    public_key = privtopub(private_key)
    address = pubtoaddr(public_key)
    btc_address = BTCAddress.objects.create(private_key=p_key, address=address)
    return Response({"address": btc_address.address})


@api_view(['GET'])
def eth_address(request):
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    p_key = PrivateKey.objects.create(key=private_key)
    eth_address = ETHAddress.objects.create(private_key=p_key, address=acct.address)
    return Response({"address": eth_address.address})
