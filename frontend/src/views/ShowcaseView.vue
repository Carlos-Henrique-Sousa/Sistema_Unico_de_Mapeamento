<template>
  <div class="showcase-view">
    <!-- Header -->
    <header :class="['header', { 'header-scrolled': scrolled }]">
      <nav class="nav-container">
        <div class="logo-section">
          <div class="logo-icon">
            <span>S</span>
          </div>
          <span class="logo-text">S.U.M</span>
        </div>
        
        <button @click="menuOpen = !menuOpen" class="menu-toggle">
          <svg v-if="!menuOpen" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
          <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
        
        <div class="nav-links">
          <a href="#features">Recursos</a>
          <a href="#profiles">Perfis</a>
          <a href="#about">Sobre</a>
          <button class="btn-primary">Começar Agora</button>
        </div>
      </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-bg-gradient"></div>
      <div class="hero-blur hero-blur-1"></div>
      <div class="hero-blur hero-blur-2"></div>
      
      <div class="hero-content">
        <div class="hero-badge">
          <span class="pulse-dot"></span>
          <span>Plataforma educacional inteligente</span>
        </div>
        
        <h1 class="hero-title">
          Sistema Único de
          <span class="gradient-text">Mapeamento</span>
        </h1>
        
        <p class="hero-description">
          Revolucione a gestão educacional com análises em tempo real, inteligência artificial e dashboards personalizados para cada perfil
        </p>
        
        <div class="hero-buttons">
          <button class="btn-primary btn-large">
            Explorar Plataforma
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>
          <button class="btn-secondary btn-large">Ver Demonstração</button>
        </div>

        <!-- Stats -->
        <div class="stats-grid">
          <div v-for="stat in stats" :key="stat.label" class="stat-card">
            <div class="stat-value">{{ stat.value }}</div>
            <div class="stat-label">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="features-section">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">
            Recursos <span class="text-emerald">Poderosos</span>
          </h2>
          <p class="section-description">
            Ferramentas completas para transformar a experiência educacional
          </p>
        </div>

        <div class="features-grid">
          <div v-for="feature in features" :key="feature.title" class="feature-card">
            <div class="feature-icon">
              <component :is="feature.icon" />
            </div>
            <h3 class="feature-title">{{ feature.title }}</h3>
            <p class="feature-description">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Profiles Section -->
    <section id="profiles" class="profiles-section">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">
            Escolha seu <span class="text-cyan">Perfil</span>
          </h2>
          <p class="section-description">
            Experiência personalizada para cada tipo de usuário
          </p>
        </div>

        <div class="profiles-grid">
          <div 
            v-for="profile in profiles" 
            :key="profile.id"
            class="profile-card"
            :class="{ 'active': activeProfile === profile.id }"
            @mouseenter="activeProfile = profile.id"
            @mouseleave="activeProfile = null"
          >
            <div :class="['profile-gradient', profile.gradientClass]"></div>
            <div class="profile-content">
              <div :class="['profile-icon', profile.gradientClass]">
                <component :is="profile.icon" />
              </div>
              
              <h3 class="profile-name">{{ profile.name }}</h3>
              <p class="profile-description">{{ profile.description }}</p>
              
              <div class="profile-stats">
                <div v-for="stat in profile.stats" :key="stat.label" class="profile-stat">
                  <div class="profile-stat-label">
                    <component :is="stat.icon" />
                    <span>{{ stat.label }}</span>
                  </div>
                  <span class="profile-stat-value">{{ stat.value }}</span>
                </div>
              </div>
              
              <button class="profile-button">
                Acessar Dashboard
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="cta-blur cta-blur-1"></div>
      <div class="cta-blur cta-blur-2"></div>
      
      <div class="cta-content">
        <h2 class="cta-title">
          Pronto para transformar sua
          <span class="cta-gradient-text">experiência educacional?</span>
        </h2>
        <p class="cta-description">
          Junte-se a milhares de educadores e estudantes que já utilizam o S.U.M
        </p>
        <button class="btn-cta">Começar Gratuitamente</button>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-logo">
          <div class="logo-icon">
            <span>S</span>
          </div>
          <span class="logo-text">S.U.M</span>
        </div>
        <p class="footer-description">
          Sistema Único de Mapeamento - Plataforma educacional inteligente
        </p>
        <div class="footer-links">
          <a href="#">Termos de Uso</a>
          <a href="#">Privacidade</a>
          <a href="#">Contato</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, defineComponent, h } from 'vue'

