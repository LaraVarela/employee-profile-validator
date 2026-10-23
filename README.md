# Validador de Perfil Profissional

Projeto de iniciação em Python que valida e apresenta um perfil profissional.

## O que faz

- Limpa espaços extra e organiza maiúsculas e minúsculas.
- Verifica se o nome, o cargo e o departamento foram preenchidos.
- Confirma que a idade é positiva.
- Exige uma biografia entre 20 e 160 caracteres.
- Mostra o perfil apenas quando os dados são válidos.

## Como executar

É necessário ter Python instalado. No terminal, dentro da pasta do projeto, executa:

```bash
python employee_profile_validator.py
```
## Exemplo de resultado

```text
---PERFIL PROFISSIONAL---
Nome: Ana Silva
Cargo: Data Analyst
Departamento: Product Engineering
Idade: 28
Biografia: Analista de dados que transforma informação em decisões úteis para a equipa.
```
## Conceitos praticados

- Variáveis e tipos de dados
- Strings e métodos como `strip()` e `title()`
- Formatação com f-strings
- Condições `if`
- Validação de dados