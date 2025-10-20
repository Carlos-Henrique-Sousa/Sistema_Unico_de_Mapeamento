<template>
  <div class="chat-view bg-gradient-to-br from-gray-900 to-black min-h-screen text-white py-10">
    <div class="container mx-auto px-4">
      <div class="text-center mb-10">
        <h1 class="text-4xl font-bold mb-2 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-cyan-400">
          Chat Educacional
        </h1>
        <p class="text-gray-400">Converse com colegas e professores</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-4 gap-8">
        <!-- Lista de Contatos -->
        <div class="lg:col-span-1">
          <GlassCard class="h-full flex flex-col">
            <div class="flex justify-between items-center mb-6">
              <h2 class="text-xl font-bold">Contatos</h2>
              <div class="relative">
                <input 
                  v-model="search" 
                  type="text" 
                  placeholder="Buscar..." 
                  class="bg-gray-800 rounded-lg pl-10 pr-4 py-2 focus:outline-none focus:ring-2 focus:ring-cyan-500"
                >
                <i class="fas fa-search absolute left-3 top-3 text-gray-500"></i>
              </div>
            </div>
            
            <div class="space-y-3 flex-1 overflow-y-auto">
              <ContactItem 
                v-for="contact in filteredContacts" 
                :key="contact.id"
                :contact="contact"
                :active="activeContact?.id === contact.id"
                @click="selectContact(contact)"
              />
            </div>
          </GlassCard>
        </div>

        <!-- Área de Conversa -->
        <div class="lg:col-span-3">
          <GlassCard class="h-full flex flex-col">
            <ChatWindow 
              v-if="activeContact" 
              :contact="activeContact" 
            />
            <div v-else class="flex flex-col items-center justify-center h-full text-gray-500 py-20">
              <i class="fas fa-comments text-5xl mb-4 opacity-30"></i>
              <p class="text-xl">Selecione um contato para iniciar uma conversa</p>
            </div>
          </GlassCard>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import GlassCard from '@/shared/GlassCard.vue';
import ContactItem from '@/components/communication/ContactItem.vue';
import ChatWindow from '@/components/communication/ChatWindow.vue';

interface Contact {
  id: number;
  name: string;
  role: 'Professor' | 'Aluno' | 'PDT';
  avatar: string;
  lastMessage: string;
  unread: number;
  online: boolean;
}

export default defineComponent({
  name: 'ChatView',
  components: { GlassCard, ContactItem, ChatWindow },
  setup() {
    const contacts = ref<Contact[]>([
      { id: 1, name: 'Prof. Mariana Silva', role: 'Professor', avatar: '', lastMessage: 'Não esqueça da atividade de...', unread: 2, online: true },
      { id: 2, name: 'Carlos Oliveira', role: 'Aluno', avatar: '', lastMessage: 'Você fez o exercício 5?', unread: 0, online: true },
      { id: 3, name: 'Ana Beatriz (PDT)', role: 'PDT', avatar: '', lastMessage: 'Seu relatório foi analisado...', unread: 1, online: false }
    ]);
    const search = ref('');
    const activeContact = ref<Contact | null>(null);
    const filteredContacts = computed(() => {
      if (!search.value) return contacts.value;
      return contacts.value.filter(c => c.name.toLowerCase().includes(search.value.toLowerCase()));
    });
    const selectContact = (contact: Contact) => {
      activeContact.value = contact;
      contact.unread = 0;
    };
    return { contacts, search, filteredContacts, activeContact, selectContact };
  },
});
</script>