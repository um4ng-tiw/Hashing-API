from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import hashlib
import json
from datetime import datetime
import bcrypt
# Create your views here.


@api_view(['GET'])
def hashOverview(request):
    api_urls ={
        'Create-hash': '/create',
    }
    return Response(api_urls)

@api_view(['POST'])
def createHash(request):
    print(request.data)
    received_data = request.data
    # Getting the time stamp as a string
    timestamp = str(datetime.now())

    # Adding timestamp to the received data
    received_data['timestamp'] = timestamp
    print("Received Data:", received_data)

    # Converting the json to byte data
    byte_data = json.dumps(received_data, sort_keys=True, indent=1)
    byte_data= byte_data.encode("utf-8")

    # Generating the salt
    salt = bcrypt.gensalt()

    # Hashing and sending the hash back to client
    dk = hashlib.pbkdf2_hmac('sha256', byte_data, salt, 500000)
    hashed_data = dk.hex()
    received_data['hash'] = hashed_data
    return Response(received_data)
