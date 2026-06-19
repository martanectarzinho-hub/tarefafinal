# 🍕 Sistema de Gestão de Restaurante

Aplicação web desenvolvida em Python com a framework Django, para gestão interna de um restaurante (pratos, mesas e pedidos).

---

## 📋 Funcionalidades

- Login e Logout de utilizadores
- Gestão de Pratos (criar, listar, editar, apagar, pesquisar)
- Gestão de Mesas (criar, listar, editar, apagar)
- Gestão de Pedidos (criar, listar, filtrar por estado, editar, apagar)
- Dashboard com resumo geral
- Painel de administração Django

---

## ⚙️ Requisitos

- Python 3.10 ou superior
- pip

---

## 🚀 Instalação e Execução Local

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU_UTILIZADOR/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
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

## 🗄️ Base de Dados

A aplicação utiliza **SQLite** (ficheiro local `db.sqlite3`), não sendo necessária qualquer instalação adicional.

---

## 🔐 Segurança

- Rotas protegidas com `@login_required`
- Validação de dados nos formulários (ex: preços negativos não são permitidos)
- Proteção CSRF em todos os formulários

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Django 6
- SQLite
- Bootstrap 5 (via CDN)