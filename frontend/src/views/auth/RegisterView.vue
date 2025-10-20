<template>
  <div class="register-view flex items-center justify-center min-h-screen bg-gradient-to-br from-cyan-900 to-purple-900">
    <GlassCard class="w-full max-w-md p-8">
      <h2 class="text-2xl font-bold mb-6 text-center">Criar Conta</h2>
      <form @submit.prevent="register" class="space-y-4">
        <div>
          <input
            v-model="form.name"
            class="bg-gray-800 rounded-lg px-3 py-2 w-full"
            placeholder="Nome"
            :class="{ 'border-red-500': errors.name }"
          />
          <p v-if="errors.name" class="text-red-400 text-xs mt-1">{{ errors.name }}</p>
        </div>
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
        <div>
          <select v-model="form.role" class="bg-gray-800 rounded-lg px-3 py-2 w-full">
            <option value="Aluno">Aluno</option>
            <option value="Professor">Professor</option>
            <option value="Gestor">Gestor</option>
          </select>
        </div>
        <button
          class="bg-cyan-600 hover:bg-cyan-500 px-4 py-2 rounded-lg w-full font-bold flex items-center justify-center"
          :disabled="loading"
        >
          <span v-if="loading" class="loader mr-2"></span>
          Registrar
        </button>
        <p v-if="apiError" class="text-red-400 text-sm mt-2 text-center">{{ apiError }}</p>
        <p v-if="success" class="text-emerald-400 text-sm mt-2 text-center">Cadastro realizado com sucesso!</p>
      </form>
      <p class="mt-4 text-center text-gray-400">
        Já tem uma conta?
        <router-link to="/auth/login" class="text-cyan-400 hover:underline">Entrar</router-link>
      </p>
    </GlassCard>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import GlassCard from '@shared/GlassCard.vue';

interface RegisterForm {
  name: string;
  email: string;
  password: string;
  role: string;
}

export default {
  name: 'RegisterView',
  components: { GlassCard },
  setup() {
    const router = useRouter();
    const form = ref<RegisterForm>({
      name: '',
      email: '',
      password: '',
      role: 'Aluno'
    });
    const errors = ref<{ [key: string]: string }>({});
    const loading = ref(false);
    const apiError = ref('');
    const success = ref(false);

    function validate() {
      errors.value = {};
      if (!form.value.name.trim()) {
        errors.value.name = 'Nome é obrigatório.';
      }
      if (!form.value.email.trim()) {
        errors.value.email = 'Email é obrigatório.';
      } else if (!/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/.test(form.value.email)) {
        errors.value.email = 'Email inválido.';
      }
      if (!form.value.password) {
        errors.value.password = 'Senha é obrigatória.';
      } else if (form.value.password.length < 6) {
        errors.value.password = 'A senha deve ter pelo menos 6 caracteres.';
      }
      return Object.keys(errors.value).length === 0;
    }

    async function register() {
      apiError.value = '';
      success.value = false;
      if (!validate()) return;
      loading.value = true;
      try {
        // Simulação de chamada à API
        await new Promise((resolve, reject) => setTimeout(() => {
          if (form.value.email === 'jaexiste@email.com') {
            reject(new Error('Email já cadastrado.'));
          } else {
            resolve(true);
          }
        }, 1200));
        success.value = true;
        setTimeout(() => router.push('/auth/login'), 1500);
      } catch (err: any) {
        apiError.value = err.message || 'Erro ao registrar.';
      } finally {
        loading.value = false;
      }
    }

    return { form, errors, loading, apiError, success, register };
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