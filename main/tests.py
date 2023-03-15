import json

import factory
from django.test.client import encode_multipart, RequestFactory
from factory.django import DjangoModelFactory
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from main import models
from main.models import PrivateKey, BTCAddress, ETHAddress


class BTCAddressFactory(DjangoModelFactory):
    address = factory.Faker("street_address")

    class Meta:
        model = models.BTCAddress


class ETHAddressFactory(DjangoModelFactory):
    address = factory.Faker("street_address")

    class Meta:
        model = models.ETHAddress


class TestBTCAddressView(APITestCase):
    def setUp(self):
        self.url = "/create-btc-address/"  # use the view url
        self.key = PrivateKey.objects.create(key='asdfadsfasdg')
        self.address = BTCAddress.objects.create(private_key=self.key, address='asdfadsf')

        self.address.private_key = self.key

    def test_get(self):
        response = self.client.get(self.url)
        response.render()
        self.assertEquals(200, response.status_code)
        self.assertTrue('address' in json.loads(response.content))


class TestETHAddressView(APITestCase):
    def setUp(self):
        self.url = "/create-eth-address/"  # use the view url
        self.key = PrivateKey.objects.create(key='asdfadsfasdg')
        self.address = ETHAddress.objects.create(private_key=self.key, address='asdfadsf')

        self.address.private_key = self.key

    def test_get(self):
        response = self.client.get(self.url)
        response.render()
        self.assertEquals(200, response.status_code)
        self.assertTrue('address' in json.loads(response.content))
