@echo off
echo ========================================
echo    S.U.M - Diagnostico do Sistema
echo ========================================

echo.
echo [1/8] Verificando Docker...
docker --version
if %errorlevel% neq 0 (
    echo ERRO: Docker nao encontrado
    goto :end
)
echo ✓ Docker OK

echo.
echo [2/8] Verificando containers...
docker compose ps

echo.
echo [3/8] Verificando logs do Backend...
echo --- Logs do Backend (ultimas 10 linhas) ---
docker compose logs --tail=10 backend

echo.
echo [4/8] Verificando logs do Frontend...
echo --- Logs do Frontend (ultimas 10 linhas) ---
docker compose logs --tail=10 frontend

echo.
echo [5/8] Verificando logs do Nginx...
echo --- Logs do Nginx (ultimas 10 linhas) ---
docker compose logs --tail=10 nginx

echo.
echo [6/8] Testando conectividade...
echo Testando Backend (porta 8000)...
curl -s -w "Status: %%{http_code}, Tempo: %%{time_total}s\n" http://localhost:8000/api/health/ 2>nul || echo ERRO: Backend nao responde

echo Testando Frontend (porta 5173)...
curl -s -w "Status: %%{http_code}, Tempo: %%{time_total}s\n" http://localhost:5173 2>nul || echo ERRO: Frontend nao responde

echo Testando Nginx (porta 80)...
curl -s -w "Status: %%{http_code}, Tempo: %%{time_total}s\n" http://localhost/api/health/ 2>nul || echo ERRO: Nginx nao responde

echo.
echo [7/8] Verificando uso de recursos...
echo --- Uso de CPU e Memoria ---
docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"

echo.
echo [8/8] Verificando portas em uso...
echo --- Portas em uso ---
netstat -an | findstr ":80\|:5173\|:8000\|:5432"

:end
echo.
echo ========================================
echo    Diagnostico Concluido
echo ========================================
echo.
echo Se houver problemas:
echo 1. Execute: start-system.bat
echo 2. Verifique os logs: docker compose logs -f
echo 3. Reinicie o Docker Desktop
echo.
pause
