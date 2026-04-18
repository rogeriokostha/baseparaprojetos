param (
    [Parameter(Position=0, Mandatory=$true)]
    [string]$Command,
    
    [Parameter(ValueFromRemainingArguments=$true)]
    $RestArgs
)

# Verifica se existe um .env na raiz contendo o nome do projeto (para isolamento dos containers)
if (-Not (Test-Path -Path ".\.env")) {
    Write-Host ""
    Write-Host "========== CONFIGURAÇÃO DE ISOLAMENTO ==========" -ForegroundColor Cyan
    Write-Host "Para evitar conflito de containers com outros projetos usando este mesmo boilerplate," -ForegroundColor Yellow
    $ProjectName = Read-Host "Digite o NOME DESTE PROJETO, sem espaços (ex: meunovo_projeto)"
    if ([string]::IsNullOrWhiteSpace($ProjectName)) { 
        $ProjectName = "dev_imortal" 
    }
    
    # Cria o .env na raiz que o Docker Compose lê por padrão
    Set-Content -Path ".\.env" -Value "PROJECT_NAME=$ProjectName`nCOMPOSE_PROJECT_NAME=$ProjectName"
    Write-Host "=> Arquivo .env gerado na raiz com PROJECT_NAME=$ProjectName" -ForegroundColor Gray
    Write-Host "================================================" -ForegroundColor Cyan
    Write-Host ""
}

switch ($Command) {
    "up" { 
        Write-Host "Iniciando os containers..." -ForegroundColor Green
        docker-compose up -d 
    }
    "down" { 
        Write-Host "Derrubando a infraestrutura..." -ForegroundColor Yellow
        docker-compose down 
    }
    "build" { 
        Write-Host "Reconstruindo as imagens..." -ForegroundColor Cyan
        docker-compose build 
    }
    "setup" {
        Write-Host "Iniciando setup incial do Boilerplate Dev-Imortal..." -ForegroundColor Green

        # Setup de Arquivos Base (.env)
        Write-Host "Configurando variáveis e senhas locas..." -ForegroundColor Cyan
        if (-Not (Test-Path -Path "backend\.env")) {
            Copy-Item -Path ".\.env.example" -Destination "backend\.env"
            Write-Host " => Arquivo backend\.env gerado." -ForegroundColor Gray
        }
        if (-Not (Test-Path -Path "frontend\.env.local")) {
            Copy-Item -Path ".\.env.example" -Destination "frontend\.env.local"
            Write-Host " => Arquivo frontend\.env.local gerado." -ForegroundColor Gray
        }

        Write-Host "Configurando ambiente Virtual Python Local (venv) para a IDE..." -ForegroundColor Cyan
        if (-Not (Test-Path -Path "venv")) {
            python -m venv venv
            Write-Host " => pasta venv criada na raiz." -ForegroundColor Gray
        }
        Write-Host " => Instalando pacotes locais no venv (isso pode levar uns segundos)..." -ForegroundColor Gray
        .\venv\Scripts\python.exe -m pip install --quiet --upgrade pip
        .\venv\Scripts\python.exe -m pip install --quiet -r backend\requirements.txt

        Write-Host "Iniciando Banco, Cache e Servidor Backend..." -ForegroundColor Green
        docker-compose up -d
        Write-Host "Esperando Instalação do Container (5 segundos)..." -ForegroundColor Yellow
        Start-Sleep -Seconds 5

        Write-Host "Aplicando migrações no banco de dados..." -ForegroundColor Green
        docker-compose exec backend python manage.py migrate
        
        Write-Host "Configurando Frontend e seu ecossistema Node..." -ForegroundColor Cyan
        Push-Location .\frontend
        npm install
        Pop-Location

        Write-Host ""
        Write-Host "✅ Setup finalizado com sucesso! Seu boilerplate está pronto para a guerra!" -ForegroundColor Green
        Write-Host "Para acessar o front-end, crie outro terminal, entre em 'cd frontend' e rode 'npm run dev'." -ForegroundColor Yellow
    }
    "migrate" { 
        Write-Host "Aplicando migrações na API e Banco de Dados..." -ForegroundColor Green
        docker-compose exec backend python manage.py migrate 
    }
    "migrations" { 
        Write-Host "Gerando novos arquivos de migração (makemigrations)..." -ForegroundColor Cyan
        docker-compose exec backend python manage.py makemigrations 
    }
    "superuser" { 
        Write-Host "Criador de Super Usuário (Painel Admin Unfold)" -ForegroundColor Magenta
        docker-compose exec backend python manage.py createsuperuser 
    }
    "shell" { 
        Write-Host "Abrindo Shell Iterativo do Django" -ForegroundColor Green
        docker-compose exec backend python manage.py shell 
    }
    "bash" { 
        Write-Host "Entrando dentro do Container da API" -ForegroundColor Yellow
        docker-compose exec backend bash 
    }
    "logs" {
        docker-compose logs -f backend
    }
    default { 
        # Se for um comando genérico do manage.py, repassa direto
        $argsStr = $RestArgs -join ' '
        docker-compose exec backend python manage.py $Command $argsStr
    }
}
