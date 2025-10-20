<template>
  <div class="classroom-view bg-gradient-to-br from-gray-900 to-black min-h-screen text-white py-10">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between mb-6">
        <div>
          <h1 class="text-2xl font-bold">Minha Sala de Aula</h1>
          <p class="text-gray-400">Sala 1A - Professora Mariana</p>
        </div>
        <div>
          <button @click="toggleViewMode" class="bg-gray-800 hover:bg-gray-700 px-4 py-2 rounded-lg transition-colors">
            <i :class="viewMode === '3d' ? 'fas fa-cube' : 'fas fa-th'" class="mr-2"></i>
            {{ viewMode === '3d' ? 'Visão 2D' : 'Visão 3D' }}
          </button>
        </div>
      </div>

      <div class="classroom-container bg-gray-800/20 rounded-xl p-4 min-h-[500px] relative">
        <component :is="viewModeComponent" :students="students" />
        <div class="absolute bottom-4 right-4 flex space-x-3">
          <button class="bg-cyan-600 hover:bg-cyan-500 w-10 h-10 rounded-full flex items-center justify-center shadow-lg">
            <i class="fas fa-expand"></i>
          </button>
          <button class="bg-purple-600 hover:bg-purple-500 w-10 h-10 rounded-full flex items-center justify-center shadow-lg">
            <i class="fas fa-search"></i>
          </button>
        </div>
      </div>

      <div class="mt-6">
        <h2 class="text-xl font-bold mb-4">Meu Grupo</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
          <StudentCard 
            v-for="student in groupMembers" 
            :key="student.id"
            :student="student"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import ClassroomMap3D from '@/components/classroom/ClassroomMap3D.vue';
import ClassroomGrid from '@/components/classroom/ClassroomGrid.vue';
import StudentCard from '@/components/classroom/StudentCard.vue';
import { useClassroom } from '@/composables/useClassroom';

export default defineComponent({
  name: 'ClassroomView',
  components: { ClassroomMap3D, ClassroomGrid, StudentCard },
  setup() {
    const { students } = useClassroom();
    const viewMode = ref<'3d' | '2d'>('3d');
    const toggleViewMode = () => {
      viewMode.value = viewMode.value === '3d' ? '2d' : '3d';
    };
    const viewModeComponent = computed(() => viewMode.value === '3d' ? 'ClassroomMap3D' : 'ClassroomGrid');
    const groupMembers = computed(() => students.value.slice(0, 4));
    return { students, viewMode, toggleViewMode, viewModeComponent, groupMembers };
  },
});
</script>

<style scoped>
.classroom-container {
  background-image: 
    radial-gradient(circle at center, rgba(139, 92, 246, 0.1) 0%, transparent 70%),
    linear-gradient(to bottom, rgba(30, 30, 40, 0.8), rgba(30, 30, 40, 0.9));
}
</style>