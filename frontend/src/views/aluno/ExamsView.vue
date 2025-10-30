<template>
  <div class="exams-root">
    <div class="container">
      <div class="heading">
        <h1 class="title">Provas Opcionais</h1>
        <p class="subtitle">Teste seus conhecimentos e ganhe pontos DOTS</p>
      </div>
      <div class="grid">
        <!-- Provas Disponíveis -->
        <GlassCard class="blue-glass">
          <h2 class="text-2xl font-extrabold mb-6 text-blue-400">Provas Disponíveis</h2>
          <div class="space-y-4">
            <ExamCard 
              v-for="exam in availableExams" 
              :key="exam.id"
              :exam="exam"
              @start="startExam(exam)"
            />
          </div>
        </GlassCard>
        <!-- Minhas Tentativas -->
        <GlassCard class="blue-glass">
          <h2 class="text-2xl font-extrabold mb-6 text-blue-400">Minhas Tentativas</h2>
          <div v-if="attempts.length === 0" class="text-center py-10 text-blue-300">
            <i class="fas fa-inbox text-4xl mb-4 opacity-20"></i>
            <p>Nenhuma tentativa registrada</p>
          </div>
          <div v-else class="space-y-4">
            <AttemptCard 
              v-for="attempt in attempts" 
              :key="attempt.id"
              :attempt="attempt"
            />
          </div>
        </GlassCard>
      </div>
      <!-- Criador de Provas -->
      <GlassCard class="blue-glass mt-8">
        <h2 class="text-2xl font-extrabold mb-6 text-blue-400">Criar Prova Personalizada</h2>
        <ExamCreator />
      </GlassCard>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import GlassCard from '@/shared/GlassCard.vue';
import ExamCard from '@/components/activities/ExamCard.vue';
import AttemptCard from '@/components/activities/AttemptCard.vue';
import ExamCreator from '@/components/activities/ExamCreator.vue';

export default defineComponent({
  name: 'ExamsView',
  components: { GlassCard, ExamCard, AttemptCard, ExamCreator },
  setup() {
    const availableExams = ref([
      { id: 1, title: 'Matemática Básica', subject: 'Matemática', duration: 60, difficulty: 'Fácil', points: 50 },
      { id: 2, title: 'Literatura Brasileira', subject: 'Literatura', duration: 45, difficulty: 'Médio', points: 75 },
      { id: 3, title: 'Ciências - Termodinâmica', subject: 'Ciências', duration: 90, difficulty: 'Difícil', points: 100 }
    ]);
    
    const attempts = ref([
      { id: 1, examId: 1, date: '2023-10-20', score: 85, status: 'completed' },
      { id: 2, examId: 2, date: '2023-10-25', score: 70, status: 'completed' }
    ]);
    
    const startExam = (exam: any) => {
      // Lógica para iniciar prova
      alert(`Iniciando prova: ${exam.title}`);
    };
    
    return { availableExams, attempts, startExam };
  },
});
</script>

<style scoped>
.exams-root { background:var(--cor-fundo); color:var(--cor-primaria); min-height:100vh; padding:2.3rem 0; }
.container { max-width:1100px; margin:0 auto; padding:0 1rem; }
.heading { text-align:center; margin-bottom:2rem; }
.title { font-size:2.15rem; font-weight:900; color:var(--cor-primaria); }
.subtitle { color:var(--cor-azul-light); }
.grid { display:grid; grid-template-columns: 1fr; gap:1.22rem; }
@media (min-width: 1024px) { .grid { grid-template-columns: 1fr 1fr; } }
.blue-glass { background:rgba(52,152,219,0.11) !important; border:1.5px solid var(--cor-azul-prim) !important; box-shadow:0 3.5px 19px rgba(52,152,219,0.13) !important; }
@media(max-width:700px){ .container{padding:0 2vw;} }
</style>