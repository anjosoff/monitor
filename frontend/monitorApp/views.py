from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.


def home(request):
    data=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f'[{data}] LOG INTERNO: Fazendo conexão com a API de Painéis')
    r=''
    try:
        r = requests.get('http://127.0.0.1:5000/v1/consultar')  
        print(f'[{data}] LOG INTERNO: Conexão bem sucedida, dados atualizados')
    except Exception as e2:
        print(f'[{data}] LOG INTERNO: Houve um erro na conexão com a API')
    if r:
        consulta = r.json()
    else:
        consulta={'painel':'Houve um erro na comunicação com a API Paineis'}
    return render(request, 'monitorApp/index.html',{'consultar':consulta})