Como Usar

Execute o arquivo main.py para iniciar a API.

Acesse a URL http://localhost:5000/filmes/<ano> no seu navegador ou via ferramenta de teste de API, substituindo <ano> pelo ano de lançamento desejado
A API retornará uma resposta JSON com os filmes encontrados para o ano de lançamento informado

Exemplo de Uso

Consulta de filmes lançados em 2021: 
GET http://localhost:5000/filmes/2021

{
  "filmes": [
    {
      "Nome": "Velozes e Furiosos 9",
      "Ano": 2021
    }
  ]
}

Retorno de Erros
A API retorna as seguintes mensagens de erro em caso de problemas:

400 Bad Request: Ano de lançamento inválido
404 Not Found: Nenhum filme encontrado para o ano de lançamento informado
