<template>
  <div v-if="isLoading" class="flex items-center justify-center min-h-screen">
    <i class="fas fa-spinner fa-spin text-4xl text-cyan-400"></i>
  </div>
  <div v-else class="dots-root">
    <div class="container">
      <div class="topbar">
        <div>
          <h1 class="title">Meu Perfil DOTS</h1>
          <p class="subtitle">Seu desenvolvimento técnico e social</p>
        </div>
        <div class="right">
          <span class="badge">Pontuação: {{ totalPoints }}</span>
        </div>
      </div>

      <div class="grid3">
        <!-- Habilidades -->
        <GlassCard class="lg:col-span-2">
          <div class="mb-6">
            <h2 class="text-2xl font-bold mb-4">Habilidades</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <SkillCard 
                v-for="(skill, index) in skills" 
                :key="index"
                :data="skill"
                :color="skillColors[index % skillColors.length]"
              />
            </div>
          </div>

          <div>
            <h2 class="text-2xl font-bold mb-4">Progresso Geral</h2>
            <ProgressRing :progress="overallProgress" :size="180" class="mx-auto" />
          </div>
        </GlassCard>

            <GlassCard>
      <h2 class="text-2xl font-bold mb-4">Conquistas</h2>
      <div class="space-y-4 max-h-[600px] overflow-y-auto pr-2">
        <AchievementCard 
          v-for="achievement in achievements" 
          :key="achievement.id"
          :title="achievement.title"
          :description="achievement.description"
          :points="achievement.points"
          :date="achievement.date"
          :icon="achievement.icon"
          :badges="achievement.badges || []"
        />
      </div>
    </GlassCard>
      </div>

      <!-- Comparação e Análise -->
      <div class="grid2">
        <GlassCard>
          <h2 class="text-2xl font-bold mb-4">Comparação com a Turma</h2>
          <div class="h-80">
            <InteractiveChart type="radar" :data="comparisonData" />
          </div>
        </GlassCard>

        <GlassCard>
          <h2 class="text-2xl font-bold mb-4">Análise de Desenvolvimento</h2>
          <div class="prose prose-invert max-w-none" v-html="analysis"></div>
        </GlassCard>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import GlassCard from '@/shared/GlassCard.vue';
import SkillCard from '@/components/dots/DotsTechnicalCard.vue';
import AchievementCard from '@/components/dots/DotsBadges.vue';
import ProgressRing from '@/shared/ProgressRing.vue';
import InteractiveChart from '@/shared/InteractiveChart.vue';
import { useDots } from '@/composables/useDots';


export default defineComponent({
  name: 'DotsView',
  components: { 
    GlassCard, 
    SkillCard, 
    AchievementCard,
    ProgressRing,
    InteractiveChart
  },
  setup() {
    const { profile, isLoading } = useDots();
    
    const skillColors = ['#9b59b6', '#3498db', '#2ecc71', '#f1c40f', '#e74c3c'];
    
    const totalPoints = computed(() => profile.value?.totalPoints || 0);
    const overallProgress = computed(() => {
      const total = Object.values(profile.value?.skills || {}).reduce((sum: number, val: unknown) => sum + (typeof val === 'number' ? val : 0), 0);
      return Math.min(100, Math.floor(total / 500 * 100));
    });
    
    const skills = computed(() => {
      if (!profile.value) return [];
      // Assuming profile.value.skills is an object where each key is a skill name and value is an object with the required properties
      return Object.entries(profile.value.skills)
        .map(([name, skillData]) => ({
          name: name as string,
          value: (skillData as any).value ?? 0,
          skills: (skillData as any).skills ?? [],
          projects: (skillData as any).projects ?? 0,
          certifications: (skillData as any).certifications ?? 0
        }))
        .sort((a, b) => a.value - b.value);
    });
    
    const achievements = computed(() => {
      return profile.value?.achievements || [];
    });
    
    const comparisonData = ref({
      labels: ['Humanas', 'Exatas', 'Linguagens', 'Projetos', 'Jogos'],
      datasets: [
        {
          label: 'Você',
          data: [85, 72, 90, 65, 80],
          backgroundColor: 'rgba(155, 89, 182, 0.2)',
          borderColor: '#9b59b6',
        },
        {
          label: 'Média da Turma',
          data: [75, 68, 82, 60, 72],
          backgroundColor: 'rgba(52, 152, 219, 0.2)',
          borderColor: '#3498db',
        }
      ]
    });
    
    const analysis = ref(`
      <h3>Pontos Fortes</h3>
      <ul>
        <li>Excelente em Linguagens e Comunicação</li>
        <li>Participação ativa em projetos</li>
        <li>Bom desempenho em atividades colaborativas</li>
      </ul>
      
      <h3>Áreas para Melhoria</h3>
      <ul>
        <li>Pode melhorar em raciocínio lógico</li>
        <li>Desafios em exatas</li>
      </ul>
      
      <h3>Recomendações</h3>
      <p>Participe das atividades extras de matemática e do clube de programação.</p>
    `);
    
    return { 
      profile, 
      isLoading,
      skillColors,
      totalPoints,
      overallProgress,
      skills,
      achievements,
      comparisonData,
      analysis
    };
  }
});
</script>

<style scoped>
.dots-root { background:#fcfcfc; color:#17181e; min-height:100vh; padding:2rem 0; }
.container { max-width:1100px; margin:0 auto; padding:0 1rem; }
.topbar { display:flex; align-items:center; justify-content:space-between; margin-bottom:1rem; }
.title { font-size:2rem; font-weight:800; }
.subtitle { color:#6b6b6b; }
.right { text-align:right; }
.badge { padding:0.35rem 0.6rem; background:rgba(23,24,30,0.06); border:1px solid rgba(23,24,30,0.1); border-radius:999px; font-size:0.8rem; }
.grid3 { display:grid; grid-template-columns:1fr; gap:1rem; }
@media (min-width:1024px){ .grid3 { grid-template-columns: 2fr 1fr; } }
.grid2 { display:grid; grid-template-columns:1fr; gap:1rem; margin-top:1rem; }
@media (min-width:1024px){ .grid2 { grid-template-columns: 1fr 1fr; } }
</style>