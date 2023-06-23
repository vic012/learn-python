import pyautogui as pyg
from cep import SearchCEP

class UserWindow:

	def ask_cep(self):
		"""
		Método responsável por exibir uma caixa de diálogo
		Para que o cliente possa inserir dados
		"""
		return pyg.prompt(
			text="Digite um cep para a consulta",
			title="Buscar CEP",
			default="00.000-000"
		)

	def search(self):
		"""
		Método responsável por colher o dado digitado pelo cliente,
		Enviar este dado para o Módulo cep.py que fará a consulta e
		Retornará para o cliente uma janela com o resultado
		"""
		cep = self.ask_cep()
		if cep is not None:
			search = SearchCEP()
			response = search.process_cep(cep)
			pyg.alert(
				text=response["response"] if response.get("response") else response["error"],
				title="Dados do CEP",
				button="Fechar"
			)

if __name__ == '__main__':
	UserWindow().search()
