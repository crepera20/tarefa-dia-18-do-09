CREATE DATABASE DBescola;

CREATE TABLE TBl_professores
(
    PRO_codigo INT PRIMARY KEY AUTO_INCREMENT,
    PRO_nome VARCHAR(45),
    PRO_endereco VARCHAR(45),
    PRO_email VARCHAR(45),
    PRO_telefone INT,
    PRO_cpf INT,
    PRO_idade INT
);

CREATE TABLE TBl_alunos
(
    ALU_codigo INT PRIMARY KEY AUTO_INCREMENT,
    ALU_nome VARCHAR(45),
    ALU_endereco VARCHAR(45),
    ALU_email VARCHAR(45),
    ALU_telefone INT,
    ALU_idade INT
);

CREATE TABLE TBl_cidades
(
    CID_codigo INT PRIMARY KEY AUTO_INCREMENT,
    CID_nome VARCHAR(45),
    CID_uf VARCHAR(2)
);

CREATE TABLE TBl_cursos
(
    COD_codigo INT PRIMARY KEY AUTO_INCREMENT,
    COD_nome VARCHAR(45),
    COD_valor VARCHAR(6)
);

CREATE TABLE TBl_usuarios
(
    USU_codigo INT PRIMARY KEY AUTO_INCREMENT,
    USU_nome VARCHAR(45),
    USU_username VARCHAR(20),
    USU_senha INT
);

ALTER TABLE TBl_professores
ADD COLUMN CID_codigo INT,
ADD CONSTRAINT fk_cidad_codigo FOREIGN KEY (CID_codigo) REFERENCES TBl_cidades(CID_codigo);

ALTER TABLE TBl_alunos
ADD COLUMN CID_codigo INT,
ADD CONSTRAINT fk_cidad2_codigo FOREIGN KEY (CID_codigo) REFERENCES TBl_cidades(CID_codigo);

ALTER TABLE TBl_alunos
ADD COLUMN CUR_codigo INT,
ADD CONSTRAINT fk_curso_codigo FOREIGN KEY (CUR_codigo) REFERENCES TBl_cursos(COD_codigo);

INSERT INTO TBl_usuarios (USU_nome, USU_username, USU_senha)
VALUES ('a', 'renata_user', '1');