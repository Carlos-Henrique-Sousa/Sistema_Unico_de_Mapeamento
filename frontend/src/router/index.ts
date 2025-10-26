import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import { useAuthStore } from '@/store/auth'
import type { UserRole } from '@/types/user'

const routes: RouteRecordRaw[] = [
  // Rotas Públicas
  {
    path: '/',
    name: 'showcase',
    component: () => import('@/views/ShowcaseView.vue'),
    meta: { 
      title: 'S.U.M - Plataforma Educacional',
      public: true,
      layout: 'PublicLayout'
    }
  },
  
  // Rotas de Autenticação
  {
    path: '/auth',
    name: 'auth',
    redirect: '/auth/login',
    meta: { public: true, layout: 'AuthLayout' },
    children: [
      {
        path: 'login',
        name: 'login',
        component: () => import('@/views/auth/LoginView.vue'),
        meta: { title: 'Acessar Plataforma' }
      },
      {
        path: 'register',
        name: 'register',
        component: () => import('@/views/auth/RegisterView.vue'),
        meta: { title: 'Criar Conta' }
      },
      {
        path: 'profile-setup',
        name: 'profile-setup',
        component: () => import('@/views/auth/ProfileSetupView.vue'),
        meta: { 
          title: 'Complete seu Perfil',
          requiresAuth: true
        }
      }
    ]
  },

  // Rotas do Admin
  {
    path: '/admin',
    name: 'admin',
    redirect: '/admin/system-config',
    meta: { 
      requiresAuth: true, 
      allowedRoles: ['Admin'],
      layout: 'AdminLayout'
    },
    children: [
      {
        path: 'system-config',
        name: 'admin-system-config',
        component: () => import('@/views/admin/SystemConfigView.vue'),
        meta: { title: 'Configurações do Sistema' }
      },
      {
        path: 'database',
        name: 'admin-database',
        component: () => import('@/views/admin/DatabaseManager.vue'),
        meta: { title: 'Gerenciamento do Banco de Dados' }
      },
      {
        path: 'status',
        name: 'admin-status',
        component: () => import('@/views/admin/SystemStatusView.vue'),
        meta: { title: 'Status do Sistema' }
      },
    ]
  },

  // Rotas da Escola
  {
    path: '/escola',
    name: 'escola',
    redirect: '/escola/dashboard',
    meta: { 
      requiresAuth: true, 
      allowedRoles: ['Gestor', 'PDT'],
      layout: 'EscolaLayout'
    },
    children: [
      {
        path: 'dashboard',
        name: 'escola-dashboard',
        component: () => import('@/views/escola/DashboardEscola.vue'),
        meta: { title: 'Dashboard da Escola' }
      },
      {
        path: 'classroom-setup',
        name: 'escola-classroom-setup',
        component: () => import('@/views/escola/ClassroomSetupView.vue'),
        meta: { title: 'Configurar Sala de Aula' }
      },
      {
        path: 'user-registration',
        name: 'escola-user-registration',
        component: () => import('@/views/escola/UserRegistrationView.vue'),
        meta: { title: 'Cadastrar Usuários' }
      },
      {
        path: 'reports',
        name: 'escola-reports',
        component: () => import('@/views/escola/ReportsView.vue'),
        meta: { title: 'Relatórios Escolares' }
      },
      {
        path: 'management',
        name: 'escola-management',
        component: () => import('@/views/escola/SchoolManagementView.vue'),
        meta: { title: 'Gerenciamento Escolar' }
      }
    ]
  },

  // Rotas do Professor
  {
    path: '/professor',
    name: 'professor',
    redirect: '/professor/dashboard',
    meta: { 
      requiresAuth: true, 
      allowedRoles: ['Professor'],
      layout: 'ProfessorLayout'
    },
    children: [
      {
        path: 'dashboard',
        name: 'professor-dashboard',
        component: () => import('@/views/professor/DashboardProfessor.vue'),
        meta: { title: 'Dashboard do Professor' }
      },
      {
        path: 'class-management',
        name: 'professor-class-management',
        component: () => import('@/views/professor/ClassManagementView.vue'),
        meta: { title: 'Gerenciar Turmas' }
      },
      {
        path: 'ai-activities',
        name: 'professor-ai-activities',
        component: () => import('@/views/professor/AIActivityView.vue'),
        meta: { title: 'Criar Atividades com IA' }
      },
      {
        path: 'ai-notes',
        name: 'professor-ai-notes',
        component: () => import('@/views/professor/AINotesView.vue'),
        meta: { title: 'Gerar Anotações com IA' }
      },
      {
        path: 'exams',
        name: 'professor-exams',
        component: () => import('@/views/professor/ExamCreatorView.vue'),
        meta: { title: 'Criar Avaliações' }
      },
      {
        path: 'student-analysis',
        name: 'professor-student-analysis',
        component: () => import('@/views/professor/StudentAnalysisView.vue'),
        meta: { title: 'Análise de Alunos' }
      },
      {
        path: 'chat',
        name: 'professor-chat',
        component: () => import('@/views/professor/ChatView.vue'),
        meta: { title: 'Comunicação com Alunos' }
      }
    ]
  },

  // Rotas do Aluno
  {
    path: '/aluno',
    name: 'aluno',
    redirect: '/aluno/dashboard',
    meta: { 
      requiresAuth: true, 
      allowedRoles: ['Aluno'],
      layout: 'AlunoLayout'
    },
    children: [
      {
        path: 'dashboard',
        name: 'aluno-dashboard',
        component: () => import('@/views/aluno/DashboardAluno.vue'),
        meta: { title: 'Meu Dashboard' }
      },
      {
        path: 'classroom',
        name: 'aluno-classroom',
        component: () => import('@/views/aluno/ClassroomView.vue'),
        meta: { title: 'Minha Sala de Aula' }
      },
      {
        path: 'activities',
        name: 'aluno-activities',
        component: () => import('@/views/aluno/ActivitiesView.vue'),
        meta: { title: 'Minhas Atividades' }
      },
      {
        path: 'exams',
        name: 'aluno-exams',
        component: () => import('@/views/aluno/ExamsView.vue'),
        meta: { title: 'Minhas Avaliações' }
      },
      {
        path: 'notes',
        name: 'aluno-notes',
        component: () => import('@/views/aluno/NotesView.vue'),
        meta: { title: 'Minhas Anotações' }
      },
      {
        path: 'dots',
        name: 'aluno-dots',
        component: () => import('@/views/aluno/DotsView.vue'),
        meta: { title: 'Meu Perfil DOTS' }
      },
      {
        path: 'summary',
        name: 'aluno-summary',
        component: () => import('@/views/aluno/SummaryCard.vue'),
        meta: { title: 'Resumo Acadêmico' }
      },
      {
        path: 'chat',
        name: 'aluno-chat',
        component: () => import('@/views/aluno/ChatView.vue'),
        meta: { title: 'Comunicação' }
      }
    ]
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
        top: 80
      }
    } else if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0, behavior: 'smooth' }
    }
  }
})

