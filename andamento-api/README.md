# API de Notificação

## Pré-requsitos
* Node.js - v22.13.1, para testar a versão: `node -v`

* Subir o docker do Banco de dados
```bash
CD API_integracao_de_sistemas\DATABASE 
docker build -t bd_user_tasks .
docker run -p 5432:5432 --name=dk-bd_user_tasks bd_user_tasks 
``` 
* Subir o docker do Redis
```bash
docker run --name redis-andamento -p 6379:6379 -d redis
``` 
## Rodando a API
```bash
npm run start
``` 
Ambiente de desenvolvimento
```bash
npm run start:dev
```

## Dependencias
```bash
* npm install express         # Framework para rotas e servidor HTTP
* npm install pg              # Cliente PostgreSQL para Node.js
* npm install ioredis           # Cliente Redis para Node.js
* npm install keyv            # Armazenamento em cache simples e compatível com Redis
```

##
### Requisições no Postman:
- `POST` - API de **Tarefas** vai enviar os dados para:
```bash
http://localhost:3000/notificacao-tarefa
``` 
`JSON` para envio no **BODY**
```bash
{
  "idTarefa": 1,
  "titulo": "titulo",
  "descricao": "descrição",
  "status": "A Fazer",
  "prazo": "2025-05-15",
  "idEquipe": 2,
  "idUsuarioResponsavel": 1
}
``` 
### Regras do Endpoint: 
Se a TAREFA não existir na tabela Andamento, será retornado:
> XXXX que pertence a equipe: XXXX criou a TITULO_TAREFA

Se a TAREFA já existir na tabela Andamento, será retornado:
> XXXX que pertence a equipe: XXXX alterou o status da TITULO_TAREFA de ANTIGO_STATUS para NOVO_STATUS`

#

- `GET` - Buscar histórico de uma tarefa por titulo:
```bash
localhost:3000/historico-tarefa/TITULO DA TAREFA
``` 
