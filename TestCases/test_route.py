import pytest
import json
import requests

def test_todos_route():
	URL = 'http://127.0.0.1:5000/todos'
	
	response = requests.get(URL)
	assert response.status_code == 200

def test_limpar_route():
	URL = 'http://127.0.0.1:5000/limparjson'
	
	response = requests.get(URL)
	assert response.status_code == 200

def test_ajuda_route():
	URL = 'http://127.0.0.1:5000/ajuda'
	
	response = requests.get(URL)
	assert response.status_code == 200

def test_id_route():
	URL = 'http://127.0.0.1:5000/id'
	
	response = requests.get(URL)
	assert response.status_code == 200

def test_tarifa_route():
	URL = 'http://127.0.0.1:5000/tarifa'
	
	response = requests.get(URL)
	assert response.status_code == 200

def test_energiaconsumida_route():
	URL = 'http://127.0.0.1:5000/energiaconsumida'
	
	response = requests.get(URL)
	assert response.status_code == 200

def test_preco_route():
	URL = 'http://127.0.0.1:5000/preco'
	
	response = requests.get(URL)
	assert response.status_code == 200

def test_potencia_route():
	URL = 'http://127.0.0.1:5000/potencia'
	
	response = requests.get(URL)
	assert response.status_code == 200

def test_erro_api():
	# rota inexistente
	URL = 'http://127.0.0.1:5000/api'
	
	response = requests.get(URL)
	assert response.status_code == 404

def test_erro_semrota():
	# rota inexistente
	URL = 'http://127.0.0.1:5000/'
	
	response = requests.get(URL)
	assert response.status_code == 404

