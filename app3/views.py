from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from app3.models import Item
from app3.serializsers import ItemSerializer

from django.conf import settings


# Create your views here.


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ItemView(viewsets.ModelViewSet):
    model = apps.get_model('app3', 'item')
    print(model._meta.get_field("name"))
    print("______________________________________")
    queryset = model.objects.all().order_by('-pk')
    serializer_class = ItemSerializer
    pagination_class = StandardResultsSetPagination


# Import the Kafka library
from kafka import KafkaProducer, KafkaConsumer


# Define the Kafka settings in your Django settings file


# Create a Kafka producer in your Django view

def my_kafka_producer(request):
    # Create a KafkaProducer object
    # producer = KafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
    pass

    # producer = KafkaProducer(
    #     bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS  #####,
    #     client_id =  None,
    # value_serializer = {'a':2},
    # api_version = (0, 10, 1)
    # )
    #
    # # Send a message to the Kafka topic
    # producer.send(settings.KAFKA_TOPIC_PREFIX + 'my-topic', b'test')
    # # Return a HTTP response
    # return HttpResponse(200)
