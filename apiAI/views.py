"""vievs"""
import json
from django.shortcuts import render


def crypto_prices(request):
    """retrieve crypto data"""
    file_path = "/home/veigar/Desktop/django_projects/tang_wit_django_wEB_APP/apiAI/management/commands/api_data.json"

    with open(file_path, 'r') as f:
        data = json.load(f)
    return render(request, 'apiAI/crypto_prices.html', {'data': data})
