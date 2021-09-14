from datetime import datetime
import json

# O software deverá armazenar os dados lidos em um banco de dados.
# R4.1 O software deve salvar os dados requisitados no requisito R2.2  em um banco de dados em formato JSON 
# R4.2 O software deve enviar uma mensagem de erro "O dado ‘X’ não foi armazenado"  se os dados não forem  armazenados. 

# O software deverá acessar o banco de dados.

# function to add to JSON
# data chega como str
def write_json(dataName, data, id):
    #print(data)

    #load arquivo lista
    with open('Code/databaseAXS.json', 'r') as file:
        # First we load existing data into a dict.
        # Lista de ojetos
        clientlist = json.load(file)
        timestamp = datetime.now().timestamp()

        newEntry = {"id": id, dataName: data, "timestamp": timestamp}
        clientlist["clients"].append(newEntry)
    
        for item in range(len(clientlist["clients"])): 
            if (clientlist["clients"][item]["timestamp"] == timestamp):   
                if (clientlist["clients"][item]["id"] == id):
                    print("O ID foi armazenado:", id)
                else:
                    print("O ID NÃO foi armazenado:", id)
                if (clientlist["clients"][item][dataName] == data):
                    print("O DADO foi armazenado:", data)
                else:
                    print("O DADO NÃO foi armazenado: ", data)

        # found = False
        # #roda cada um dos clientes
        # for item in range(len(clientlist)):
        #     if (clientlist["clients"][item]["id"] == id):
        #         found = True
        #         #add
        #         clientlist["clients"][0][dataName] = data
        #         break

        # if found == False :
        #     newEntry = {"id": id, dataName: data, "timestamp": datetime.now().timestamp()}
        #     #adicionar date/time
        #     clientlist["clients"].append(newEntry)

        #manipulação de dados
        #clientlist["clients"][0]["id"] = 10    
    with open('Code/databaseAXS.json','w') as file:
        # convert back to json.
        json.dump(clientlist, file, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
    
def clear_json():
    with open('Code/databaseAXS.json', 'r') as file:
        clientlist = json.load(file)
        clientlist["clients"].clear()

    with open('Code/databaseAXS.json','w') as file:
        # convert back to json.
        json.dump(clientlist, file, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

def get_data_for_id(id, timestamp):
    with open('Code/databaseAXS.json', 'r') as file:
        clientlist = json.load(file)
        for client in clientlist["clients"]:
            if (client["id"] == id):
                if(client["timestamp" == timestamp]):
                    return client