// Icons as Vue components
const BarChartIcon = defineComponent({
  render: () => h('svg', { width: 24, height: 24, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('line', { x1: 12, y1: 20, x2: 12, y2: 10 }),
    h('line', { x1: 18, y1: 20, x2: 18, y2: 4 }),
    h('line', { x1: 6, y1: 20, x2: 6, y2: 16 })
  ])
})

const FileTextIcon = defineComponent({
  render: () => h('svg', { width: 24, height: 24, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('path', { d: 'M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z' }),
    h('polyline', { points: '14 2 14 8 20 8' }),
    h('line', { x1: 16, y1: 13, x2: 8, y2: 13 }),
    h('line', { x1: 16, y1: 17, x2: 8, y2: 17 }),
    h('polyline', { points: '10 9 9 9 8 9' })
  ])
})

const TrendingUpIcon = defineComponent({
  render: () => h('svg', { width: 24, height: 24, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('polyline', { points: '23 6 13.5 15.5 8.5 10.5 1 18' }),
    h('polyline', { points: '17 6 23 6 23 12' })
  ])
})

const CalendarIcon = defineComponent({
  render: () => h('svg', { width: 24, height: 24, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('rect', { x: 3, y: 4, width: 18, height: 18, rx: 2, ry: 2 }),
    h('line', { x1: 16, y1: 2, x2: 16, y2: 6 }),
    h('line', { x1: 8, y1: 2, x2: 8, y2: 6 }),
    h('line', { x1: 3, y1: 10, x2: 21, y2: 10 })
  ])
})

const BookOpenIcon = defineComponent({
  render: () => h('svg', { width: 32, height: 32, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('path', { d: 'M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z' }),
    h('path', { d: 'M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z' })
  ])
})

const UsersIcon = defineComponent({
  render: () => h('svg', { width: 32, height: 32, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('path', { d: 'M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2' }),
    h('circle', { cx: 9, cy: 7, r: 4 }),
    h('path', { d: 'M23 21v-2a4 4 0 0 0-3-3.87' }),
    h('path', { d: 'M16 3.13a4 4 0 0 1 0 7.75' })
  ])
})

const SchoolIcon = defineComponent({
  render: () => h('svg', { width: 32, height: 32, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('path', { d: 'M22 10v6M2 10l10-5 10 5-10 5z' }),
    h('path', { d: 'M6 12v5c3 3 9 3 12 0v-5' })
  ])
})

const SettingsIcon = defineComponent({
  render: () => h('svg', { width: 32, height: 32, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('circle', { cx: 12, cy: 12, r: 3 }),
    h('path', { d: 'M12 1v6m0 6v6m9.22-9.22l-4.24 4.24m-5.96 0L6.78 9.78m12.44 8.44l-4.24-4.24m-5.96 0l-4.24 4.24' })
  ])
})

const SmallFileIcon = defineComponent({
  render: () => h('svg', { width: 16, height: 16, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('path', { d: 'M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z' }),
    h('polyline', { points: '14 2 14 8 20 8' })
  ])
})

const SmallTrendIcon = defineComponent({
  render: () => h('svg', { width: 16, height: 16, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('polyline', { points: '23 6 13.5 15.5 8.5 10.5 1 18' }),
    h('polyline', { points: '17 6 23 6 23 12' })
  ])
})

const SmallUsersIcon = defineComponent({
  render: () => h('svg', { width: 16, height: 16, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('path', { d: 'M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2' }),
    h('circle', { cx: 9, cy: 7, r: 4 })
  ])
})

