#!/bin/bash
# Script de teste de integração S.U.M

echo "🚀 Testando integração S.U.M..."

# Verificar se Docker está rodando
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker não está rodando. Por favor, inicie o Docker primeiro."
    exit 1
fi

# Parar containers existentes
echo "🛑 Parando containers existentes..."
docker-compose down

# Construir e iniciar containers
echo "🔨 Construindo e iniciando containers..."
docker-compose up --build -d

# Aguardar serviços iniciarem
echo "⏳ Aguardando serviços iniciarem..."
sleep 30

# Testar backend
echo "🔍 Testando backend..."
BACKEND_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/api/health/)
if [ "$BACKEND_STATUS" = "200" ]; then
    echo "✅ Backend funcionando!"
else
    echo "❌ Backend com problemas (Status: $BACKEND_STATUS)"
fi

# Testar frontend
echo "🔍 Testando frontend..."
FRONTEND_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5173/)
if [ "$FRONTEND_STATUS" = "200" ]; then
    echo "✅ Frontend funcionando!"
else
    echo "❌ Frontend com problemas (Status: $FRONTEND_STATUS)"
fi

# Testar nginx
echo "🔍 Testando nginx..."
NGINX_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost/)
if [ "$NGINX_STATUS" = "200" ]; then
    echo "✅ Nginx funcionando!"
else
    echo "❌ Nginx com problemas (Status: $NGINX_STATUS)"
fi

echo ""
echo "📊 Status dos serviços:"
echo "Backend: http://localhost:8000/api/health/"
echo "Frontend: http://localhost:5173/"
echo "Nginx: http://localhost/"
echo ""
echo "📝 Para ver logs: docker-compose logs -f"
echo "🛑 Para parar: docker-compose down"
