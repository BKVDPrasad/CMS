
from django.contrib import admin
from django.core.management import call_command
from django.http import HttpResponse
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework import routers
from app3.views import ItemView, my_kafka_producer
from bigP.schema import schema

routers = routers.DefaultRouter()
routers.register('items', ItemView)

from app3.management.commands import my_manage as cmd

def run_my_command(request):
    # You can pass arguments and options to the command
    # call_command('my_manage',[12,35,],new='kumarvenkata',)
    lcmd = cmd.Command()
    call_command(lcmd.handle('asdfasdfasdf',new='prasad'))
    # You can return a response or redirect to another view
    return HttpResponse('Command ran successfully')

urlpatterns = [
    path('', include(routers.urls)),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('my_command/', run_my_command, name='my_command'),
    path('new/', my_kafka_producer)
]

# from django.core.management import call_command
#
# def run_my_command(request):
#     # You can pass arguments and options to the command
#     call_command('my_command', arg1, arg2, option1=value1)
#     # You can return a response or redirect to another view
#     return HttpResponse('Command ran successfully')
#
# urlpatterns = [
#     path('my_command/', run_my_command, name='my_command'),
# ]