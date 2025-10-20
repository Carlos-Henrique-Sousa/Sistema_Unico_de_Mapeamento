<template>
  <div class="dashboard-professor">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <div class="logo">
          <div class="logo-icon">S</div>
          <span class="logo-text">S.U.M</span>
        </div>
      </div>
      
      <nav class="sidebar-nav">
        <router-link 
          v-for="item in navItems" 
          :key="item.name"
          :to="item.path"
          class="nav-item"
          :class="{ 'active': $route.path === item.path }"
        >
          <i :class="item.icon" class="nav-icon"></i>
          <span class="nav-text">{{ item.name }}</span>
        </router-link>
      </nav>
      
      <div class="sidebar-footer">
        <button @click="logout" class="logout-btn">
          <i class="fas fa-sign-out-alt"></i>
          <span>Sair</span>
        </button>
      </div>
    </aside>

    <!-- Conteúdo Principal -->
    <div class="main-content">
      <!-- Header -->
      <header class="page-header">
        <div class="header-left">
          <h1 class="page-title">{{ currentPageTitle }}</h1>
          <p class="page-subtitle">{{ currentPageDescription }}</p>
        </div>
        
        <div class="header-right">
          <!-- Notificações -->
          <button class="icon-btn notification-btn">
            <i class="fas fa-bell"></i>
            <span class="badge">3</span>
          </button>
          
          <!-- Perfil -->
          <div class="user-profile">
            <div class="avatar">{{ userInitials }}</div>
            <div class="user-info">
              <p class="user-name">{{ userName }}</p>
              <p class="user-role">{{ userRole }}</p>
            </div>
          </div>
        </div>
      </header>

      <!-- Conteúdo Dinâmico -->
      <div class="content-area">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useAuthStore } from '@/store';

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const navItems = [
  { name: 'Dashboard', path: '/professor/dashboard', icon: 'fas fa-th-large' },
  { name: 'Turmas', path: '/professor/class-management', icon: 'fas fa-chalkboard-teacher' },
  { name: 'IA Atividades', path: '/professor/ai-activities', icon: 'fas fa-robot' },
  { name: 'IA Notas', path: '/professor/ai-notes', icon: 'fas fa-file-invoice' },
  { name: 'Provas', path: '/professor/exams', icon: 'fas fa-clipboard-check' },
  { name: 'Análise', path: '/professor/student-analysis', icon: 'fas fa-chart-line' },
  { name: 'Chat', path: '/professor/chat', icon: 'fas fa-comments' }
]

const pageTitles: Record<string, string> = {
  '/professor/dashboard': 'Dashboard',
  '/professor/class-management': 'Gerenciar Turmas',
  '/professor/ai-activities': 'Atividades com IA',
  '/professor/ai-notes': 'Notas com IA',
  '/professor/exams': 'Criar Provas',
  '/professor/student-analysis': 'Análise de Alunos',
  '/professor/chat': 'Comunicação'
}

const pageDescriptions: Record<string, string> = {
  '/professor/dashboard': 'Visão geral das suas turmas e atividades',
  '/professor/class-management': 'Gerencie suas salas de aula e alunos',
  '/professor/ai-activities': 'Crie atividades personalizadas com inteligência artificial',
  '/professor/ai-notes': 'Gere anotações e resumos automaticamente',
  '/professor/exams': 'Monte avaliações personalizadas',
  '/professor/student-analysis': 'Acompanhe o desempenho dos alunos',
  '/professor/chat': 'Converse com alunos e colegas'
}

const currentPageTitle = computed(() => pageTitles[route.path] || 'Dashboard')
const currentPageDescription = computed(() => pageDescriptions[route.path] || '')
const userName = computed(() => authStore.user?.nome || 'Professor')
const userRole = computed(() => 'Professor')

const userInitials = computed(() => {
  const names = userName.value.split(' ')
  return names.length > 1 
    ? `${names[0][0]}${names[names.length - 1][0]}`
    : names[0][0]
})

function logout() {
  authStore.logout()
  router.push('/auth/login')
}
</script>

