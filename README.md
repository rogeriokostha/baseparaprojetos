# 🚀 Dev-Imortal — Boilerplate Corporativo Fullstack

Bem-vindo ao **Boilerplate Dev-Imortal**! Este não é apenas um template, mas um ecossistema pronto para produção pensado para iniciar novos produtos escaláveis instantaneamente com forte ênfase em **arquitetura, segurança e padronização**.

A estrutura adota o padrão **Monorepo** com comunicação por REST, unindo Django na infraestrutura de dados (Backend) acoplado intimamente a um frontend em React moderno (Next.js).

---

## 🛠 Tecnologias Embarcadas

**Backend:**
* [Django 5+](https://www.djangoproject.com/) — Robusto núcleo do servidor.
* [Django REST Framework](https://www.django-rest-framework.org/) — Interface padrão para a rede HTTP.
* [JWT e DRF Spectacular] — Autenticação blindada e design em Swagger automático.
* **Infra**: PostgreSQL (base global) e Redis (cache primário rápido e background tasks).
* **Qualidade**: Linting ativo via pacote moderno `Ruff` acelerado em Rust.

**Frontend:**
* [Next.js 15+](https://nextjs.org/) — Roteamento pelo diretório `/app`.
* Integração JWT assíncrona baseada por Actions ou Middleware para proteção de sessão.
* Base UI já conectada e performática. 

---

## 🏗 Estrutura do Sistema

```text
/
├── backend/          -> Diretório isolado do núcleo Python e API do Django.
├── frontend/         -> Ambiente puro Node.js em SPA / SSR e consumo de React.
├── cli.ps1           -> Poderoso Wrapper utilitário que substitui dezenas de linhas de comando para instanciar a aplicação.
└── docker-compose.yml-> Gerenciador de provisionamento local e produtivo de serviços de Infra via Containers.
```

---

## ⚙️ Começando Imediatamente (Modo Rápido usando Script `cli.ps1`)

Este projeto abstrai todas as complicações iniciais com contêineres e instalações utilizando um _wrapper script_ incluído na pasta base **PowerShell** `cli.ps1`. 

### Pré-requisitos Requeridos:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) rodando ativamente.
- Node.js (v18.x ou superior) + pnpm / npm local para dev no Front.

### 1️⃣ Inicialização Total e Mágica (`setup`)
O comando setup copiará os `.env` exigidos pelo projeto local, fará o build do banco com as tabelas pré-prontas do painel admin unificado, levantará Docker, aplicará migrações de SQL e instalará todas as bibliotecas necessárias para o Node no frontend:

```powershell
.\cli.ps1 setup
```

### 2️⃣ Gerando seu Superusuário (Painel Unfold Django)
Para testar seu painel administrativo backend instantaneamente, rode:

```powershell
.\cli.ps1 superuser
```

### 3️⃣ Subindo a Experiência Frontend Completa em Dev (Local Server)
Geralmente o desenvolvimento em React exige resposta nativa ao compilador para "Hot Reload" ágil, portanto mantemos seu acesso local (pelo Node) em vez do Docker, apenas digite:

```powershell
cd frontend
npm run dev
```

Pronto 🎉! Acesse a interface unificada pelas seguintes portas:

* **Aplicação Pública Frontend**: [http://localhost:3000](http://localhost:3000)
* **Status da API e Rotas de Back**: [http://localhost:8000/api](http://localhost:8000/api) 
* **Documentação Viva em Swagger:** [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/) 

---

## 🛑 Outros Comandos Úteis do Wrapper CLI

Gerencie o uso diário somente usando o helper na raiz (`cli.ps1`):
* `.\cli.ps1 up` — Dá a partida regular no servidor já existente sem reinstalar nada.
* `.\cli.ps1 down` — Para a aplicação global e seus sub-processos do Compose.
* `.\cli.ps1 migrations` — Para mapear mudanças de modelo do py e transferir.
* `.\cli.ps1 migrate` — Envia pro banco as migrações mais ativas gravadas em arquivo.
* `.\cli.ps1 bash` —  Acessar internamente como bash root o app principal python.
* `.\cli.ps1 logs` — Monitorar acesso em cauda do seu Nginx/Django.

*(Qualquer outro comando injetará nativamente no `manage.py` de seu docker. Ex: `.\cli.ps1 runserver`).*

---

> _Tão eterno quanto a ideia original. Boilerplate desenvolvido pelo sistema base corporativa RoGeRio CoSTa._
