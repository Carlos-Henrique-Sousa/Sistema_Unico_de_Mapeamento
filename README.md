# S.U.M - Sistema Unificado de Mapeamento

Uma plataforma educacional inovadora para mapeamento inteligente de salas de aula, desenvolvida com Django (backend) e Vue.js (frontend).

## 🚀 Início Rápido

### 🐳 Configuração com Docker (Recomendado)

```bash
# Clone o repositório
git clone <seu-repositorio>
cd S.U.M/Sistema_Unico_de_Mapeamento

# Iniciar todos os serviços
docker-compose up --build

# Ou usar o script de teste automático
# Linux/Mac: ./test_integration.sh
# Windows: test_integration.bat
```

### 🔧 Configuração Manual (Desenvolvimento)

```bash
# Clone o repositório
git clone <seu-repositorio>
cd S.U.M/Sistema_Unico_de_Mapeamento

# Backend
cd backend/django-back-end
pip install -r ../requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend (em outro terminal)
cd frontend
npm install
npm run dev
```

### Configuração Manual

#### 1. Backend (Django)

```bash
cd backend/django-back-end

# Instale as dependências
pip install -r ../requirements.txt

# Configure o ambiente
cp env.example .env
# Edite o arquivo .env conforme necessário

# Execute as migrações
python manage.py makemigrations
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

#### 2. Frontend (Vue.js)

```bash
cd frontend

# Instale as dependências
npm install

# Configure o ambiente
cp env.example .env.local
# Edite o arquivo .env.local conforme necessário

# Inicie o servidor de desenvolvimento
npm run dev
```

## 🗄️ Banco de Dados

### SQLite (Desenvolvimento/Testes)
- **Configuração**: Automática via `settings.py`
- **Arquivo**: `backend/django-back-end/db.sqlite3`
- **Testes**: Banco em memória (`:memory:`)

### PostgreSQL (Produção)
- **Configuração**: Via variável `DATABASE_URL` no `.env`
- **Exemplo**: `DATABASE_URL=postgresql://user:password@localhost:5432/sum_db`

## 🔧 Configuração de Ambiente

### Backend (.env)
```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:8080
```

### Frontend (.env.local)
```env
VITE_API_URL=http://localhost:8000
VITE_API_TIMEOUT=10000
VITE_NODE_ENV=development
```

## 🧪 Testes

### Teste de Conexão
```bash
python test_connection.py
```

### Testes Unitários
```bash
# Backend
cd backend/django-back-end
python manage.py test

# Frontend
cd frontend
npm run test:unit
```

### Testes com Docker
```bash
docker-compose -f docker-compose.test.yml up --build
```

## 🐳 Docker

### 🚀 Desenvolvimento (Integração Completa)
```bash
# Inicia todos os serviços com Nginx como proxy reverso
docker-compose up --build

# Parar todos os serviços
docker-compose down

# Ver logs em tempo real
docker-compose logs -f

# Status dos serviços
docker-compose ps
```

### 🔧 Comandos Úteis
```bash
# Executar comandos no backend
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser

# Executar comandos no frontend
docker-compose exec frontend npm install

# Reiniciar um serviço específico
docker-compose restart backend
docker-compose restart frontend
```

## 📡 API Endpoints

- **Health Check**: `GET /api/health/`
- **API Info**: `GET /api/info/`
- **Escola**: `/api/escola/`
- **Estudantes**: `/api/estudantes/`
- **Professores**: `/api/professores/`
- **Atividades**: `/api/atividades/`
- **Eventos**: `/api/eventos/`
- **Mapeamento**: `/api/mapeamento/`

## 🏗️ Arquitetura

### 🌐 Arquitetura com Nginx (Docker)

```
┌─────────────────────────────────────────────────────────────┐
│                        Nginx (Porta 80)                    │
│                    Proxy Reverso Principal                 │
└─────────────────┬───────────────────────────────────────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
┌───▼───┐    ┌───▼───┐    ┌───▼───┐
│Frontend│    │Backend│    │  DB   │
│Vue.js  │    │Django │    │PostgreSQL│
│:5173   │    │:8000  │    │:5432  │
└────────┘    └───────┘    └───────┘
```

### 📁 Estrutura Simplificada

```
Sistema_Unico_de_Mapeamento/
├── docker-compose.yml         # Configuração principal
├── backend/
│   ├── dockerfile            # Container Django
│   └── django-back-end/      # Código Django
├── frontend/
│   ├── dockerfile            # Container Vue.js
│   └── src/                  # Código Vue.js
├── nginx/
│   └── nginx.conf            # Configuração proxy
└── docs/                     # Documentação
```

## 🔐 Autenticação

- **JWT Tokens**: Autenticação stateless
- **Refresh Tokens**: Renovação automática
- **CORS**: Configurado para desenvolvimento
- **Guardião**: Permissões por objeto

## 🎯 Funcionalidades

- **Mapeamento 3D**: Visualização interativa de salas
- **Gestão de Usuários**: Estudantes, professores e administradores
- **Sistema de Atividades**: Criação e gerenciamento
- **IA Integrada**: Geração automática de conteúdo
- **PWA**: Aplicação web progressiva
- **Responsivo**: Interface adaptável

## 🛠️ Desenvolvimento

### Comandos Essenciais

```bash
# Iniciar sistema completo
docker-compose up --build

# Parar sistema
docker-compose down

# Ver logs
docker-compose logs -f

# Executar migrações
docker-compose exec backend python manage.py migrate

# Criar superusuário
docker-compose exec backend python manage.py createsuperuser
```

## 📝 Logs e Monitoramento

```bash
# Ver logs em tempo real
docker-compose logs -f

# Logs específicos
docker-compose logs backend
docker-compose logs frontend
docker-compose logs nginx

# Status dos serviços
docker-compose ps
```

## ✅ Correções Implementadas

### Backend (Django)
- ✅ Corrigido campo `tipo` para `user_type` em todos os modelos
- ✅ Configuração CORS atualizada para incluir portas 5173 e 8080
- ✅ URLs duplicadas removidas e organizadas
- ✅ Autenticação JWT configurada corretamente
- ✅ Logout melhorado para funcionar sem token válido
- ✅ Configuração de banco de dados otimizada

### Frontend (Vue.js)
- ✅ Configuração de proxy atualizada para Docker
- ✅ Dockerfile otimizado para desenvolvimento
- ✅ Configuração Vite corrigida

### Docker & Integração
- ✅ Docker Compose simplificado e funcional
- ✅ Nginx configurado como proxy reverso
- ✅ Scripts de teste automático criados
- ✅ Variáveis de ambiente configuradas
- [Admin Interface](http://localhost:8000/admin/)

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Suporte

Para suporte e dúvidas:
- Abra uma issue no GitHub
- Consulte a documentação da API
- Verifique os logs para troubleshooting