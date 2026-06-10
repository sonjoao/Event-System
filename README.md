# Sistema de Organização de Eventos

Projeto desenvolvido para a disciplina de Fundamentos da Programação, utilizando a linguagem Python.

## Descrição

O Sistema de Organização de Eventos foi criado com o objetivo de auxiliar usuários no planejamento e gerenciamento de eventos. A aplicação permite cadastrar eventos, controlar tarefas, acompanhar orçamentos, visualizar contagens regressivas e receber sugestões personalizadas para melhorar a organização.

O sistema funciona através do terminal e utiliza arquivos de texto para armazenar os dados de forma simples e eficiente.

## Objetivos do Projeto

* Aplicar os conceitos fundamentais de programação.
* Desenvolver um sistema modular utilizando funções e arquivos.
* Utilizar persistência de dados por meio de arquivos `.txt`.
* Implementar tratamento de erros e validação de entradas.
* Simular uma aplicação real de gerenciamento de eventos.

## Tecnologias Utilizadas

* Python 3
* Visual Studio Code
* Git e GitHub
* Arquivos TXT para armazenamento de dados

## Estrutura do Projeto

```text
Projeto-FP/
├── main.py
├── README.md
├── manual_usuario.md
├── .gitignore
├── dados/
│   ├── eventos.txt
│   └── tarefas.txt
└── src/
    ├── arquivos.py
    ├── eventos.py
    ├── tarefas.py
    ├── orcamento.py
    ├── sugestoes.py
    └── extra.py
```

## Funcionalidades

### Gerenciamento de Eventos

* Cadastro de eventos
* Listagem de eventos cadastrados
* Edição de eventos
* Exclusão de eventos
* Validação de datas e horários

### Gerenciamento de Tarefas

* Cadastro de tarefas vinculadas a eventos
* Listagem de tarefas
* Listagem de tarefas por evento
* Marcação de tarefas concluídas
* Exclusão de tarefas

### Controle de Orçamento

* Registro dos custos das tarefas
* Cálculo automático de gastos
* Comparação entre gastos e orçamento disponível
* Exibição do saldo restante

### Contagem Regressiva

* Cálculo automático da quantidade de dias restantes para cada evento.

### Sugestões Personalizadas

* Recomendações baseadas no tipo de evento.
* Sugestões para organização e planejamento.

### Funcionalidades Extras

* Sistema de notificações de eventos próximos.
* Tratamento de exceções para entradas inválidas.
* Armazenamento permanente das informações.

## Armazenamento dos Dados

Os eventos são armazenados no arquivo:

```text
dados/eventos.txt
```

Formato:

```text
id;nome;tipo;data;horario;local;orcamento;convidados
```

Exemplo:

```text
1;Festa Junina;Festa;20/06/2026;18:00;Escola;1500.00;100
```

As tarefas são armazenadas no arquivo:

```text
dados/tarefas.txt
```

Formato:

```text
id_tarefa;id_evento;nome_tarefa;custo;status
```

Exemplo:

```text
1;1;Comprar decoração;150.00;Pendente
```

## Como Executar

### Pré-requisitos

* Python 3 instalado.

### Passos

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Entre na pasta do projeto:

```bash
cd Organia-Festa
```

3. Execute o sistema:

```bash
python main.py
```

Caso necessário:

```bash
python3 main.py
```

## Exemplo de Uso

1. Cadastrar um evento.
2. Definir orçamento disponível.
3. Adicionar tarefas relacionadas ao evento.
4. Marcar tarefas concluídas.
5. Consultar gastos e saldo restante.
6. Verificar a contagem regressiva para o evento.
7. Receber sugestões personalizadas.

## Equipe de Desenvolvimento

| Integrante  | Responsabilidade                                |
| ----------- | ----------------------------------------------- |
| João Marcos | Integração geral, menu principal e documentação |
| Vinícius    | CRUD de eventos                                 |
| Miguel      | Gerenciamento de tarefas                        |
| Luiz        | Orçamento, sugestões e funcionalidades extras   |

## Conceitos Aplicados

* Variáveis
* Estruturas condicionais
* Estruturas de repetição
* Funções
* Manipulação de arquivos
* Modularização
* Tratamento de exceções
* Listas
* Validação de dados
* Organização de projetos em Python

## Melhorias Futuras



Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina de Fundamentos da Programação.
