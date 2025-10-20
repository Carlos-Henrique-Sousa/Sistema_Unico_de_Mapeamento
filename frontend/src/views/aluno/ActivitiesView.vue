<template>
  <div class="activities-view bg-gradient-to-br from-gray-900 to-black min-h-screen text-white py-10">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between mb-6">
        <div>
          <h1 class="text-2xl font-bold">Atividades</h1>
          <p class="text-gray-400">Suas tarefas e exercícios</p>
        </div>
        <div class="flex space-x-3">
          <select v-model="filter" class="bg-gray-800 rounded-lg px-3 py-2">
            <option value="all">Todas</option>
            <option value="pending">Pendentes</option>
            <option value="completed">Concluídas</option>
            <option value="late">Atrasadas</option>
          </select>
        </div>
      </div>

      <div v-if="filteredActivities.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <ActivityCard 
          v-for="activity in filteredActivities" 
          :key="activity.id"
          :title="activity.title"
          :deadline="activity.dueDate"
          :status="activity.status"
          :priority="'medium'"
          :participants="[]"
          @click="selectActivity(activity)"
        />
      </div>
      <div v-else class="text-center py-20 text-gray-500">
        <i class="fas fa-inbox text-5xl mb-4 opacity-30"></i>
        <p>Nenhuma atividade encontrada</p>
      </div>

      <ActivityModal 
        v-if="selectedActivity"
        :activity="selectedActivity"
        @close="selectedActivity = null"
        @complete="markCompleted(selectedActivity)"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import ActivityCard from '@/components/activities/ActivityCard.vue';
import ActivityModal from '@/components/activities/ActivityModal.vue';

interface Activity {
  id: number;
  title: string;
  subject: string;
  dueDate: string;
  status: 'pending' | 'completed' | 'late';
  description: string;
  content: string;
}

export default defineComponent({
  name: 'ActivitiesView',
  components: { ActivityCard, ActivityModal },
  setup() {
    const filter = ref<'all' | 'pending' | 'completed' | 'late'>('all');
    const selectedActivity = ref<Activity | null>(null);

    const activities = ref<Activity[]>([
      {
        id: 1,
        title: 'Exercícios de Álgebra',
        subject: 'Matemática',
        dueDate: '2023-11-15',
        status: 'pending',
        description: 'Lista de exercícios sobre equações quadráticas',
        content: '<p>Conteúdo detalhado da atividade...</p>'
      },
      {
        id: 2,
        title: 'Análise de Poema',
        subject: 'Literatura',
        dueDate: '2023-11-10',
        status: 'completed',
        description: 'Análise do poema "No Meio do Caminho" de Carlos Drummond de Andrade',
        content: '<p>Conteúdo detalhado da atividade...</p>'
      },
      {
        id: 3,
        title: 'Experimento de Física',
        subject: 'Ciências',
        dueDate: '2023-11-05',
        status: 'late',
        description: 'Relatório sobre experimento de termodinâmica',
        content: '<p>Conteúdo detalhado da atividade...</p>'
      }
    ]);

    const filteredActivities = computed(() => {
      if (filter.value === 'all') return activities.value;
      return activities.value.filter(a => a.status === filter.value);
    });

    const selectActivity = (activity: Activity) => {
      selectedActivity.value = activity;
    };

    const markCompleted = (activity: Activity | null) => {
      if (!activity) return;
      const idx = activities.value.findIndex(a => a.id === activity.id);
      if (idx !== -1) activities.value[idx].status = 'completed';
      selectedActivity.value = null;
    };

    return { 
      filter, 
      activities, 
      filteredActivities,
      selectedActivity,
      selectActivity,
      markCompleted
    };
  },
});
</script>