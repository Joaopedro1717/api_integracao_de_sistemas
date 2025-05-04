-- Inserir equipes
INSERT INTO Equipe (Id, Nome) VALUES
(1, 'Equipe Backend'),
(2, 'Equipe Frontend');

-- Inserir usuários
INSERT INTO Usuarios (Id, Nome, Email, Cargo, Id_Equipe) VALUES
(1, 'João Silva', 'joao@empresa.com', 'Desenvolvedor Backend', 1),
(2, 'Maria Souza', 'maria@empresa.com', 'Desenvolvedora Frontend', 2),
(3, 'Carlos Lima', 'carlos@empresa.com', 'Tech Lead', 1);

-- Inserir tarefas
INSERT INTO Tarefas (Id, Titulo, Descricao, Status, Prazo, Id_Equipe, Id_Usuario_Responsavel) VALUES
(1, 'Criar endpoint de login', 'Desenvolver autenticação JWT no backend', 'Em andamento', '2025-05-10', 1, 1),
(2, 'Criar tela de cadastro', 'Interface de cadastro no app web', 'Pendente', '2025-05-12', 2, 2),
(3, 'Refatorar serviços de email', 'Melhorar envio de notificações', 'Concluído', '2025-05-08', 1, 3);

-- Inserir andamentos (com Data_Criacao)
INSERT INTO Andamento (Mensagem, Status_antigo, Status_atual, Id_Usuario, Id_Tarefa, Data_Criacao) VALUES
('João Silva criou a tarefa Criar endpoint de login', 'Tarefa nova', 'Em andamento', 1, 1, '2025-05-01 10:00:00'),
('Carlos Lima alterou o status da tarefa Refatorar serviços de email de Em andamento para Concluído', 'Em andamento', 'Concluído', 3, 3, '2025-05-02 15:30:00');
