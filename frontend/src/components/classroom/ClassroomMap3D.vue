<template>
  <div class="classroom-map-3d relative bg-[#1f1d20]/5 rounded-xl overflow-hidden border-2 border-[#e1d4c2]" :style="{ height }">
    <!-- Simulation Overlay -->
    <div 
      v-if="simulationMode" 
      class="simulation-overlay absolute inset-0 pointer-events-none z-20 transition-all"
      :class="simulationClasses"
      :style="overlayStyle"
    ></div>

    <!-- 3D Canvas Container -->
    <div ref="canvasContainer" class="w-full h-full"></div>

    <!-- Controls Overlay -->
    <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm rounded-lg p-3 shadow-lg z-10">
      <div class="space-y-2 text-sm">
        <div class="flex items-center gap-2">
          <div class="w-3 h-3 rounded-full bg-[#2d531a]"></div>
          <span class="text-[#1f1d20]">Aluno</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="w-3 h-3 rounded-full bg-purple-500"></div>
          <span class="text-[#1f1d20]">Dificuldade Visual</span>
        </div>
      </div>
    </div>

    <!-- View Controls -->
    <div class="absolute top-4 right-4 flex flex-col gap-2 z-10">
      <button 
        @click="resetCamera"
        class="p-2 rounded-lg bg-white/90 hover:bg-white shadow-lg transition-all"
        title="Resetar Câmera"
      >
        <svg class="w-5 h-5 text-[#2d531a]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
      </button>
      <button 
        @click="toggleView"
        class="p-2 rounded-lg bg-white/90 hover:bg-white shadow-lg transition-all"
        title="Alternar Vista"
      >
        <svg class="w-5 h-5 text-[#2d531a]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
        </svg>
      </button>
    </div>

    <!-- Loading State -->
    <div v-if="isLoading" class="absolute inset-0 flex items-center justify-center bg-white/80 backdrop-blur-sm z-30">
      <div class="text-center">
        <div class="w-16 h-16 mx-auto mb-4">
          <div class="w-full h-full rounded-full border-4 border-[#2d531a] border-t-transparent animate-spin"></div>
        </div>
        <p class="text-[#1f1d20] font-medium">Carregando sala 3D...</p>
      </div>
    </div>

    <!-- Info Panel -->
    <div v-if="selectedStudent" class="absolute bottom-4 left-4 bg-white/95 backdrop-blur-sm rounded-lg p-4 shadow-lg max-w-xs z-10">
      <div class="flex items-center gap-3 mb-2">
        <div 
          class="w-10 h-10 rounded-full flex items-center justify-center text-white font-bold"
          :class="selectedStudent.visionIssues ? 'bg-purple-500' : 'bg-gradient-to-br from-[#2d531a] to-[#0f1e3f]'"
        >
          {{ selectedStudent.name.split(' ').map(n => n[0]).join('') }}
        </div>
        <div>
          <h5 class="font-bold text-[#1f1d20]">{{ selectedStudent.name }}</h5>
          <p class="text-xs text-[#1f1d20]/60">Posição na sala</p>
        </div>
      </div>
      <div v-if="selectedStudent.visionIssues" class="flex items-center gap-2 p-2 bg-purple-50 rounded-lg">
        <svg class="w-4 h-4 text-purple-600" fill="currentColor" viewBox="0 0 20 20">
          <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
          <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd" />
        </svg>
        <span class="text-xs text-purple-700 font-medium">Necessita atenção especial</span>
      </div>
    </div>

    <!-- Instructions -->
    <div v-if="!simulationMode && !editMode" class="absolute bottom-4 right-4 bg-white/90 backdrop-blur-sm rounded-lg p-3 shadow-lg max-w-xs z-10">
      <p class="text-xs text-[#1f1d20]/70">
        <strong class="text-[#2d531a]">Dica:</strong> Use o mouse para rotacionar, scroll para zoom
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, computed } from 'vue';

interface Student {
  id: string;
  name: string;
  visionIssues?: boolean;
  position: { x: number; y: number; z: number };
}

interface SimulationOptions {
  studentId: string;
  type: 'myopia' | 'astigmatism' | 'glaucoma' | 'colorBlindness';
  intensity: number;
  showLabels: boolean;
}

