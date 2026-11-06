modelagem = '''
CREATE TABLE vendas_produtos (
    id_venda BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    data_venda TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    numero_pedido VARCHAR(30) NOT NULL,
    nome_cliente VARCHAR(150) NOT NULL,
    produto VARCHAR(150) NOT NULL,
    categoria VARCHAR(100),
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    valor_unitario NUMERIC(12,2) NOT NULL CHECK (valor_unitario >= 0),
    desconto NUMERIC(12,2) NOT NULL DEFAULT 0 CHECK (desconto >= 0),
    valor_total NUMERIC(12,2)
        GENERATED ALWAYS AS (
            (quantidade * valor_unitario) - desconto
        ) STORED,
    forma_pagamento VARCHAR(50),
    status_venda VARCHAR(30) DEFAULT 'Concluída'
);'''

instrucao = f"""
Você é um especialista em SQL e PostgreSQL.
Com base na modelagem abaixo, gere apenas uma consulta SQL SELECT.
Não explique nada.
Não use Markdown.
Não use ```sql.
Não gere INSERT, UPDATE, DELETE, DROP, ALTER ou TRUNCATE.
Use aspas duplas nos nomes de tabelas e colunas, exatamente como estão na modelagem (minúsculas).
Em filtros de texto no WHERE, compare ignorando maiúsculas e minúsculas, usando UPPER() nos dois lados.
Use somente a tabela e as colunas da modelagem abaixo.

MODELAGEM:
{modelagem}

PERGUNTA DO USUÁRIO:
"""