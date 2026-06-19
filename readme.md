# 🍕 Sistema de Gestão de Restaurante

Aplicação web desenvolvida em Python com a framework **Django**, para gestão interna de um restaurante. Permite gerir pratos, mesas e pedidos de forma simples e intuitiva, com autenticação de utilizadores e painel de administração.

---

## 📸 Funcionalidades

| Módulo | Operações |
|--------|-----------|
| 🍽️ Pratos | Criar, listar, pesquisar, editar, apagar, ver detalhe |
| 🪑 Mesas | Criar, listar, editar, apagar |
| 📋 Pedidos | Criar, listar, filtrar por estado, editar, apagar, ver detalhe |
| 📊 Dashboard | Resumo geral com últimos pedidos e ações rápidas |
| 🔐 Autenticação | Login, Logout, rotas protegidas |
| ⚙️ Admin | Painel de administração Django (apenas para staff) |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Django 6**
- **SQLite** (base de dados local)
- **Bootstrap 5** (via CDN)
- **Bootstrap Icons** (via CDN)

---

## ⚙️ Requisitos

- Python 3.10 ou superior
- pip
- Git

---

## 🚀 Instalação e Execução Local

### 1. Clonar o repositório
```bash
git clone https://github.com/martanectarzinho-hub/tarefafinal.git
cd tarefafinal
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Aplicar as migrações
```bash
python manage.py migrate
```

### 5. Criar utilizador administrador
```bash
python manage.py createsuperuser
```

### 6. Iniciar o servidor
```bash
python manage.py runserver
```

Acede a **http://127.0.0.1:8000** no browser.

---

## 🗄️ Modelos de Dados

- **Categoria** — categorias dos pratos (ex: Entradas, Sobremesas)
- **Prato** — nome, descrição, preço e categoria (`ForeignKey`)
- **Mesa** — número e capacidade
- **Pedido** — mesa, pratos e estado (`ForeignKey` + `ManyToManyField`)

---

## 🔐 Segurança

- Rotas protegidas com `@login_required`
- Validação de dados no backend (ex: preços negativos não são permitidos)
- Proteção CSRF em todos os formulários
- Painel de administração restrito a utilizadores staff

---

## 👥 Autores

Github: https://github.com/martanectarzinho-hub/tarefafinal

Desenvolvido no âmbito do MODULO **AID06**.
