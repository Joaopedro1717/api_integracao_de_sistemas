# Documentação dos Endpoints

## Listar todas as tarefas
### GET /tarefas  
```http://localhost:8080/tarefas```

```json
[
    {
        "id": 1,
        "titulo": "Reunião de planejamento",
        "descricao": "Definir escopo do projeto",
        "status": "Concluído",
        "prazo": "2025-05-10",
        "idEquipe": 1,
        "idUsuarioResponsavel": 2
    }
]
```

## Obter tarefa por ID
### GET /tarefas{id}
```http://localhost:8080/tarefas/1```

```json
[
  {
    "id": 1,
    "titulo": "Reunião de planejamento",
    "descricao": "Definir escopo do projeto",
    "status": "Concluído",
    "prazo": "2025-05-10",
    "idEquipe": 1,
    "idUsuarioResponsavel": 2
  }
]
```


## Criar nova tarefa
### POST /tarefas
```http://localhost:8080/tarefas```

```json
[
  {
    "titulo": "Desenvolver endpoint POST",
    "descricao": "Implementar criação de tarefas",
    "status": "Em andamento",
    "prazo": "2025-05-20",
    "idEquipe": 2,
    "idUsuarioResponsavel": 3
  }
]
```
### Exemplo de resposta:
```json
[
  {
    "id": 2,
    "titulo": "Desenvolver endpoint POST",
    "descricao": "Implementar criação de tarefas",
    "status": "Em andamento",
    "prazo": "2025-05-20",
    "idEquipe": 2,
    "idUsuarioResponsavel": 3
  }
]
```


## Atualizar tarefa
### PUT /tarefas/{id}
```http://localhost:8080/tarefas/2```

```json
[
  {
    "titulo": "Desenvolver endpoint PUT",
    "status": "Concluído",
    "prazo": "2025-05-18"
  }
]
```
### Exemplo de resposta:
```json
[
  {
    "id": 2,
    "titulo": "Desenvolver endpoint PUT",
    "descricao": "Implementar criação de tarefas",
    "status": "Concluído",
    "prazo": "2025-05-18",
    "idEquipe": 2,
    "idUsuarioResponsavel": 3
  }
]
```


## Remover tarefa
### DELETE /tarefas/{id}
```http://localhost:8080/tarefas/2```

```json
[
  {
    "id": 1,
    "titulo": "Reunião de planejamento",
    "descricao": "Definir escopo do projeto",
    "status": "Concluído",
    "prazo": "2025-05-10",
    "idEquipe": 1,
    "idUsuarioResponsavel": 2
  }
]
```
#### Resposta: Status 204 No Content (sem corpo)

### Insert inicial para dados de teste
````sql
-- Inserindo equipes (como o ID é SERIAL, podemos omitir ou usar DEFAULT)
INSERT INTO public.equipe (id, nome) VALUES (1, 'Equipe de Desenvolvimento');
INSERT INTO public.equipe (id, nome) VALUES (2, 'Equipe de QA');
INSERT INTO public.equipe (id, nome) VALUES (3, 'Equipe de DevOps');
INSERT INTO public.equipe (id, nome) VALUES (4, 'Equipe de Design');
INSERT INTO public.equipe (id, nome) VALUES (5, 'Equipe Comercial');

-- Desenvolvedores (Equipe 1)
INSERT INTO public.usuarios (id, nome, email, cargo, id_equipe) VALUES 
(1, 'João Silva', 'joao.silva@empresa.com', 'Desenvolvedor Backend', 1),
(2, 'Maria Oliveira', 'maria.oliveira@empresa.com', 'Desenvolvedor Frontend', 1),
(3, 'Carlos Souza', 'carlos.souza@empresa.com', 'Arquiteto de Software', 1);

-- QA (Equipe 2)
INSERT INTO public.usuarios (id, nome, email, cargo, id_equipe) VALUES 
(4, 'Ana Santos', 'ana.santos@empresa.com', 'Analista de QA Sênior', 2),
(5, 'Pedro Rocha', 'pedro.rocha@empresa.com', 'Engenheiro de Testes', 2);

-- DevOps (Equipe 3)
INSERT INTO public.usuarios (id, nome, email, cargo, id_equipe) VALUES 
(6, 'Fernanda Lima', 'fernanda.lima@empresa.com', 'Engenheira de DevOps', 3),
(7, 'Ricardo Alves', 'ricardo.alves@empresa.com', 'Especialista em Cloud', 3);

-- Design (Equipe 4)
INSERT INTO public.usuarios (id, nome, email, cargo, id_equipe) VALUES 
(8, 'Juliana Costa', 'juliana.costa@empresa.com', 'Designer UX/UI', 4),
(9, 'Marcos Ribeiro', 'marcos.ribeiro@empresa.com', 'Designer Gráfico', 4);

-- Comercial (Equipe 5)
INSERT INTO public.usuarios (id, nome, email, cargo, id_equipe) VALUES 
(10, 'Patricia Nunes', 'patricia.nunes@empresa.com', 'Gerente Comercial', 5),
(11, 'Roberto Ferreira', 'roberto.ferreira@empresa.com', 'Executivo de Vendas', 5);
````