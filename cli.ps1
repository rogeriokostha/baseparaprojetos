param (
    [Parameter(Position=0, Mandatory=$true)]
    [string]$Command,
    
    [Parameter(ValueFromRemainingArguments=$true)]
    $RestArgs
)

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
