<template>
  <div v-if="isLoading" class="flex items-center justify-center min-h-screen">
    <i class="fas fa-spinner fa-spin text-4xl text-cyan-400"></i>
  </div>
  <div v-else class="dots-view bg-gradient-to-br from-gray-900 to-black min-h-screen text-white py-10">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between mb-10">
        <div>
          <h1 class="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-amber-400 to-orange-500">
            Meu Perfil DOTS
          </h1>
          <p class="text-gray-400">Seu desenvolvimento técnico e social</p>
        </div>
        <div class="text-right">
          <span class="px-4 py-2 bg-amber-500/20 text-amber-400 rounded-full text-sm">
            Pontuação: {{ totalPoints }}
          </span>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
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
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-8">
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