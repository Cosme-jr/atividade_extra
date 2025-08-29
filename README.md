# Projeto Python - Fundamentos de Programação

Este repositório contém 4 programas básicos em Python que demonstram conceitos fundamentais de programação.

## 📋 Índice

1. [Calculadora Básica](#1-calculadora-básica)
2. [Sistema de Notas](#2-sistema-de-notas)
3. [Verificador de Senhas](#3-verificador-de-senhas)
4. [Analisador de Números](#4-analisador-de-números)

## 🚀 Como Executar

Certifique-se de ter Python 3.6 ou superior instalado em seu sistema.

```bash
# Clone o repositório
git clone [url-do-repositório]

# Entre na pasta do projeto
cd projeto-python-basico

# Execute qualquer um dos arquivos
python calculadora.py
python sistema_notas.py
python verificador_senha.py
python analisador_numeros.py
```

## 1. Calculadora Básica

**Arquivo:** `calculadora.py`

### Descrição
Uma calculadora simples que realiza as quatro operações matemáticas básicas: adição (+), subtração (-), multiplicação (*) e divisão (/).

### Funcionalidades
- ✅ Adição de dois números
- ✅ Subtração de dois números
- ✅ Multiplicação de dois números
- ✅ Divisão de dois números (com tratamento de divisão por zero)
- ✅ Interface simples via linha de comando

### Como usar
```bash
python calculadora.py
```

### Exemplo de uso
```
=== CALCULADORA BÁSICA ===
Digite o primeiro número: 10
Digite o segundo número: 5
Escolha a operação (+, -, *, /): *
Resultado: 10.0 * 5.0 = 50.0
```

---

## 2. Sistema de Notas

**Arquivo:** `sistema_notas.py`

### Descrição
Sistema para registrar notas de alunos e calcular automaticamente a média da turma.

### Funcionalidades
- ✅ Registro de nomes dos alunos
- ✅ Registro de notas individuais
- ✅ Cálculo da média da turma
- ✅ Exibição de relatório completo

### Como usar
```bash
python sistema_notas.py
```

### Exemplo de uso
```
=== SISTEMA DE NOTAS ===
Quantos alunos há na turma? 3
Nome do aluno 1: João
Nota do João: 8.5
Nome do aluno 2: Maria
Nota da Maria: 9.0
Nome do aluno 3: Pedro
Nota do Pedro: 7.5

=== RELATÓRIO DA TURMA ===
João: 8.5
Maria: 9.0
Pedro: 7.5
Média da turma: 8.33
```

---

## 3. Verificador de Senhas

**Arquivo:** `verificador_senha.py`

### Descrição
Sistema que verifica se uma senha atende aos critérios básicos de segurança.

### Critérios de Segurança
- ✅ Deve ter pelo menos 8 caracteres
- ✅ Deve conter pelo menos um número
- ✅ Feedback detalhado sobre cada critério

### Como usar
```bash
python verificador_senha.py
```

### Exemplo de uso
```
=== VERIFICADOR DE SENHAS ===
Digite uma senha para verificar: minhasenha123

✅ Critérios atendidos:
- Tem pelo menos 8 caracteres
- Contém pelo menos um número

🎉 Senha APROVADA! Atende a todos os critérios de segurança.
```

---

## 4. Analisador de Números

**Arquivo:** `analisador_numeros.py`

### Descrição
Programa que analisa números digitados pelo usuário, classificando-os como pares ou ímpares e mantendo um contador de cada tipo.

### Funcionalidades
- ✅ Classificação de números como pares ou ímpares
- ✅ Contador de números pares
- ✅ Contador de números ímpares
- ✅ Relatório final com estatísticas

### Como usar
```bash
python analisador_numeros.py
```

### Exemplo de uso
```
=== ANALISADOR DE NÚMEROS ===
Digite números para análise (0 para parar):
Digite um número: 4
4 é PAR

Digite um número: 7
7 é ÍMPAR

Digite um número: 0

=== RELATÓRIO FINAL ===
Total de números analisados: 2
Números pares: 1
Números ímpares: 1
```

## 🛠️ Estrutura do Projeto

```
projeto-python-basico/
│
├── README.md
├── calculadora.py
├── sistema_notas.py
├── verificador_senha.py
└── analisador_numeros.py
```

## 📚 Conceitos Demonstrados

Este projeto demonstra os seguintes conceitos de programação:

- **Entrada e saída de dados** (`input()` e `print()`)
- **Variáveis e tipos de dados** (int, float, string)
- **Operadores matemáticos** (+, -, *, /)
- **Estruturas condicionais** (`if`, `elif`, `else`)
- **Loops** (`while`, `for`)
- **Listas** para armazenar dados
- **Funções** para organizar código
- **Tratamento de exceções** (try/except)
- **Validação de entrada**

## 🎯 Objetivos de Aprendizado

Após completar este projeto, você será capaz de:

1. Criar programas interativos com entrada do usuário
2. Implementar validações básicas de dados
3. Trabalhar com estruturas de controle de fluxo
4. Organizar dados em listas e processá-los
5. Criar interfaces simples via linha de comando

## 💡 Sugestões de Melhorias

Para expandir este projeto, considere adicionar:

- Interface gráfica usando `tkinter`
- Salvamento de dados em arquivos
- Validações mais robustas
- Menu principal para escolher entre os programas
- Testes unitários
- Documentação com `docstrings`

## 📞 Suporte

Se encontrar algum problema ou tiver dúvidas sobre o código, verifique:

1. Se o Python está instalado corretamente
2. Se está executando os arquivos na pasta correta
3. Se está seguindo as instruções de entrada exatamente como mostrado

## 📄 Licença

Este projeto é livre para uso educacional.

---

**Desenvolvido como material de estudo para fundamentos de Python** 🐍
