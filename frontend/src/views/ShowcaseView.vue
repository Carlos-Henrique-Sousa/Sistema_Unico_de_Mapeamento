<template>
  <div class="showcase-container">
    <!-- Fundo animado com partículas -->
    <div class="particles-container" ref="particlesRef"></div>

    <!-- Grade de fundo -->
    <div class="grid-background"></div>

    <div class="content">
      <!-- Hero Section -->
      <div class="hero-section">
        <div class="logo-container">
          <div class="logo-wrapper">
            <img src="@/assets/logo.png" alt="S.U.M Logo" class="logo">
          </div>
          <h1 class="title">
            Sistema Único de <span class="highlight">Mapeamento</span>
          </h1>
          <p class="subtitle">Plataforma educacional inteligente para gestão e análise</p>
        </div>
      </div>

      <!-- Cards de Acesso -->
      <div class="access-grid">
        <router-link 
          v-for="profile in profiles" 
          :key="profile.name" 
          :to="profile.mainRoute"
          class="profile-card"
          :style="{ '--card-color': profile.color }"
          @mouseenter="activateProfile(profile.name)"
        >
          <div class="card-glow"></div>
          <div class="card-content">
            <div class="icon-wrapper">
              <div class="icon">{{ profile.icon }}</div>
            </div>
            <h3>{{ profile.name }}</h3>
            <p>{{ profile.description }}</p>
            <div class="card-arrow">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
                <path d="M10 5l5 5-5 5V5z"/>
              </svg>
            </div>
          </div>
        </router-link>
      </div>

      <!-- Seção de Preview -->
      <div class="preview-section" v-if="activePreview">
        <div class="preview-header">
          <h2>Prévia: {{ activePreview.name }}</h2>
          <p>Explore as funcionalidades do perfil selecionado</p>
        </div>
        <div class="preview-container">
          <div class="preview-content">
            <component :is="activePreview.previewComponent" class="preview-component" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import DashboardAluno from '@/views/aluno/DashboardAluno.vue'
import DashboardProfessor from '@/views/professor/DashboardProfessor.vue'
import DashboardEscola from '@/views/escola/DashboardEscola.vue'
import SystemConfigView from '@/views/admin/SystemConfigView.vue'

const profiles = [
  {
    name: 'Aluno',
    icon: '🎓',
    description: 'Acompanhe seu desempenho e atividades',
    mainRoute: '/aluno/dashboard',
    previewComponent: DashboardAluno,
    color: '#10b981' // Verde
  },
  {
    name: 'Professor',
    icon: '👨‍🏫',
    description: 'Gerencie turmas e atividades com IA',
    mainRoute: '/professor/dashboard',
    previewComponent: DashboardProfessor,
    color: '#fbbf24' // Amarelo
  },
  {
    name: 'Escola',
    icon: '🏫',
    description: 'Administre recursos e usuários',
    mainRoute: '/escola/dashboard',
    previewComponent: DashboardEscola,
    color: '#f59e0b' // Laranja
  },
  {
    name: 'Admin',
    icon: '⚙️',
    description: 'Configurações do sistema',
    mainRoute: '/admin/system-config',
    previewComponent: SystemConfigView,
    color: '#ffffff' // Branco
  }
]

const activeProfile = ref<string | null>(null)
const particlesRef = ref<HTMLElement | null>(null)

const activePreview = computed(() => {
  if (!activeProfile.value) return null
  return profiles.find(p => p.name === activeProfile.value) || null
})

function activateProfile(profileName: string) {
  activeProfile.value = profileName
}

function initParticles() {
  if (!particlesRef.value) return
  
  for (let i = 0; i < 30; i++) {
    const particle = document.createElement('div')
    particle.className = 'particle'
    particle.style.setProperty('--x', `${Math.random() * 100}%`)
    particle.style.setProperty('--y', `${Math.random() * 100}%`)
    particle.style.setProperty('--delay', `${Math.random() * 5}s`)
    particle.style.setProperty('--duration', `${10 + Math.random() * 10}s`)
    particlesRef.value.appendChild(particle)
  }
}

onMounted(() => {
  initParticles()
})
</script>

<style scoped>
.showcase-container {
  position: relative;
  min-height: 100vh;
  background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0f0f0f 100%);
  color: #ffffff;
  overflow: hidden;
}

/* Fundo de grade */
.grid-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    linear-gradient(rgba(16, 185, 129, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(16, 185, 129, 0.05) 1px, transparent 1px);
  background-size: 50px 50px;
  z-index: 0;
}

