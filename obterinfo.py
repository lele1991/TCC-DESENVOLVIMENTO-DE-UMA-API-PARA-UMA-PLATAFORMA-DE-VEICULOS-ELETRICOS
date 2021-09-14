#.\env\Scripts\Activate.ps1

from flask import Flask
from flask.scaffold import F
from flask.views import MethodView, MethodViewType

from main import genResponse, genResponse_error, genResponse_save, genResponse_help
from armazenardados import clear_json, write_json, get_data_for_id
from evse import verify_evse
from data_evse import request_data, get_data_from_evse

#O cliente pela Bplus requisita acesso aos dados.
#R1.1 O software deve receber uma requisição HTTP via arquitetura REST do cliente com as informações de interesse.

#Verificar disponibilidade do eletroposto no caso de uso 3.
#R1.2 O software deve enviar uma mensagem de erro “O eletroposto está OFFLINE” se a estação de recarga estiver inativa. 

#Verificar o dado no caso de uso 2.
#R1.3 O software deve enviar uma mensagem de erro “O parâmetro ‘X’ não foi encontrado” se o dado não estiver indisponível.

#O software retorna o valor ao cliente pela Bplus.
#R1.4 O software deve enviar o dado para o cliente via requisição HTTP.

Api = Flask("dados")

#O @ está a dizer a Python para decorar o índice de função() com o decorador definido em app.route().
#Basicamente, um decorador é uma função que modifica o comportamento de outra função.
@Api.route("/id", methods = ["GET"])
def verify_id():
    status = verify_evse()
    if (status == True):
            identidade = request_data("id")  
            if (identidade == -1):
                return genResponse("-1", "O parâmetro ID não foi encontrado")
            elif (identidade == -2):
                return genResponse("-2", "O parâmetro ID não é provido")
            elif (identidade == -3):
                return genResponse("-3", "O parâmetro ID retornado pelo eletroposto não é o esperado")
            else:
                return genResponse("200", "O parâmetro ID foi encontrado", "id", identidade)
    else:
        return genResponse_error("400", "O eletroposto está OFFLINE")

@Api.route("/tarifa", methods = ["GET"])
def verify_tarifa():
    status = verify_evse()
    if (status == True):
        identidade = request_data("id") 
        tarifa = request_data("tarifa") 
        if (identidade == -1):
            return genResponse_error("-1", "O parâmetro ID não foi encontrado")
        elif (identidade == -2):
            return genResponse_error("-2", "O parâmetro ID não é provido")
        elif (identidade == -3):
            return genResponse_error("-3", "O parâmetro ID retornado pelo eletroposto não é o esperado")
        else:
            if (tarifa == -1):
                return genResponse_error("-1", "O parâmetro TARIFA  não foi encontrado")
            elif (tarifa == -2):
                return genResponse_error("-2", "O parâmetro TARIFA não é provido")
            elif (tarifa == -3):
                return genResponse_error("-3", "O parâmetro TARIFA retornado pelo eletroposto não é o esperado")
            else:                
                write_json("tarifa", tarifa, identidade)
                return genResponse("200", "O parâmetro TARIFA foi encontrado", "tarifa", tarifa)         
                
    else:
        return genResponse_error("400", "O eletroposto está OFFLINE")

@Api.route("/energiaconsumida", methods = ["GET"])
def verify_energia_consumida():
    status = verify_evse()
    if (status == True):
        identidade = request_data("id") 
        energia_consumida = request_data("energia_consumida")             
        if (identidade == -1):
            return genResponse_error("-1", "O parâmetro ID não foi encontrado")
        elif (identidade == -2):
            return genResponse_error("-2", "O parâmetro ID não é provido")
        elif (identidade == -3):
            return genResponse_error("-3", "O parâmetro ID retornado pelo eletroposto não é o esperado")
        else:
            if (energia_consumida == -1):
                return genResponse_error("-1", "O parâmetro ENERGIA CONSUMIDA  não foi encontrado")
            elif (energia_consumida == -2):
                return genResponse_error("-2", "O parâmetro ENERGIA CONSUMIDA não é provido")
            elif (energia_consumida == -3):
                return genResponse_error("-3", "O parâmetro ENERGIA CONSUMIDA retornado pelo eletroposto não é o esperado")  
            else:             
                write_json("energia_consumida", energia_consumida, identidade)
                return genResponse("200", "O parâmetro ENERGIA CONSUMIDA foi encontrado", "energia_consumida", energia_consumida)
    else:
        return genResponse_error("400", "O eletroposto está OFFLINE")

