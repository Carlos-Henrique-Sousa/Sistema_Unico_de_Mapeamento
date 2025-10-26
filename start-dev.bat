@echo off
echo ========================================
echo    S.U.M - Sistema Unico de Mapeamento
echo    Iniciando ambiente de desenvolvimento
echo ========================================

echo.
echo [1/4] Parando containers existentes...
docker compose down

echo.
echo [2/4] Removendo containers antigos...
docker compose rm -f

echo.
echo [3/4] Construindo imagens...
docker compose build --no-cache

echo.
echo [4/4] Iniciando serviços...
docker compose up -d

echo.
echo ========================================
echo    Serviços iniciados:
echo    - Frontend: http://localhost:5173
echo    - Backend:  http://localhost:8000
echo    - Nginx:    http://localhost:80
echo ========================================

echo.
echo Aguardando serviços iniciarem...
timeout /t 10 /nobreak > nul

echo.
echo Verificando status dos containers:
docker compose ps

echo.
echo Para ver os logs em tempo real:
echo docker compose logs -f
echo.
echo Para parar os serviços:
echo docker compose down
echo.

pause
