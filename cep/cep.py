import requests
import pyautogui as pyg
import re

class SearchCEP:

  # O Código de status de uma requisição bem sucedida
  STATUS_SUCCESS = [200]

  def _process_response(self, response):
    """
    Este método verifica se a requisição foi bem sucedida
    """
    if response.status_code in self.STATUS_SUCCESS:
      response = response.json()
      if not response.get("erro"):
        return response
    return "CEP Inválido"

  def _clean_cep(self, cep):
    """
    Este método limpará o cep, deixando apenas números
    Exemplo: 70.070-750 -> 70070750
    """
    cep = re.sub(r'\D', '', cep)
    return cep

  def process_cep(self, cep=None):
    """
    Este método é responsável por administrar o dado de centra: CEP,
    Efetuar a requisição e retornar uma resposta na forma de um
    Dicionário Python que conterá um "response" ou "error"
    """
    result = {"response": None, "error": None}
    if not cep:
      result["error"] = "Por favor, insira um CEP"
      return result
    cep = self._clean_cep(cep)
    url_base = f"https://viacep.com.br/ws/{cep}/json/"
    request = requests.get(url_base)
    result["response"] = self._process_response(request)
    return result

"""
Se este módulo for executado, por exemplo, pelo cmd:
> python3 cep.py
O bloco a seguir será executado
"""
if __name__ == '__main__':
  search = SearchCEP()
  cep = search.process_cep('Pedro')
  pyg.alert(
    text=cep["response"] if cep.get("response") else cep["error"],
    title="Dados do CEP",
    button="Fechar"
  )