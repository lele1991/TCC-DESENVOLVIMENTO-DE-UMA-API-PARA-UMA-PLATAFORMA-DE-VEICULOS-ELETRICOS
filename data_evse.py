import requests

from requests.sessions import session


def get_data_from_evse(req):
    """
    requisita um dado do eletroposto da Voltbras
    :param req: O dado a desejado para a requisição
    :return:
        dado puro retornado pelo eletroposto
        erro -1 caso o eletroposto não retorne status code 200
        erro -2 caso req não esteja dentro das requisições esperadas
    """
    BASE_URL = "https://api.voltbras.com.br/graphql"
    TOKEN = "****"
    if req == "id":
        # Teste
        # result = {"stations": [{"id": "7eeab9db-d9c9-4865-bbda-9090baf9c884"}]}
        # status_code = 200
        # Requisição real a API da voltbras
        data = {"query": "{ stations { id }}"}
        result = requests.post(BASE_URL, json=data, headers={"api-key": TOKEN})
        if result.status_code == 200:
            # if status_code == 200:
            return result.json()["data"]
            # return result
        else:
            return -1

    elif req == "tarifa":
        # data = {"stations": [{"energyPrice": 2.0}]}
        # status_code = 200
        data = {"query": "{ stations { energyPrice }}"}
        result = requests.post(BASE_URL, json=data, headers={"api-key": TOKEN})
        if result.status_code == 200:
            # if status_code == 200:
            # if status_code == 200:
            return result.json()["data"]
            # return data
        else:
            return -1

    elif req == "energia_consumida":
        # data = {"sessions": [{"energyConsumed": 15}]}
        # status_code = 200
        data = {"query": "{ sessions { energyConsumed }}"}
        result = requests.post(BASE_URL, json=data, headers={"api-key": TOKEN})
        if result.status_code == 200:
            return result.json()["data"]
        # if status_code == 200:
        # print(data)
        # return data
        else:
            return -1

    elif req == "preco":
        # data = {"sessions": [{"chargePrice": 150.00}]}
        # status_code = 200
        data = {"query": "{ sessions { chargePrice }}"}
        result = requests.post(BASE_URL, json=data, headers={"api-key": TOKEN})
        if result.status_code == 200:
            return result.json()["data"]
        # if status_code == 200:
        # print(data)
        # return data
        else:
            return -1

    elif req == "potencia":
        # data = {"connectors": [{"power": 22000.00}]}
        # status_code = 200
        data = {"query": "{ stations { connectors { power }}}"}
        result = requests.post(BASE_URL, json=data, headers={"api-key": TOKEN})
        if result.status_code == 200:
            return result.json()["data"]
        # if status_code == 200:
        # print(data)
        # return data
        else:
            return -1

    elif req == "alldata":
        data = {"query": "{stations {id,energyPrice,connectors {power},sessions{chargePrice,energyConsumed}}}"}
        result = requests.post(BASE_URL, json=data, headers={"api-key": TOKEN})
        # data = {
        #     "data": {
        #         "stations": [
        #             {
        #                 "id": "7eeab9db-d9c9-4865-bbda-9090baf9c884",
        #                 "energyPrice": 0,
        #                 "connectors": [{"power": 22000}],
        #                 "sessions": [{"chargePrice": 0, "energyConsumed": 0}],
        #             }
        #         ]
        #     }
        # }
        # status_code = 200
        if result.status_code == 200:
            return result.json()["data"]
        else:
            return -1

    else:
        return -2


def verify_data(data, value):
    """
    Verifica se um dado é do tipo esperado
    :param data : o dado para verificar o valor
    :param value: valor para ser verificado o tipo
    :return:
        retorna o valor caso seja do tipo esperado
        erro -3 caso o dado seja diferente do esperado
    """
    if data == "id":
        if type(value) == str:
            return value
        else:
            return -3

    elif data == "tarifa":
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return value
        else:
            return -3

    elif data == "energia_consumida":
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return value
        else:
            return -3

    elif data == "preco":
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return value
        else:
            return -3

    elif data == "potencia":
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return value
        else:
            return -3


def request_data(req):
    """
    Realiza uma requisição ao eletroposto e verifica a consisyencia dos dados
    :param req : o dado a ser adquirido a informação
    :return:
        retorna o valor caso o processo seja bem sucedido
        erro -1 caso o eletroposto não retorna o dado
        erro -2 caso o dado solicitado não é provido pelo SW
        erro -3 caso o dado seja diferente do esperado
    """
    if req == "id":
        data = get_data_from_evse("id")
        if data["stations"] == []:
            return -1
        else:
            data = data["stations"][0]["id"]
            verified_data = verify_data("id", data)
            return verified_data

    elif req == "tarifa":
        data = get_data_from_evse("tarifa")
        if data["stations"] == []:
            return -1
        else:
            data = data["stations"][0]["energyPrice"]
            verified_data = verify_data("tarifa", data)
            return verified_data

    elif req == "energia_consumida":
        data = get_data_from_evse("energia_consumida")
        if data["sessions"] == []:
            return -1
        else:
            data = data["sessions"][0]["energyConsumed"]
            verified_data = verify_data("energia_consumida", data)
            return verified_data

    elif req == "preco":
        data = get_data_from_evse("preco")
        if data["sessions"] == []:
            return -1
        else:
            data = data["sessions"][0]["chargePrice"]
            verified_data = verify_data("preco", data)
            return verified_data

    elif req == "potencia":
        data = get_data_from_evse("potencia")
        if data["stations"] == [] or data["stations"][0]["connectors"] == []:
            return -1
        else:
            data = data["stations"][0]["connectors"][0]["power"]
            verified_data = verify_data("potencia", data)
            return verified_data

    elif req == "alldata":
        data = get_data_from_evse("alldata")
        if data["stations"] == [] or data["stations"][0]["connectors"] == [] or data["stations"][0]["sessions"] == []:
            return -1
        else:
            data_id =  data["stations"][0]["id"]
            data_tarifa =  data["stations"][0]["energyPrice"]
            data_energia_consumida =  data["sessions"][0]["energyConsumed"]
            data_preco =  data["sessions"][0]["chargePrice"]
            data_potencia =  data["stations"][0]["connectors"][0]["power"]
            if (verify_data("id", data_id) == -3 or verify_data("potencia", data_potencia) == -3 or verify_data("tarifa", data_tarifa) == -3 or
                verify_data("energia_consumida", data_energia_consumida) == -3 or  verify_data("preco", data_preco) == -3):
                return -3
        return data

    else:
        return -2
