<template>
  <div class="login-view flex items-center justify-center min-h-screen bg-gradient-to-br from-cyan-900 to-purple-900">
    <GlassCard class="w-full max-w-md p-8">
      <h2 class="text-2xl font-bold mb-6 text-center">Entrar</h2>
      <form @submit.prevent="login" class="space-y-4">
        <div>
          <input
            v-model="form.email"
            class="bg-gray-800 rounded-lg px-3 py-2 w-full"
            placeholder="Email"
            type="email"
            :class="{ 'border-red-500': errors.email }"
          />
          <p v-if="errors.email" class="text-red-400 text-xs mt-1">{{ errors.email }}</p>
        </div>
        <div>
          <input
            v-model="form.password"
            class="bg-gray-800 rounded-lg px-3 py-2 w-full"
            placeholder="Senha"
            type="password"
            :class="{ 'border-red-500': errors.password }"
          />
          <p v-if="errors.password" class="text-red-400 text-xs mt-1">{{ errors.password }}</p>
        </div>
        <button
          class="bg-cyan-600 hover:bg-cyan-500 px-4 py-2 rounded-lg w-full font-bold flex items-center justify-center"
          :disabled="loading"
        >
          <span v-if="loading" class="loader mr-2"></span>
          Entrar
        </button>
        <p v-if="apiError" class="text-red-400 text-sm mt-2 text-center">{{ apiError }}</p>
      </form>
      <p class="mt-4 text-center text-gray-400">
        Não tem uma conta?
        <router-link to="/auth/register" class="text-cyan-400 hover:underline">Registrar</router-link>
      </p>
    </GlassCard>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import GlassCard from '@shared/GlassCard.vue';

export default {
  name: 'LoginView',
  components: { GlassCard },
  setup() {
    const router = useRouter();
    const form = ref({ email: '', password: '' });
    const errors = ref<{ [key: string]: string }>({});
    const loading = ref(false);
    const apiError = ref('');

    function validate() {
      errors.value = {};
      if (!form.value.email.trim()) {
        errors.value.email = 'Email é obrigatório.';
      } else if (!/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/.test(form.value.email)) {
        errors.value.email = 'Email inválido.';
      }
      if (!form.value.password) {
        errors.value.password = 'Senha é obrigatória.';
      }
      return Object.keys(errors.value).length === 0;
    }

    async function login() {
      apiError.value = '';
      if (!validate()) return;
      loading.value = true;
      try {
        // Simulação de chamada à API
        await new Promise((resolve, reject) => setTimeout(() => {
          if (form.value.email !== 'usuario@email.com' || form.value.password !== '123456') {
            reject(new Error('Credenciais inválidas.'));
          } else {
            resolve(true);
          }
        }, 1000));
        router.push('/dashboard');
      } catch (err: any) {
        apiError.value = err.message || 'Erro ao entrar.';
      } finally {
        loading.value = false;
      }
    }

    return { form, errors, loading, apiError, login };
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