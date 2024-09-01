from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa = Pessoa("João Silva", "123456", "01/01/2020", "Ativa")
pessoaFisica = PessoaFisica("Maria Souza", "654321", "02/02/2021", "Inativa", "15/05/1980", "12345678901", "MG1234567")
pessoaJuridica = PessoaJuridica("Empresa XYZ", "789012", "03/03/2022", "Ativa", "05/10/2010", "12.345.678/0001-00")

pessoa.imprimir_informacoes()
print("\n")
pessoaFisica.imprimir_informacoes()
print("\n")
pessoaJuridica.imprimir_informacoes()

pessoa.nome = "João Pereira"
pessoaFisica.cpf = "10987654321"
pessoaJuridica.cnpj = "98.765.432/0001-99"

print("\nValores alterados:\n")
pessoa.imprimir_informacoes()
print("\n")
pessoaFisica.imprimir_informacoes()
print("\n")
pessoaJuridica.imprimir_informacoes()