const props = withDefaults(defineProps<{
  classroomId: string;
  height?: string;
  interactive?: boolean;
  simulationMode?: boolean;
  simulationOptions?: SimulationOptions;
  editMode?: boolean;
}>(), {
  height: '70vh',
  interactive: false,
  simulationMode: false,
  editMode: false
});

const emit = defineEmits<{
  'student-moved': [studentId: string, position: { x: number; y: number; z: number }];
}>();

const canvasContainer = ref<HTMLElement | null>(null);
const isLoading = ref(true);
const selectedStudent = ref<Student | null>(null);
const currentView = ref<'top' | 'perspective'>('perspective');

// Mock data
const students = ref<Student[]>([
  { id: '1', name: 'João Silva', position: { x: -2, y: 0, z: -1 } },
  { id: '2', name: 'Maria Santos', visionIssues: true, position: { x: 0, y: 0, z: -1 } },
  { id: '3', name: 'Pedro Costa', position: { x: 2, y: 0, z: -1 } },
  { id: '4', name: 'Ana Lima', position: { x: -2, y: 0, z: 1 } },
  { id: '5', name: 'Carlos Souza', position: { x: 0, y: 0, z: 1 } }
]);

// Simulation overlay classes
const simulationClasses = computed(() => {
  if (!props.simulationMode || !props.simulationOptions) return '';
  
  const classes = [];
  const { type, intensity } = props.simulationOptions;
  
  switch (type) {
    case 'myopia':
      classes.push('blur-overlay');
      break;
    case 'glaucoma':
      classes.push('vignette-overlay');
      break;
    case 'colorBlindness':
      classes.push('color-filter-overlay');
      break;
  }
  
  if (intensity > 70) {
    classes.push('high-intensity');
  }
  
  return classes.join(' ');
});

const overlayStyle = computed(() => {
  if (!props.simulationMode || !props.simulationOptions) return {};
  
  const { type, intensity } = props.simulationOptions;
  const styles: any = {};
  
  switch (type) {
    case 'myopia':
      styles.backdropFilter = `blur(${intensity / 8}px)`;
      break;
    case 'glaucoma':
      styles.background = `radial-gradient(circle at center, transparent ${100 - intensity}%, rgba(0,0,0,0.9) 100%)`;
      break;
    case 'colorBlindness':
      styles.filter = `grayscale(${intensity * 0.6}%) saturate(${100 - intensity}%)`;
      break;
  }
  
  return styles;
});

// Initialize 3D scene (simplified - would use Three.js in production)
const init3DScene = () => {
  isLoading.value = true;
  
  // Simulate loading
  setTimeout(() => {
    isLoading.value = false;
    console.log('3D scene initialized for classroom:', props.classroomId);
  }, 1500);
  
  // Here would be Three.js initialization:
  // - Create scene, camera, renderer
  // - Add classroom model (floor, walls, board)
  // - Add student avatars at positions
  // - Add controls (OrbitControls)
  // - Setup lights
  // - Animation loop
};

const resetCamera = () => {
  console.log('Camera reset');
  // Reset camera to default position
};

const toggleView = () => {
  currentView.value = currentView.value === 'top' ? 'perspective' : 'top';
  console.log('View toggled to:', currentView.value);
};

const selectStudentById = (id: string) => {
  selectedStudent.value = students.value.find(s => s.id === id) || null;
};

// Watch for simulation changes
watch(() => props.simulationOptions, (newOptions) => {
  if (props.simulationMode && newOptions) {
    console.log('Applying simulation:', newOptions);
    // Apply visual effects based on simulation type
  }
}, { deep: true });

onMounted(() => {
  if (canvasContainer.value) {
    init3DScene();
  }
});

onUnmounted(() => {
  // Cleanup Three.js resources
  console.log('Cleaning up 3D scene');
});
</script>

<style scoped>
.simulation-overlay {
  transition: all 0.3s ease;
  mix-blend-mode: multiply;
}

.blur-overlay {
  backdrop-filter: blur(4px);
}

.vignette-overlay {
  background: radial-gradient(circle at center, transparent 60%, rgba(0,0,0,0.8) 100%);
}

.color-filter-overlay {
  filter: saturate(0.3) contrast(1.2);
}

.high-intensity {
  opacity: 0.85;
}

/* Button hover effects */
button {
  transition: all 0.2s ease;
}

button:hover {
  transform: scale(1.05);
}

button:active {
  transform: scale(0.95);
}
</style>