// Guarda de navegação global
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  
  // Definir título da página
  document.title = `${to.meta.title || 'S.U.M'} - Sistema Único de Mapeamento`
  
  // Verificar autenticação
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    return next({
      name: 'login',
      query: { redirect: to.fullPath }
    })
  }
  
  // Verificar permissões
  if (to.meta.allowedRoles && Array.isArray(to.meta.allowedRoles)) {
    const userRole = authStore.user?.role as UserRole
    const allowedRoles = to.meta.allowedRoles as UserRole[]
    
    if (!userRole || !allowedRoles.includes(userRole)) {
      // Admin sempre tem acesso
      if (userRole === 'Admin') {
        return next()
      }
      
      // Redirecionar para dashboard apropriado
      if (authStore.isAuthenticated) {
        const dashboardRoutes: Record<string, string> = {
          'Gestor': 'escola-dashboard',
          'PDT': 'escola-dashboard',
          'Professor': 'professor-dashboard',
          'Aluno': 'aluno-dashboard',
          'Admin': 'admin-system-config'
        }
        
        const dashboardRoute = dashboardRoutes[userRole] || 'login'
        return next({ name: dashboardRoute })
      }
      
      return next({ name: 'login' })
    }
  }
  
  // Se está autenticado e tenta acessar página pública de login, redireciona
  if (to.name === 'login' && authStore.isAuthenticated) {
    const userRole = authStore.user?.role as UserRole
    const dashboardRoutes: Record<string, string> = {
      'Gestor': 'escola-dashboard',
      'PDT': 'escola-dashboard',
      'Professor': 'professor-dashboard',
      'Aluno': 'aluno-dashboard',
      'Admin': 'admin-system-config'
    }
    
    return next({ name: dashboardRoutes[userRole] || 'showcase' })
  }
  
  next()
})

// Pré-carregamento inteligente de rotas
router.afterEach((to) => {
  const preloadRoutes: Record<string, string[]> = {
    'login': ['register'],
    'aluno-dashboard': ['aluno-classroom', 'aluno-activities'],
    'professor-dashboard': ['professor-class-management', 'professor-ai-activities'],
    'escola-dashboard': ['escola-user-registration', 'escola-management']
  }
  
  const routeNames = preloadRoutes[to.name as string]
  if (routeNames) {
    routeNames.forEach(name => {
      const route = router.resolve({ name })
      if (route.matched.length) {
        const component = route.matched[0].components?.default
        if (component && typeof component === 'function') {
          component()
        }
      }
    })
  }
})

export default router