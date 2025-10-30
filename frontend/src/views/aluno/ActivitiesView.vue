<template>
  <div class="activities-root">
    <div class="container">
      <div class="header">
        <div>
          <h1 class="title">Atividades</h1>
          <p class="subtitle">Suas tarefas e exercícios</p>
        </div>
        <div>
          <select v-model="filter" class="select">
            <option value="all">Todas</option>
            <option value="pending">Pendentes</option>
            <option value="completed">Concluídas</option>
            <option value="late">Atrasadas</option>
          </select>
        </div>
      </div>

      <div v-if="filteredActivities.length" class="grid">
        <ActivityCard 
          v-for="activity in filteredActivities" 
          :key="activity.id"
          :title="activity.title"
          :deadline="activity.dueDate"
          :status="activity.status"
          :priority="'medium'"
          :participants="[]"
          @click="selectActivity(activity)"
          class="card-style"
        />
      </div>
      <div v-else class="empty">
        <i class="fas fa-inbox"></i>
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

<style scoped>
.activities-root { background:var(--cor-fundo); color:var(--cor-primaria); min-height:100vh; padding:2.5rem 0; }
.container { max-width:1100px; margin:0 auto; padding:0 1rem; }
.header { display:flex; align-items:center; justify-content:space-between; margin-bottom:2rem; }
.title { font-size:2.0rem; font-weight:900; color:var(--cor-primaria); margin-bottom:0.18rem; letter-spacing:-0.5px; }
.subtitle { color:var(--cor-azul-light); font-size:1.08rem; font-weight:500; }
.select { padding:0.68rem 0.9rem; min-width:148px; border:1.5px solid var(--cor-azul-prim); border-radius:14px; background:var(--cor-fundo); color:var(--cor-primaria); font-weight:600; outline:none; font-size:1.02rem; box-shadow:0 1.5px 10px rgba(58,134,255,0.04); }
.grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(305px, 1fr)); gap:1.35rem; }
.empty { text-align:center; color:var(--cor-cinza); padding:4rem 0; }
.empty i { font-size:52px; opacity:0.15; display:block; margin-bottom:0.7rem; color:var(--cor-azul-light); }
@media(max-width:700px){ .container{padding:0 2vw;} .header{flex-direction:column;gap:1.2rem;align-items:flex-start;}}
</style>