@Api.route("/preco", methods = ["GET"])
def verify_preco():
    status = verify_evse()
    if (status == True):
        identidade = request_data("id") 
        preco = request_data("preco")             
        if (identidade == -1):
            return genResponse_error("-1", "O parâmetro ID não foi encontrado")
        elif (identidade == -2):
            return genResponse_error("-2", "O parâmetro ID não é provido")
        elif (identidade == -3):
            return genResponse_error("-3", "O parâmetro ID retornado pelo eletroposto não é o esperado")
        else:
            if (preco == -1):
                return genResponse_error("-1", "O parâmetro PREÇO  não foi encontrado")
            elif (preco == -2):
                return genResponse_error("-2", "O parâmetro PREÇO não é provido")
            elif (preco == -3):
                return genResponse_error("-3", "O parâmetro PREÇO retornado pelo eletroposto não é o esperado") 
            else:                
                write_json("preco", preco, identidade)
                return genResponse("200", "O parâmetro PREÇO foi encontrado", "preco", preco)
    else:
        return genResponse_error("400", "O eletroposto está OFFLINE")

@Api.route("/potencia", methods = ["GET"])
def verify_potencia():
    status = verify_evse()
    if (status == True):
        identidade = request_data("id") 
        potencia = request_data("potencia")             
        if (identidade == -1):
            return genResponse_error("-1", "O parâmetro ID não foi encontrado")
        elif (identidade == -2):
            return genResponse_error("-2", "O parâmetro ID não é provido")
        elif (identidade == -3):
            return genResponse_error("-3", "O parâmetro ID retornado pelo eletroposto não é o esperado")
        else:
            if (potencia == -1):
                return genResponse_error("-1", "O parâmetro POTÊNCIA  não foi encontrado")
            elif (potencia == -2):
                return genResponse_error("-2", "O parâmetro POTÊNCIA não é provido")
            elif (potencia == -3):
                return genResponse_error("-3", "O parâmetro POTÊNCIA retornado pelo eletroposto não é o esperado") 
            else:                
                write_json("potencia", potencia, identidade)
                return genResponse("200", "O parâmetro POTÊNCIA foi encontrado", "potencia", potencia)
    else:
        return genResponse_error("400", "O eletroposto está OFFLINE")

@Api.route("/todos", methods = ["GET"])
def armazenar_all():
    status = verify_evse()
    if (status == True):
        identidade = request_data("id") 
        all_data = request_data("alldata") 
        if (identidade == -1):
            return genResponse_error("-1", "O parâmetro ID não foi encontrado")
        elif (identidade == -2):
            return genResponse_error("-2", "O parâmetro ID não é provido")
        elif (identidade == -3):
            return genResponse_error("-3", "O parâmetro ID retornado pelo eletroposto não é o esperado")
        else:
            write_json("armazenado", all_data, identidade)
            if (all_data == -1):
                return genResponse_error("-1", "Nenhum parâmetro encontrado")
            else:
                return genResponse("200", "Armazenado", "Todos os dados", all_data)
    else:
        return genResponse_error("400", "O eletroposto está OFFLINE")


@Api.route("/limparjson", methods = ["GET"])
def limpar_json():
    clear_json()
    return genResponse_save("200", "O arquivo está limpo")

@Api.route("/ajuda", methods = ["GET"])
def ajuda():
    id = "/id para retornar a ID da estação de recarga"
    tarifa = "/tarifa para retornar a tarifa da energia"
    energia = "/energiaconsumida para retornar a quandidade de energia utilizada na recarga"
    preco = "/preco para retornar o preço total da recarga"
    potencia = "/potencia para retornar a potência máxima da estação de recarga"
    todos = "/todos para retornar todos os dados unicamente"
    return genResponse_help("200", "Tipos de parâmetros retornáveis", id, tarifa, energia, preco, potencia, todos)

Api.run()      