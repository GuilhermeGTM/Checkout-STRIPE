#  Checkout com STRIPE

# 📌 Sobre o Projeto
Este projeto é uma aplicação **Django** integrada com a **Stripe API** para processamento de pagamentos online.  
Ele permite que usuários realizem compras de produtos cadastrados, confirmem pagamentos com cartão de crédito e recebam notificações de sucesso ou erro.  
Além disso, o sistema registra pedidos no banco de dados e possibilita reembolsos diretamente pelo painel administrativo do Django.

---
  

## Layout web
![Web 1](https://github.com/GuilhermeGTM/Checkout-STRIPE/blob/main/git/2.png)

![Web 1](https://github.com/GuilhermeGTM/Checkout-STRIPE/blob/main/git/1.png)

![Web 1](https://github.com/GuilhermeGTM/Checkout-STRIPE/blob/main/git/3.png)

---

# ⚙️ Tecnologias Utilizadas
- **Python 3**
- **Django** (framework web)
- **Stripe API** (integração de pagamentos)
- **HTML / CSS / JavaScript** (frontend com Stripe Elements)

---

## DB
- SQLite3

---

## 🚀 Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| Cadastro e exibição de produtos | Permite cadastrar produtos e exibi-los na aplicação. |
| Criação de **PaymentIntent** | Gera um PaymentIntent no Stripe com valor e metadados do cliente. |
| Formulário de checkout | Usa Stripe Elements para capturar dados do cartão de forma segura. |
| Webhook Stripe | Recebe notificações de eventos do Stripe (ex.: `charge.succeeded`). |
| Registro de pedidos | Salva pedidos no banco de dados com status e valor pago. |
| Reembolso no Admin | Ação personalizada no Django Admin para reembolsar clientes via Stripe. |
| Feedback visual | Exibe mensagens de sucesso/erro e spinner de carregamento para o usuário. |


---

# Como executar o projeto

```bash
instalar o venv na pasta do projeto
--->python -m venv .venv
ativando venv
--->.\.venv\Scripts\Activate
baixando as dependencias
--->python -m pip install -r requirements.txt
--->python manage.py migrate
-->python manage.py runserver
Configurar as chaves no settings
```

---

# Autor

Guilherme Timm Moreira

