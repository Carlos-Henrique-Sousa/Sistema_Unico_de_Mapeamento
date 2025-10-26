@echo off
echo ========================================
echo    S.U.M - Sistema Unico de Mapeamento
echo    Inicializacao Completa do Sistema
echo ========================================

echo.
echo [1/6] Verificando Docker...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Docker nao esta instalado ou nao esta no PATH
    echo Por favor, instale o Docker Desktop e tente novamente
    pause
    exit /b 1
)
echo ✓ Docker encontrado

echo.
echo [2/6] Parando containers existentes...
docker compose down >nul 2>&1

echo.
echo [3/6] Removendo containers e imagens antigas...
docker compose rm -f >nul 2>&1
docker system prune -f >nul 2>&1

echo.
echo [4/6] Construindo imagens (isso pode demorar alguns minutos)...
echo Construindo Backend...
docker compose build backend --no-cache
if %errorlevel% neq 0 (
    echo ERRO: Falha ao construir backend
    pause
    exit /b 1
)

echo Construindo Frontend...
docker compose build frontend --no-cache
if %errorlevel% neq 0 (
    echo ERRO: Falha ao construir frontend
    pause
    exit /b 1
)

echo.
echo [5/6] Iniciando servicos...
docker compose up -d
if %errorlevel% neq 0 (
    echo ERRO: Falha ao iniciar servicos
    pause
    exit /b 1
)

echo.
echo [6/6] Aguardando servicos iniciarem...
echo Aguarde 30 segundos para os servicos ficarem prontos...
timeout /t 30 /nobreak > nul

echo.
echo ========================================
echo    Verificando Status dos Servicos
echo ========================================

echo.
echo Testando Backend...
curl -s http://localhost:8000/api/health/ >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Backend: FUNCIONANDO
) else (
    echo ✗ Backend: COM PROBLEMAS
)

echo Testando Frontend...
curl -s http://localhost:5173 >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Frontend: FUNCIONANDO
) else (
    echo ✗ Frontend: COM PROBLEMAS
)

echo Testando Nginx...
curl -s http://localhost/api/health/ >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Nginx: FUNCIONANDO
) else (
    echo ✗ Nginx: COM PROBLEMAS
)

echo.
echo ========================================
echo    Servicos Disponiveis:
echo ========================================
echo - Frontend: http://localhost:5173
echo - Backend:  http://localhost:8000
echo - Nginx:    http://localhost
echo - Admin:    http://localhost/admin
echo - Status:   http://localhost/admin/status
echo ========================================

echo.
echo Para ver os logs em tempo real:
echo docker compose logs -f
echo.
echo Para parar os servicos:
echo docker compose down
echo.

echo Pressione qualquer tecla para abrir o sistema no navegador...
pause >nul

echo Abrindo sistema no navegador...
start http://localhost

echo.
echo Sistema iniciado com sucesso!
echo Acesse http://localhost para usar o S.U.M
echo.
pause
