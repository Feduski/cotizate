from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    response = requests.get('https://dolarapi.com/v1/dolares/').json()
    dollars = [] 
    for x in range(len(response)):
        venta_dolar = response[x]['venta']
        compra_dolar = response[x]['compra']
        nombre = response[x]['nombre']
        dollars.append({'nombre': nombre, 'venta_dolar': venta_dolar, 'compra_dolar': compra_dolar})
    return render(request, 'home.html', {'dolares': dollars[:7]})