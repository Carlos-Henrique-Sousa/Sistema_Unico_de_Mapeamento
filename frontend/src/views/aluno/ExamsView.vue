<template>
  <div class="exams-view bg-gradient-to-br from-gray-900 to-black min-h-screen text-white py-10">
    <div class="container mx-auto px-4">
      <div class="text-center mb-10">
        <h1 class="text-4xl font-bold mb-2 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-cyan-400">
          Provas Opcionais
        </h1>
        <p class="text-gray-400">Teste seus conhecimentos e ganhe pontos DOTS</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <!-- Provas Disponíveis -->
        <GlassCard>
          <h2 class="text-2xl font-bold mb-6">Provas Disponíveis</h2>
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
        <GlassCard>
          <h2 class="text-2xl font-bold mb-6">Minhas Tentativas</h2>
          <div v-if="attempts.length === 0" class="text-center py-10 text-gray-500">
            <i class="fas fa-inbox text-4xl mb-4 opacity-30"></i>
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
      <GlassCard class="mt-8">
        <h2 class="text-2xl font-bold mb-6">Criar Prova Personalizada</h2>
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