import requests


def verify_evse():
    """
    Verifica se está disponível para requisição dos dados
    :return:
        True caso esteja disponível
        False caso esteja indisponível
    """
    BASE_URL = "https://api.voltbras.com.br/graphql"
    TOKEN = "****"

    # result = {'stations': [{'status': 'UNKNOWN'}]}
    # status_code = 200
    data = {"query": "{ stations { status }}"}
    result = requests.post(BASE_URL, json=data, headers={"api-key": TOKEN})

    if result.status_code == 200:
        data = result.json()["data"]["stations"][0]["status"]
        if (data == "AVAILABLE") or (data == "CHARGING") or (data == "UNKNOWN"):
            return True
        else:
            return False
    else:
        return False
