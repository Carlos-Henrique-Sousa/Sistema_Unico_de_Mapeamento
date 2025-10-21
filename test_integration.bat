@echo off
REM Script de teste de integração S.U.M para Windows

echo 🚀 Testando integração S.U.M...

REM Verificar se Docker está rodando
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker não está rodando. Por favor, inicie o Docker primeiro.
    pause
    exit /b 1
)

REM Parar containers existentes
echo 🛑 Parando containers existentes...
docker-compose down

REM Construir e iniciar containers
echo 🔨 Construindo e iniciando containers...
docker-compose up --build -d

REM Aguardar serviços iniciarem
echo ⏳ Aguardando serviços iniciarem...
timeout /t 30 /nobreak >nul

REM Testar backend
echo 🔍 Testando backend...
curl -s -o nul -w "%%{http_code}" http://localhost:8000/api/health/ > temp_backend.txt
set /p BACKEND_STATUS=<temp_backend.txt
del temp_backend.txt

if "%BACKEND_STATUS%"=="200" (
    echo ✅ Backend funcionando!
) else (
    echo ❌ Backend com problemas (Status: %BACKEND_STATUS%)
)

REM Testar frontend
echo 🔍 Testando frontend...
curl -s -o nul -w "%%{http_code}" http://localhost:5173/ > temp_frontend.txt
set /p FRONTEND_STATUS=<temp_frontend.txt
del temp_frontend.txt

if "%FRONTEND_STATUS%"=="200" (
    echo ✅ Frontend funcionando!
) else (
    echo ❌ Frontend com problemas (Status: %FRONTEND_STATUS%)
)

REM Testar nginx
echo 🔍 Testando nginx...
curl -s -o nul -w "%%{http_code}" http://localhost/ > temp_nginx.txt
set /p NGINX_STATUS=<temp_nginx.txt
del temp_nginx.txt

if "%NGINX_STATUS%"=="200" (
    echo ✅ Nginx funcionando!
) else (
    echo ❌ Nginx com problemas (Status: %NGINX_STATUS%)
)

echo.
echo 📊 Status dos serviços:
echo Backend: http://localhost:8000/api/health/
echo Frontend: http://localhost:5173/
echo Nginx: http://localhost/
echo.
echo 📝 Para ver logs: docker-compose logs -f
echo 🛑 Para parar: docker-compose down
echo.
pause
