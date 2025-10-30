<template>
  <div class="chat-root">
    <div class="container">
      <div class="heading">
        <h1 class="title">Chat Educacional</h1>
        <p class="subtitle">Converse com colegas e professores</p>
      </div>

      <div class="grid">
        <!-- Lista de Contatos -->
        <div class="sidebar">
          <GlassCard class="h-full flex flex-col blue-glass">
            <div class="flex justify-between items-center mb-7">
              <h2 class="text-xl font-extrabold">Contatos</h2>
              <div class="relative">
                <input 
                  v-model="search" 
                  type="text" 
                  placeholder="Buscar..." 
                  class="search" />
                <i class="fas fa-search absolute left-4 top-4 text-blue-500"></i>
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
        <div class="content">
          <GlassCard class="h-full flex flex-col blue-glass">
            <ChatWindow 
              v-if="activeContact" 
              :contact="activeContact" 
            />
            <div v-else class="flex flex-col items-center justify-center h-full text-blue-400 py-20">
              <i class="fas fa-comments text-5xl mb-4 opacity-15"></i>
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

<style scoped>
.chat-root { background:var(--cor-fundo); color:var(--cor-primaria); min-height:100vh; padding:2.5rem 0; }
.container { max-width:1100px; margin:0 auto; padding:0 1rem; }
.heading { text-align:center; margin-bottom:2rem; }
.title { font-size:2.1rem; font-weight:900; color:var(--cor-primaria); }
.subtitle { color:var(--cor-azul-light); }
.grid { display:grid; grid-template-columns:1fr; gap:1.2rem; }
.sidebar { grid-column:1; }
.content { grid-column:1; }
.blue-glass { background:rgba(52, 152, 219, 0.08) !important; border:1.4px solid var(--cor-azul-prim) !important; }
.search { background:var(--cor-fundo); border:1.5px solid var(--cor-azul-prim); border-radius:12px; padding:0.62rem 0.9rem 0.62rem 2.6rem; color:var(--cor-primaria); font-weight:600; min-width:142px; outline:none; font-size:1.08rem; }
@media (min-width:1024px){ .grid { grid-template-columns:1.05fr 2.95fr; }}
@media(max-width:700px){ .container{padding:0 2vw;} .grid{grid-template-columns:1fr;}}
</style>