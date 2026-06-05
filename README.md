# 🏦 Conta Corrente

Projeto desenvolvido durante a graduação na disciplina de **Computação 2**, explorando **Programação Orientada a Objetos (POO)**, **exceções personalizadas** e a biblioteca gráfica **Tkinter** do Python.

## 💡 Sobre o projeto

Simulação de uma conta corrente bancária com interface gráfica. O usuário pode criar uma conta informando nome e limite, realizar depósitos e saques, e acompanhar o saldo em tempo real.

## 🖥️ Funcionalidades

- Criação de conta com nome e limite personalizados
- Depósito e saque com validação de valores
- Exibição de saldo, limite e data de criação da conta
- Tratamento de erros com mensagens amigáveis ao usuário

## 🧠 Conceitos aplicados

- **POO**: classes `ContaCorrente` e `InterfaceContaCorrente` com responsabilidades separadas
- **Encapsulamento**: atributos privados (`__saldo`, `__limite`, `__nome`) protegidos por métodos
- **Exceções personalizadas**: `ValorNegativoError` e `SaldoInsuficienteError` para tratamento semântico de erros
- **Tkinter**: uso de `Entry`, `Label`, `Button`, `grid layout` e `messagebox`

## 🚀 Como executar

**Pré-requisitos:** Python 3.x instalado (o Tkinter já vem incluído).

```bash
# Clone o repositório
git clone https://github.com/nubiamneves/nome-do-repositorio.git

# Entre na pasta
cd nome-do-repositorio

# Execute o programa
python banco.py
```

## 🗂️ Estrutura do projeto

```
conta-corrente/
└── banco.py   # Código principal com a lógica da conta e a interface gráfica
```

## 🛠️ Tecnologias

- Python 3
- Tkinter
- datetime
