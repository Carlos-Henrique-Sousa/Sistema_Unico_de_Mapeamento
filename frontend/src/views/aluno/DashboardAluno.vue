<template>
  <div class="dashboard-aluno bg-gradient-to-br from-gray-900 to-black min-h-screen text-white">
    <!-- Sidebar de Navegação -->
    <div class="sidebar fixed left-0 top-0 h-full w-20 bg-gray-900/80 backdrop-blur-md z-50 flex flex-col items-center py-6">
      <div class="logo mb-10">
        <div class="w-12 h-12 rounded-xl bg-gradient-to-r from-purple-600 to-cyan-500 flex items-center justify-center">
          <span class="font-bold text-white">S</span>
        </div>
      </div>
      
      <nav class="flex-1 space-y-6">
        <router-link 
          v-for="item in navItems" 
          :key="item.name"
          :to="item.path"
          class="w-14 h-14 flex items-center justify-center rounded-xl transition-all duration-300"
          :class="[
            $route.path === item.path 
              ? 'bg-gradient-to-r from-cyan-500 to-purple-600 shadow-lg shadow-cyan-500/30' 
              : 'bg-gray-800 hover:bg-gray-700'
          ]"
          v-tooltip.right="item.name"
        >
          <i :class="item.icon" class="text-xl"></i>
        </router-link>
      </nav>
      
      <div class="mt-auto">
        <button 
          @click="logout"
          class="w-14 h-14 flex items-center justify-center rounded-xl bg-gray-800 hover:bg-rose-600/80 transition-colors"
          v-tooltip.right="'Sair'"
        >
          <i class="fas fa-sign-out-alt"></i>
        </button>
      </div>
    </div>

    <!-- Conteúdo Principal -->
    <div class="main-content ml-20 p-6">
      <!-- Cabeçalho -->
      <header class="flex justify-between items-center mb-8">
        <div>
          <h1 class="text-3xl font-bold">{{ currentPageTitle }}</h1>
          <p class="text-gray-400">{{ currentPageDescription }}</p>
        </div>
        
        <div class="flex items-center space-x-4">
          <div class="relative">
            <button class="bg-gray-800 hover:bg-gray-700 p-3 rounded-full">
              <i class="fas fa-bell"></i>
            </button>
            <span class="absolute top-1 right-1 w-3 h-3 bg-rose-500 rounded-full"></span>
          </div>
          
          <div class="flex items-center space-x-3 bg-gray-800/80 px-4 py-2 rounded-full">
            <div class="w-10 h-10 rounded-full bg-gradient-to-r from-cyan-500 to-purple-500 flex items-center justify-center text-white font-bold">
              {{ userInitials }}
            </div>
            <div>
              <p class="font-medium">{{ userName }}</p>
              <p class="text-xs text-gray-400">{{ userRole }}</p>
            </div>
          </div>
        </div>
      </header>

      <!-- Conteúdo Dinâmico -->
      <div class="dashboard-content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../../store/auth';

export default defineComponent({
  name: 'DashboardAluno',
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    
    const navItems = ref([
      { name: 'Dashboard', path: '/aluno/dashboard', icon: 'fas fa-home' },
      { name: 'DOTS', path: '/aluno/dots', icon: 'fas fa-star' },
      { name: 'Sala de Aula', path: '/aluno/sala', icon: 'fas fa-chalkboard' },
      { name: 'Atividades', path: '/aluno/atividades', icon: 'fas fa-book' },
      { name: 'Provas', path: '/aluno/provas', icon: 'fas fa-file-alt' },
      { name: 'Anotações', path: '/aluno/anotacoes', icon: 'fas fa-sticky-note' },
      { name: 'Chat', path: '/aluno/chat', icon: 'fas fa-comments' },
    ]);
    
    const pageTitles = {
      '/aluno/dashboard': 'Dashboard',
      '/aluno/dots': 'Perfil DOTS',
      '/aluno/sala': 'Sala de Aula',
      '/aluno/atividades': 'Atividades',
      '/aluno/provas': 'Provas Opcionais',
      '/aluno/anotacoes': 'Anotações',
      '/aluno/chat': 'Chat Educacional',
    };
    
    const pageDescriptions = {
      '/aluno/dashboard': 'Visão geral do seu desempenho',
      '/aluno/dots': 'Seu desenvolvimento técnico e social',
      '/aluno/sala': 'Visualização da sua sala e grupo',
      '/aluno/atividades': 'Suas tarefas e exercícios',
      '/aluno/provas': 'Teste seus conhecimentos',
      '/aluno/anotacoes': 'Organize seu conhecimento',
      '/aluno/chat': 'Converse com colegas e professores',
    };
    
    const currentPageTitle = computed(() => {
      return pageTitles[router.currentRoute.value.path as keyof typeof pageTitles] || 'Dashboard';
    });
    
    const currentPageDescription = computed(() => {
      return pageDescriptions[router.currentRoute.value.path as keyof typeof pageDescriptions] || 'Visão geral do seu desempenho';
    });
    
    const userName = computed(() => authStore.user?.name || 'Aluno');
    const userRole = computed(() => authStore.user?.role || 'Aluno');
    
    const userInitials = computed(() => {
      const names = userName.value.split(' ');
      return names.length > 1 
        ? `${names[0][0]}${names[names.length - 1][0]}`
        : names[0][0];
    });
    
    const logout = () => {
      authStore.logout();
      router.push('/login');
    };
    
    return { 
      navItems, 
      currentPageTitle,
      currentPageDescription,
      userName,
      userRole,
      userInitials,
      logout
    };
  },
});
</script>

<style scoped>
.sidebar {
  border-right: 1px solid rgba(255, 255, 255, 0.1);
}

.dashboard-aluno {
  background-image: 
    radial-gradient(circle at 10% 20%, rgba(87, 108, 188, 0.1) 0%, transparent 20%),
    radial-gradient(circle at 90% 80%, rgba(139, 92, 246, 0.1) 0%, transparent 20%);
}

.dashboard-content {
  min-height: calc(100vh - 150px);
}

.router-link-active {
  position: relative;
}

.router-link-active::after {
  content: '';
  position: absolute;
  left: -4px;
  top: 50%;
  transform: translateY(-50%);
  width: 4px;
  height: 24px;
  background: linear-gradient(to bottom, #00c6ff, #0072ff);
  border-radius: 0 4px 4px 0;
}
</style>