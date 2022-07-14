"""
TODO:
Přidat requirements.txt
Přidat Readme.txt
"""

import json

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_data(request):
    file = open(r'api\test_data.json', encoding="utf-8")
    data = json.load(file)
    return Response(data)


@api_view(["GET"])
def get_model(request, model):
    file = open(r'api\test_data.json', encoding="utf-8")
    data = json.load(file)
    result = [json_model for json_model in data if model in json_model]
    return Response(result) if result else Response({"message": f"No model named: {model} found"})


@api_view(["GET"])
def get_model_by_id(request, model, model_id):
    file = open(r'api\test_data.json', encoding="utf-8")
    data = json.load(file)
    models = [json_model for json_model in data if model in json_model]
    result = [json_model for json_model in models if json_model[model]["id"] == model_id]
    return Response(result) if result else Response({"message": f"No model named: {model} with id: {model_id} found"})


@api_view(["POST"])
def add_item(request):
    file = open(r'api\test_data.json', "r+", encoding="utf-8")
    if request.data:
        json_file = json.load(file)
        json_file.append(request.data)
        json_object = json.dumps(json_file, indent=4)
        with open(r'api\test_data.json', 'w', encoding="utf-8") as outfile:
            outfile.write(json_object)
    return Response(request.data)
