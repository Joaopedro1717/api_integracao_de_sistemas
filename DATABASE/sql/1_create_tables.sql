CREATE TABLE Equipe (
    Id INT PRIMARY KEY,
    Nome VARCHAR(255)
);

CREATE TABLE Usuarios (
    Id INT PRIMARY KEY,
    Nome VARCHAR(255),
    Email VARCHAR(255),
    Cargo VARCHAR(255),
    Id_Equipe INT,
    FOREIGN KEY (Id_Equipe) REFERENCES Equipe(Id)
);

CREATE TABLE Tarefas (
    Id INT PRIMARY KEY,
    Titulo VARCHAR(255),
    Descricao TEXT,
    Status VARCHAR(50),
    Prazo DATE,
    Id_Equipe INT,
    Id_Usuario_Responsavel INT,
    FOREIGN KEY (Id_Equipe) REFERENCES Equipe(Id),
    FOREIGN KEY (Id_Usuario_Responsavel) REFERENCES Usuarios(Id)
);

CREATE TABLE Andamento (
    Id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Mensagem TEXT,
    Status_antigo VARCHAR(50),
    Status_atual VARCHAR(50),
    Id_Usuario INT,
    Id_Tarefa INT,
    Data_Criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Id_Usuario) REFERENCES Usuarios(Id),
    FOREIGN KEY (Id_Tarefa) REFERENCES Tarefas(Id)
);
