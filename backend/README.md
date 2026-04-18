# Núcleo API

API base desenvolvida em **Django + Django REST Framework** para servir como núcleo reutilizável de aplicações web e mobile.

Este projeto fornece uma estrutura sólida de autenticação, gerenciamento de usuários e perfil, com documentação automática via Swagger.

---

# Tecnologias Utilizadas

- Python 3.13
- Django 5
- Django REST Framework
- JWT Authentication (SimpleJWT)
- DRF Spectacular (Swagger / OpenAPI)
- Unfold Admin
- SQLite (desenvolvimento)

---

# Estrutura do Projeto

backend/
│
├── apps/
│ ├── core/
│ └── users/
│
├── nucleo/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── media/
├── static/
├── manage.py
└── db.sqlite3


---

# Funcionalidades Implementadas

### Autenticação JWT

| Endpoint | Descrição |
|--------|-----------|
| POST `/api/auth/register/` | Registro de usuário |
| POST `/api/auth/login/` | Login |
| POST `/api/auth/refresh/` | Renovar token |
| POST `/api/auth/verify/` | Verificar token |
| GET `/api/auth/me/` | Retorna usuário logado |
| POST `/api/auth/logout/` | Logout (blacklist refresh token) |

---

### Perfil

| Endpoint | Descrição |
|--------|-----------|
| GET `/api/profile/` | Ver perfil |
| PATCH `/api/profile/` | Atualizar perfil |

---

### Usuários (Admin)

| Endpoint | Descrição |
|--------|-----------|
| GET `/api/users/` | Listar usuários |
| GET `/api/users/{id}/` | Detalhar usuário |
| PATCH `/api/users/{id}/` | Atualizar usuário |
| DELETE `/api/users/{id}/` | Remover usuário |

Apenas usuários **staff/admin** podem acessar.

---

# Documentação da API

Swagger disponível em:

```
http://localhost:8000/api/docs/
```

Schema OpenAPI:

```
http://localhost:8000/api/schema/
```

---

# Instalação

Clone o projeto:

```bash
git clone https://github.com/seuusuario/nucleo-api.git

cd nucleo-api/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver  

http://127.0.0.1:8000