<style scoped>
.dashboard-professor {
  display: flex;
  min-height: 100vh;
  background: #0a0a0a;
  color: #ffffff;
}

/* Sidebar */
.sidebar {
  width: 280px;
  background: linear-gradient(180deg, #1a1a1a 0%, #0f0f0f 100%);
  border-right: 1px solid rgba(16, 185, 129, 0.1);
  display: flex;
  flex-direction: column;
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  z-index: 100;
}

.sidebar-header {
  padding: 2rem 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.logo {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.logo-icon {
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, #10b981, #fbbf24);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: 900;
  color: #0a0a0a;
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, #10b981, #fbbf24);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.sidebar-nav {
  flex: 1;
  padding: 1.5rem 1rem;
  overflow-y: auto;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.25rem;
  margin-bottom: 0.5rem;
  border-radius: 12px;
  color: rgba(255, 255, 255, 0.6);
  text-decoration: none;
  transition: all 0.3s ease;
  position: relative;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.05);
  color: #10b981;
}

.nav-item.active {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(251, 191, 36, 0.15));
  color: #10b981;
  border-left: 3px solid #10b981;
}

.nav-icon {
  font-size: 1.25rem;
  width: 24px;
  text-align: center;
}

.nav-text {
  font-weight: 600;
  font-size: 0.95rem;
}

.sidebar-footer {
  padding: 1.5rem 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.logout-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  padding: 1rem;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: 12px;
  color: #ef4444;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.logout-btn:hover {
  background: rgba(239, 68, 68, 0.2);
  border-color: #ef4444;
}

/* Main Content */
.main-content {
  flex: 1;
  margin-left: 280px;
  display: flex;
  flex-direction: column;
}

.page-header {
  padding: 2rem;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.05), rgba(251, 191, 36, 0.05));
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-left {
  flex: 1;
}

.page-title {
  font-size: 2rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, #ffffff, #10b981);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.page-subtitle {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.95rem;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.icon-btn {
  position: relative;
  width: 48px;
  height: 48px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  color: #ffffff;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-btn:hover {
  background: rgba(16, 185, 129, 0.1);
  border-color: #10b981;
  color: #10b981;
}

.badge {
  position: absolute;
  top: -6px;
  right: -6px;
  width: 20px;
  height: 20px;
  background: #fbbf24;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: 700;
  color: #0a0a0a;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.5rem 1rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.user-profile:hover {
  background: rgba(255, 255, 255, 0.05);
  border-color: #10b981;
}

.avatar {
  width: 44px;
  height: 44px;
  background: linear-gradient(135deg, #10b981, #fbbf24);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: #0a0a0a;
}

.user-info {
  display: flex;
  flex-direction: column;
}

.user-name {
  font-weight: 600;
  font-size: 0.95rem;
  color: #ffffff;
  margin: 0;
}

.user-role {
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.5);
  margin: 0;
}

/* Content Area */
.content-area {
  flex: 1;
  padding: 2rem;
  background: 
    linear-gradient(135deg, rgba(16, 185, 129, 0.02) 0%, transparent 50%),
    linear-gradient(225deg, rgba(251, 191, 36, 0.02) 0%, transparent 50%);
}

/* Responsive */
@media (max-width: 768px) {
  .sidebar {
    width: 80px;
  }
  
  .logo-text,
  .nav-text,
  .logout-btn span {
    display: none;
  }
  
  .main-content {
    margin-left: 80px;
  }
  
  .page-header {
    flex-direction: column;
    gap: 1rem;
  }
  
  .header-right {
    width: 100%;
    justify-content: space-between;
  }
}

/* Scrollbar customizado */
.sidebar-nav::-webkit-scrollbar {
  width: 6px;
}

.sidebar-nav::-webkit-scrollbar-track {
  background: transparent;
}

.sidebar-nav::-webkit-scrollbar-thumb {
  background: rgba(16, 185, 129, 0.3);
  border-radius: 10px;
}

.sidebar-nav::-webkit-scrollbar-thumb:hover {
  background: rgba(16, 185, 129, 0.5);
}
</style>