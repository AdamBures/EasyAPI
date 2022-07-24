"""
TODO:
Přidat requirements.txt
Přidat Readme.txt
"""

import json
from pathlib import Path
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Item
from .serializers import ItemSerializer

@api_view(["GET"])
def get_data(request):
    file = open(Path('api_folder/test_data.json'), encoding="utf-8")
    data = json.load(file)
    return Response(data)


@api_view(["GET"])
def get_model(request, model):
    file = open(Path('api_folder/test_data.json'), encoding="utf-8")
    data = json.load(file)
    result = [json_model for json_model in data if model in json_model]
    return Response(result) if result else Response({"message": f"No model named: {model} found"})


@api_view(["GET"])
def get_model_by_id(request, model, model_id):
    file = open(Path('api_folder/test_data.json'), encoding="utf-8")
    data = json.load(file)
    models = [json_model for json_model in data if model in json_model]
    result = [json_model for json_model in models if json_model[model]["id"] == model_id]
    return Response(result) if result else Response({"message": f"No model named: {model} with id: {model_id} found"})


@api_view(["POST"])
def add_item(request):
    file = open(Path('api_folder/test_data.json'), "r+", encoding="utf-8")
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        json_file = json.load(file)
        json_file.append(request.data)
        json_object = json.dumps(json_file, indent=4)
        with open(Path('api_folder/test_data.json'), 'w', encoding="utf-8") as outfile:
            outfile.write(json_object)
    else:
        return Response({'error': "Enter valid JSON"})    
    return Response(request.data)

def main(request):
    return render(request, Path('index.html'))