const SmallBookIcon = defineComponent({
  render: () => h('svg', { width: 16, height: 16, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('path', { d: 'M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z' }),
    h('path', { d: 'M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z' })
  ])
})

const SmallSchoolIcon = defineComponent({
  render: () => h('svg', { width: 16, height: 16, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': 2 }, [
    h('path', { d: 'M22 10v6M2 10l10-5 10 5-10 5z' }),
    h('path', { d: 'M6 12v5c3 3 9 3 12 0v-5' })
  ])
})

const scrolled = ref(false)
const menuOpen = ref(false)
const activeProfile = ref<string | null>(null)

const stats = [
  { value: '3.5k+', label: 'Usuários Ativos' },
  { value: '98%', label: 'Satisfação' },
  { value: '24/7', label: 'Suporte' },
  { value: '12+', label: 'Instituições' }
]

const features = [
  {
    title: 'Dashboard Inteligente',
    description: 'Visualize dados em tempo real com gráficos e métricas personalizadas',
    icon: BarChartIcon
  },
  {
    title: 'Gestão de Atividades',
    description: 'Crie, distribua e avalie atividades de forma automatizada',
    icon: FileTextIcon
  },
  {
    title: 'Análise de Desempenho',
    description: 'Acompanhe o progresso individual e coletivo com relatórios detalhados',
    icon: TrendingUpIcon
  },
  {
    title: 'Calendário Acadêmico',
    description: 'Organize eventos, prazos e compromissos em um só lugar',
    icon: CalendarIcon
  }
]

const profiles = [
  {
    id: 'aluno',
    name: 'Aluno',
    icon: BookOpenIcon,
    description: 'Acompanhe seu desempenho acadêmico em tempo real',
    color: '#10b981',
    gradientClass: 'gradient-emerald',
    stats: [
      { label: 'Atividades', value: '24', icon: SmallFileIcon },
      { label: 'Progresso', value: '87%', icon: SmallTrendIcon }
    ]
  },
  {
    id: 'professor',
    name: 'Professor',
    icon: UsersIcon,
    description: 'Gerencie turmas e atividades com inteligência artificial',
    color: '#3b82f6',
    gradientClass: 'gradient-blue',
    stats: [
      { label: 'Turmas', value: '5', icon: SmallUsersIcon },
      { label: 'Alunos', value: '142', icon: SmallBookIcon }
    ]
  },
  {
    id: 'escola',
    name: 'Escola',
    icon: SchoolIcon,
    description: 'Administre recursos e acompanhe métricas institucionais',
    color: '#8b5cf6',
    gradientClass: 'gradient-violet',
    stats: [
      { label: 'Professores', value: '48', icon: SmallUsersIcon },
      { label: 'Estudantes', value: '1.2k', icon: SmallBookIcon }
    ]
  },
  {
    id: 'admin',
    name: 'Admin',
    icon: SettingsIcon,
    description: 'Configurações avançadas e gestão do sistema',
    color: '#06b6d4',
    gradientClass: 'gradient-cyan',
    stats: [
      { label: 'Escolas', value: '12', icon: SmallSchoolIcon },
      { label: 'Usuários', value: '3.5k', icon: SmallUsersIcon }
    ]
  }
]

const handleScroll = () => {
  scrolled.value = window.scrollY > 20
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.showcase-view {
  min-height: 100vh;
  background: #fcfcfc;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

/* Header */
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 50;
  transition: all 0.3s ease;
}

.header-scrolled {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(20px);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.nav-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 1rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.logo-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #10b981, #06b6d4);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-icon span {
  color: white;
  font-weight: bold;
  font-size: 1.25rem;
}

.logo-text {
  font-size: 1.25rem;
  font-weight: bold;
  color: #17181D;
}

.menu-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  color: #17181D;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-links a {
  color: #6b7280;
  text-decoration: none;
  transition: color 0.3s;
}

.nav-links a:hover {
  color: #17181D;
}

