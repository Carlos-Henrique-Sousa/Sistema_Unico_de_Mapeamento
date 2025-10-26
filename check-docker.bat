@echo off
echo ========================================
echo    Verificando Docker e Serviços
echo ========================================

echo.
echo [1/3] Verificando se Docker está rodando...
docker --version
if %errorlevel% neq 0 (
    echo ERRO: Docker não está instalado ou não está no PATH
    pause
    exit /b 1
)

echo.
echo [2/3] Verificando containers ativos...
docker compose ps

echo.
echo [3/3] Testando conectividade...
echo Testando backend...
curl -s http://localhost:8000/api/ > nul
if %errorlevel% equ 0 (
    echo ✓ Backend respondendo
) else (
    echo ✗ Backend não está respondendo
)

echo Testando frontend...
curl -s http://localhost:5173 > nul
if %errorlevel% equ 0 (
    echo ✓ Frontend respondendo
) else (
    echo ✗ Frontend não está respondendo
)

echo.
echo ========================================
echo    Status dos Serviços:
echo ========================================
docker compose ps

echo.
echo Para iniciar os serviços:
echo start-dev.bat
echo.
echo Para ver logs:
echo docker compose logs -f [servico]
echo.

pause
