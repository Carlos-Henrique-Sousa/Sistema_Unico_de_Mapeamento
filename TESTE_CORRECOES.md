# 🧪 Guia de Testes - S.U.M

## ✅ Correções Implementadas

### 🔧 Backend (Django)
- **Modelos corrigidos**: Campo `tipo` → `user_type` em todos os modelos
- **CORS configurado**: Suporte para portas 5173 e 8080
- **URLs organizadas**: Removidas duplicações e organizadas hierarquicamente
- **Autenticação JWT**: Configurada corretamente com refresh tokens
- **Logout melhorado**: Funciona sem token válido
- **Banco de dados**: Configuração otimizada para SQLite/PostgreSQL

### 🎨 Frontend (Vue.js)
- **Proxy configurado**: Aponta para `backend:8000` no Docker
- **Dockerfile otimizado**: Inclui dependências de desenvolvimento
- **Vite configurado**: Host 0.0.0.0 para Docker

### 🐳 Docker & Integração
- **Docker Compose**: Configuração simplificada e funcional
- **Nginx**: Proxy reverso configurado corretamente
- **Scripts de teste**: Automatizados para Linux/Mac e Windows
- **Variáveis de ambiente**: Configuradas com valores padrão

## 🚀 Como Testar

### 1. **Teste Automático**
```bash
# Linux/Mac
./test_integration.sh

# Windows
test_integration.bat
```

### 2. **Teste Manual**
```bash
# Iniciar serviços
docker-compose up --build

# Testar endpoints
curl http://localhost:8000/api/health/
curl http://localhost:5173/
curl http://localhost/
```

### 3. **Verificar Logs**
```bash
# Todos os serviços
docker-compose logs -f

# Serviço específico
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f nginx
```

## 🔍 Endpoints de Teste

- **Health Check**: `GET /api/health/`
- **API Info**: `GET /api/info/`
- **Admin**: `http://localhost:8000/admin/`
- **Frontend**: `http://localhost:5173/`
- **Nginx**: `http://localhost/`

## 🐛 Troubleshooting

### Backend não responde
```bash
# Verificar logs
docker-compose logs backend

# Reiniciar backend
docker-compose restart backend
```

### Frontend não carrega
```bash
# Verificar logs
docker-compose logs frontend

# Reinstalar dependências
docker-compose exec frontend npm install
```

### Banco de dados com problemas
```bash
# Verificar conexão
docker-compose exec backend python manage.py dbshell

# Executar migrações
docker-compose exec backend python manage.py migrate
```

## 📊 Status Esperado

Após executar `docker-compose up --build`:

- ✅ **PostgreSQL**: Rodando na porta 5432
- ✅ **Backend**: Rodando na porta 8000
- ✅ **Frontend**: Rodando na porta 5173
- ✅ **Nginx**: Rodando na porta 80

Todos os serviços devem estar saudáveis e comunicando entre si!