/* Partículas */
.particles-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
}

.particle {
  position: absolute;
  width: 4px;
  height: 4px;
  background: radial-gradient(circle, #10b981 0%, transparent 70%);
  border-radius: 50%;
  top: var(--y);
  left: var(--x);
  animation: float var(--duration) var(--delay) infinite ease-in-out;
}

@keyframes float {
  0%, 100% {
    transform: translate(0, 0);
    opacity: 0;
  }
  10% {
    opacity: 0.8;
  }
  50% {
    transform: translate(50px, -100px);
    opacity: 1;
  }
  90% {
    opacity: 0.8;
  }
}

/* Conteúdo */
.content {
  position: relative;
  z-index: 10;
  max-width: 1400px;
  margin: 0 auto;
  padding: 4rem 2rem;
}

/* Hero Section */
.hero-section {
  text-align: center;
  margin-bottom: 4rem;
  animation: fadeIn 1s ease-out;
}

.logo-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.logo-wrapper {
  width: 140px;
  height: 140px;
  padding: 20px;
  background: linear-gradient(135deg, #10b981, #fbbf24);
  border-radius: 30px;
  margin-bottom: 2rem;
  animation: pulse 3s ease-in-out infinite;
  box-shadow: 0 10px 40px rgba(16, 185, 129, 0.3);
}

.logo {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: brightness(1.2);
}

.title {
  font-size: 4rem;
  font-weight: 900;
  margin-bottom: 1rem;
  letter-spacing: -2px;
  background: linear-gradient(135deg, #ffffff 0%, #10b981 50%, #fbbf24 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1.2;
}

.highlight {
  display: inline-block;
  position: relative;
}

.subtitle {
  font-size: 1.25rem;
  color: rgba(255, 255, 255, 0.7);
  max-width: 600px;
  margin: 0 auto;
}

/* Grid de Cards */
.access-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-bottom: 4rem;
}

.profile-card {
  position: relative;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 20px;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
}

.profile-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--card-color);
  transform: scaleX(0);
  transition: transform 0.4s ease;
}

.profile-card:hover::before {
  transform: scaleX(1);
}

.profile-card:hover {
  transform: translateY(-8px);
  background: rgba(255, 255, 255, 0.06);
  border-color: var(--card-color);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4),
              0 0 40px var(--card-color);
}

.card-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, var(--card-color) 0%, transparent 70%);
  transform: translate(-50%, -50%);
  opacity: 0;
  transition: opacity 0.4s ease;
}

.profile-card:hover .card-glow {
  opacity: 0.15;
}

.card-content {
  position: relative;
  z-index: 2;
}

.icon-wrapper {
  width: 80px;
  height: 80px;
  margin: 0 auto 1.5rem;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(251, 191, 36, 0.1));
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.4s ease;
}

.profile-card:hover .icon-wrapper {
  transform: scale(1.1) rotate(5deg);
  border-color: var(--card-color);
}

.icon {
  font-size: 2.5rem;
}

.profile-card h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #ffffff;
}

.profile-card p {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.95rem;
  line-height: 1.6;
}

.card-arrow {
  position: absolute;
  bottom: 1.5rem;
  right: 1.5rem;
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--card-color);
  opacity: 0;
  transform: translateX(-10px);
  transition: all 0.4s ease;
}

.profile-card:hover .card-arrow {
  opacity: 1;
  transform: translateX(0);
}

/* Preview Section */
.preview-section {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 30px;
  overflow: hidden;
  animation: slideUp 0.6s ease-out;
}

.preview-header {
  padding: 2rem;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(251, 191, 36, 0.1));
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
}

.preview-header h2 {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #10b981;
}

.preview-header p {
  color: rgba(255, 255, 255, 0.6);
}

.preview-container {
  padding: 2rem;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.preview-content {
  width: 100%;
  max-width: 1200px;
}

.preview-component {
  transform: scale(0.9);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
  pointer-events: none;
}

/* Animations */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
    box-shadow: 0 10px 40px rgba(16, 185, 129, 0.3);
  }
  50% {
    transform: scale(1.05);
    box-shadow: 0 15px 60px rgba(16, 185, 129, 0.5);
  }
}

/* Responsive */
@media (max-width: 768px) {
  .title {
    font-size: 2.5rem;
  }
  
  .subtitle {
    font-size: 1rem;
  }
  
  .access-grid {
    grid-template-columns: 1fr;
  }
  
  .logo-wrapper {
    width: 100px;
    height: 100px;
  }
}
</style>