.btn-primary {
  padding: 0.625rem 1.5rem;
  background: linear-gradient(135deg, #10b981, #06b6d4);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-primary:hover {
  box-shadow: 0 10px 25px rgba(16, 185, 129, 0.3);
  transform: scale(1.05);
}

.btn-secondary {
  padding: 0.625rem 1.5rem;
  background: white;
  color: #17181D;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-secondary:hover {
  border-color: #10b981;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.btn-large {
  padding: 1rem 2rem;
  font-size: 1rem;
}

/* Hero Section */
.hero-section {
  padding: 8rem 1.5rem 5rem;
  position: relative;
  overflow: hidden;
}

.hero-bg-gradient {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #f0fdf4, #ecfeff, #eff6ff);
  opacity: 0.5;
}

.hero-blur {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.2;
}

.hero-blur-1 {
  top: 5rem;
  left: 2.5rem;
  width: 18rem;
  height: 18rem;
  background: #10b981;
}

.hero-blur-2 {
  bottom: 2.5rem;
  right: 2.5rem;
  width: 24rem;
  height: 24rem;
  background: #06b6d4;
}

.hero-content {
  max-width: 1280px;
  margin: 0 auto;
  position: relative;
  z-index: 10;
  text-align: center;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  border: 1px solid #e5e7eb;
  margin-bottom: 2rem;
  font-size: 0.875rem;
  color: #6b7280;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  background: #10b981;
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.hero-title {
  font-size: 4rem;
  font-weight: 900;
  color: #17181D;
  margin-bottom: 1.5rem;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.gradient-text {
  display: block;
  background: linear-gradient(135deg, #10b981, #06b6d4, #3b82f6);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-description {
  font-size: 1.25rem;
  color: #6b7280;
  max-width: 48rem;
  margin: 0 auto 3rem;
  line-height: 1.6;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 5rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  max-width: 1000px;
  margin: 0 auto;
}

.stat-card {
  background: white;
  border-radius: 1rem;
  padding: 1.5rem;
  border: 1px solid #f3f4f6;
  transition: all 0.3s;
}

.stat-card:hover {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  background: linear-gradient(135deg, #10b981, #06b6d4);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 0.875rem;
  color: #6b7280;
}

/* Features Section */
.features-section {
  padding: 5rem 1.5rem;
  background: white;
}

.section-container {
  max-width: 1280px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-title {
  font-size: 3rem;
  font-weight: bold;
  color: #17181D;
  margin-bottom: 1rem;
}

.text-emerald {
  color: #10b981;
}

.text-cyan {
  color: #06b6d4;
}

.section-description {
  font-size: 1.125rem;
  color: #6b7280;
  max-width: 48rem;
  margin: 0 auto;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.feature-card {
  background: linear-gradient(135deg, #f9fafb, white);
  padding: 2rem;
  border-radius: 1rem;
  border: 1px solid #f3f4f6;
  transition: all 0.3s;
}

.feature-card:hover {
  border-color: #10b981;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #10b981, #06b6d4);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  margin-bottom: 1.5rem;
  transition: transform 0.3s;
}

.feature-card:hover .feature-icon {
  transform: scale(1.1);
}

.feature-title {
  font-size: 1.25rem;
  font-weight: bold;
  color: #17181D;
  margin-bottom: 0.75rem;
}

.feature-description {
  color: #6b7280;
  line-height: 1.6;
}

/* Profiles Section */
.profiles-section {
  padding: 5rem 1.5rem;
  background: linear-gradient(135deg, #f9fafb, white);
}

.profiles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.profile-card {
  position: relative;
  background: white;
  border-radius: 1.5rem;
  overflow: hidden;
  border: 2px solid #f3f4f6;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.profile-card:hover {
  border-color: transparent;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
}

.profile-gradient {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 0.5s;
}

.profile-card:hover .profile-gradient {
  opacity: 1;
}

.gradient-emerald {
  background: linear-gradient(135deg, #10b981, #14b8a6);
}

.gradient-blue {
  background: linear-gradient(135deg, #3b82f6, #06b6d4);
}

.gradient-violet {
  background: linear-gradient(135deg, #8b5cf6, #a855f7);
}

.gradient-cyan {
  background: linear-gradient(135deg, #06b6d4, #3b82f6);
}

.profile-content {
  position: relative;
  padding: 2rem;
  background: white;
  border-radius: 1.4rem;
  margin: 2px;
}

.profile-icon {
  width: 64px;
  height: 64px;
  border-radius: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  margin-bottom: 1.5rem;
  transition: all 0.3s;
}

.profile-card:hover .profile-icon {
  transform: scale(1.1) rotate(5deg);
}

.profile-name {
  font-size: 1.5rem;
  font-weight: bold;
  color: #17181D;
  margin-bottom: 0.75rem;
}

.profile-description {
  color: #6b7280;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.profile-stats {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}

.profile-stat {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #f9fafb;
  border-radius: 12px;
  padding: 0.75rem;
}

.profile-stat-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #6b7280;
  font-size: 0.875rem;
}

.profile-stat-value {
  font-weight: bold;
  color: #17181D;
}

.profile-button {
  width: 100%;
  padding: 0.75rem;
  background: #f9fafb;
  color: #17181D;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.profile-card:hover .profile-button {
  background: linear-gradient(135deg, #10b981, #06b6d4);
  color: white;
}

.profile-button svg {
  transition: transform 0.3s;
}

.profile-card:hover .profile-button svg {
  transform: translateX(4px);
}

/* CTA Section */
.cta-section {
  padding: 5rem 1.5rem;
  background: linear-gradient(135deg, #17181D, #1f2937);
  color: white;
  position: relative;
  overflow: hidden;
}

.cta-blur {
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
  opacity: 0.1;
}

.cta-blur-1 {
  top: 0;
  left: 25%;
  width: 24rem;
  height: 24rem;
  background: #10b981;
}

.cta-blur-2 {
  bottom: 0;
  right: 25%;
  width: 24rem;
  height: 24rem;
  background: #06b6d4;
}

.cta-content {
  max-width: 56rem;
  margin: 0 auto;
  text-align: center;
  position: relative;
  z-index: 10;
}

.cta-title {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.cta-gradient-text {
  display: block;
  background: linear-gradient(135deg, #6ee7b7, #67e8f9);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.cta-description {
  font-size: 1.25rem;
  color: #d1d5db;
  margin-bottom: 2.5rem;
  line-height: 1.6;
}

.btn-cta {
  padding: 1.25rem 2.5rem;
  background: white;
  color: #17181D;
  border: none;
  border-radius: 12px;
  font-weight: bold;
  font-size: 1.125rem;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-cta:hover {
  box-shadow: 0 25px 50px rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

/* Footer */
.footer {
  padding: 3rem 1.5rem;
  background: white;
  border-top: 1px solid #f3f4f6;
}

.footer-content {
  max-width: 1280px;
  margin: 0 auto;
  text-align: center;
}

.footer-logo {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.footer-description {
  color: #6b7280;
  margin-bottom: 1.5rem;
}

.footer-links {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  font-size: 0.875rem;
}

.footer-links a {
  color: #9ca3af;
  text-decoration: none;
  transition: color 0.3s;
}

.footer-links a:hover {
  color: #10b981;
}

/* Responsive */
@media (max-width: 1024px) {
  .hero-title {
    font-size: 3rem;
  }
  
  .section-title {
    font-size: 2.5rem;
  }
  
  .cta-title {
    font-size: 2.5rem;
  }
}

@media (max-width: 768px) {
  .menu-toggle {
    display: block;
  }
  
  .nav-links {
    display: none;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-description {
    font-size: 1.125rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .cta-title {
    font-size: 2rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .profiles-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .hero-buttons {
    flex-direction: column;
  }
  
  .btn-large {
    width: 100%;
  }
  
  .footer-links {
    flex-direction: column;
    gap: 1rem;
  }
}