import requests

endereco = "http://127.0.0.1:8000/v1/forecast"

parametros = {
    "latitude": -26.4851,
    "longitude": -49.0713,
    "timezone": "America/Sao_Paulo",
    "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m"
}
{
    "current_units":{ 
    "temperature_2m": "°C",
    "relative_humidity_2m": "%",
    "apparent_temperature": "°C",
    "precipitation": "mm",
    "wind_speed_10m": "km/h"

}
}

resposta = requests.get(
    endereco,
    params= parametros,
    timeout=15
)

resposta.raise_for_status()

dados = resposta.json()
def obter_dados_meteorologicos():
    temperatura_ar = dados['current']["temperature_2m"]
    Umidade_relativa = dados['current']['relative_humidity_2m']
    sensacao = dados['current']['apparent_temperature']
    precipitacao = dados['current']['precipitation']
    velocidade_vento = dados['current']['wind_speed_10m']
    horario = dados['current']['time']


    return {'temperatura': temperatura_ar, 'umidade': Umidade_relativa, 'sensacao': sensacao, 'precipitacao':precipitacao, 'vento':velocidade_vento, 'horario':horario}


# if resposta.status_code == 200:
#     print("A temperatura do ar é: ", temperatura_ar, "C")


# else:
#     print("ERRO NA REQUISIÇÃO!")