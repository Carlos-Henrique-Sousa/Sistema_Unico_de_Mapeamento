<template>
  <div class="profile-setup-view flex items-center justify-center min-h-screen bg-gradient-to-br from-cyan-900 to-purple-900">
    <GlassCard class="w-full max-w-md p-8">
      <h2 class="text-2xl font-bold mb-6 text-center">Configurar Perfil</h2>
      <form @submit.prevent="saveProfile" class="space-y-4">
        <div>
          <input
            v-model="profile.name"
            class="bg-gray-800 rounded-lg px-3 py-2 w-full"
            placeholder="Nome"
            :class="{ 'border-red-500': errors.name }"
          />
          <p v-if="errors.name" class="text-red-400 text-xs mt-1">{{ errors.name }}</p>
        </div>
        <div>
          <select v-model="profile.role" class="bg-gray-800 rounded-lg px-3 py-2 w-full">
            <option value="Aluno">Aluno</option>
            <option value="Professor">Professor</option>
            <option value="Gestor">Gestor</option>
          </select>
        </div>
        <div>
          <input
            v-model="profile.avatar"
            class="bg-gray-800 rounded-lg px-3 py-2 w-full"
            placeholder="URL do Avatar (opcional)"
          />
        </div>
        <button
          class="bg-cyan-600 hover:bg-cyan-500 px-4 py-2 rounded-lg w-full font-bold flex items-center justify-center"
          :disabled="loading"
        >
          <span v-if="loading" class="loader mr-2"></span>
          Salvar
        </button>
        <p v-if="apiError" class="text-red-400 text-sm mt-2 text-center">{{ apiError }}</p>
        <p v-if="success" class="text-emerald-400 text-sm mt-2 text-center">Perfil salvo com sucesso!</p>
      </form>
    </GlassCard>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import GlassCard from '@shared/GlassCard.vue';

export default {
  name: 'ProfileSetupView',
  components: { GlassCard },
  setup() {
    const router = useRouter();
    const profile = ref({ name: '', role: 'Aluno', avatar: '' });
    const errors = ref<{ [key: string]: string }>({});
    const loading = ref(false);
    const apiError = ref('');
    const success = ref(false);

    function validate() {
      errors.value = {};
      if (!profile.value.name.trim()) {
        errors.value.name = 'Nome é obrigatório.';
      }
      return Object.keys(errors.value).length === 0;
    }

    async function saveProfile() {
      apiError.value = '';
      success.value = false;
      if (!validate()) return;
      loading.value = true;
      try {
        // Simulação de chamada à API
        await new Promise((resolve) => setTimeout(resolve, 1000));
        success.value = true;
        setTimeout(() => router.push('/dashboard'), 1200);
      } catch (err: any) {
        apiError.value = err.message || 'Erro ao salvar perfil.';
      } finally {
        loading.value = false;
      }
    }

    return { profile, errors, loading, apiError, success, saveProfile };
  }
};
</script>

<style scoped>
.loader {
  border: 2px solid #22d3ee;
  border-top: 2px solid transparent;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  animation: spin 0.7s linear infinite;
  display: inline-block;
  vertical-align: middle;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>