
def genResponse(status, msg, tipo_dado, dado, nome_cont=False, cont= False):
    response = {}
    response[tipo_dado] = dado
    response["status"] = status
    response["msg"] = msg
    
    if(nome_cont and cont):
        response[nome_cont] = cont
    return response

def genResponse_error(status, msg, nome_cont=False, cont= False):
    response = {}
    response["status"] = status
    response["msg"] = msg
    
    if(nome_cont and cont):
        response[nome_cont] = cont
    return response

def genResponse_save(status, msg, nome_cont=False, cont= False):
    response = {}
    response["status"] = status
    response["msg"] = msg
    
    if(nome_cont and cont):
        response[nome_cont] = cont
    return response

def genResponse_help(status, msg, id, tarifa, energia, preco, potencia, todos,nome_cont=False, cont= False):
    response = {}
    response["status"] = status
    response["msg"] = msg
    response["ID"]= id
    response["Tarifa"] = tarifa
    response["Energia Consumida"] = energia
    response["Preço"] = preco
    response["Potência"] = potencia
    response["Todos"] = todos
    
    if(nome_cont and cont):
        response[nome_cont] = cont
    return response