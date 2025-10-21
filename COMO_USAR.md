# 🚀 S.U.M - Configuração Simples pelo Terminal

## ✅ Configuração Limpa e Simples

Removi todos os scripts complexos e mantive apenas o essencial para funcionar pelo terminal.

## 🎯 Como Usar

### 1. **Iniciar o Sistema Completo**
```bash
cd Sistema_Unico_de_Mapeamento
docker-compose up --build
```

### 2. **Parar o Sistema**
```bash
docker-compose down
```

### 3. **Ver Logs**
```bash
docker-compose logs -f
```

### 4. **Reiniciar um Serviço**
```bash
docker-compose restart backend
docker-compose restart frontend
docker-compose restart nginx
```

## 🌐 URLs Disponíveis

Após executar `docker-compose up --build`:

- **Frontend**: http://localhost/
- **Backend API**: http://localhost/api/
- **Admin Django**: http://localhost/admin/

## 🔧 Comandos Úteis

### **Executar comandos no backend**
```bash
# Migrações
docker-compose exec backend python manage.py migrate

# Criar superusuário
docker-compose exec backend python manage.py createsuperuser

# Shell do Django
docker-compose exec backend python manage.py shell
```

### **Executar comandos no frontend**
```bash
# Instalar dependências
docker-compose exec frontend npm install

# Build para produção
docker-compose exec frontend npm run build
```

### **Verificar status**
```bash
docker-compose ps
```

## 📁 Estrutura Simplificada

```
Sistema_Unico_de_Mapeamento/
├── docker-compose.yml          # Configuração principal
├── backend/
│   ├── dockerfile             # Container Django
│   └── django-back-end/       # Código Django
├── frontend/
│   ├── dockerfile             # Container Vue.js
│   └── src/                   # Código Vue.js
└── nginx/
    └── nginx.conf             # Configuração proxy
```

## 🎉 Pronto!

Agora você tem uma configuração limpa e simples que funciona diretamente pelo terminal, sem scripts `.bat` ou arquivos desnecessários!
