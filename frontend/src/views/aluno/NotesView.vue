<template>
  <div class="notes-root">
    <div class="container">
      <div class="heading">
        <h1 class="title">Minhas Anotações</h1>
        <p class="subtitle">Organize seu conhecimento</p>
      </div>
      <div class="grid">
        <div class="sidebar">
          <GlassCard class="h-full blue-glass">
            <div class="flex justify-between items-center mb-7">
              <h2 class="text-xl font-extrabold">Anotações</h2>
              <button @click="createNewNote" class="button-main w-10 h-10 rounded-full flex items-center justify-center !py-0 !px-0">
                <i class="fas fa-plus"></i>
              </button>
            </div>
            <div class="space-y-3">
              <NoteItem 
                v-for="note in notes" 
                :key="note.id"
                :note="note"
                :active="selectedNote?.id === note.id"
                @click="selectNote(note)"
              />
            </div>
          </GlassCard>
        </div>
        <div class="content">
          <GlassCard class="h-full flex flex-col blue-glass">
            <NoteEditor 
              v-if="selectedNote" 
              :note="selectedNote" 
              @save="saveNote"
              @delete="deleteNote"
            />
            <div v-else class="flex flex-col items-center justify-center h-full text-blue-400 py-20">
              <i class="fas fa-sticky-note text-5xl mb-4 opacity-20"></i>
              <p class="text-xl">Selecione uma anotação ou crie uma nova</p>
              <button @click="createNewNote" class="mt-6 px-6 py-3 button-main rounded-lg transition-colors">
                Criar Nova Anotação
              </button>
            </div>
          </GlassCard>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import GlassCard from '@/shared/GlassCard.vue';
import NoteItem from '@/components/notes/NoteItem.vue';
import NoteEditor from '@/components/notes/NoteEditor.vue';

interface Note {
  id: number;
  title: string;
  content: string;
  subject: string;
  createdAt: string;
  updatedAt: string;
}

export default defineComponent({
  name: 'NotesView',
  components: { GlassCard, NoteItem, NoteEditor },
  setup() {
    const notes = ref<Note[]>([
      { 
        id: 1, 
        title: 'Álgebra Linear', 
        content: 'Conceitos básicos de matrizes...', 
        subject: 'Matemática',
        createdAt: '2023-10-15',
        updatedAt: '2023-10-18'
      },
      { 
        id: 2, 
        title: 'Revolução Industrial', 
        content: 'Impactos na sociedade...', 
        subject: 'História',
        createdAt: '2023-10-20',
        updatedAt: '2023-10-20'
      }
    ]);
    const selectedNote = ref<Note | null>(null);
    const selectNote = (note: Note) => { selectedNote.value = { ...note }; };
    const createNewNote = () => {
      const newNote: Note = {
        id: Date.now(),
        title: 'Nova Anotação',
        content: '',
        subject: 'Geral',
        createdAt: new Date().toISOString().split('T')[0],
        updatedAt: new Date().toISOString().split('T')[0]
      };
      notes.value.unshift(newNote);
      selectedNote.value = newNote;
    };
    const saveNote = (updatedNote: Note) => {
      const index = notes.value.findIndex(n => n.id === updatedNote.id);
      if (index !== -1) {
        notes.value[index] = { 
          ...updatedNote, 
          updatedAt: new Date().toISOString().split('T')[0]
        };
      }
    };
    const deleteNote = (noteId: number) => {
      notes.value = notes.value.filter(n => n.id !== noteId);
      if (selectedNote.value?.id === noteId) {
        selectedNote.value = null;
      }
    };
    return { notes, selectedNote, selectNote, createNewNote, saveNote, deleteNote };
  },
});
</script>

<style scoped>
.notes-root { background:var(--cor-fundo); color:var(--cor-primaria); min-height:100vh; padding:2.2rem 0; }
.container { max-width:1100px; margin:0 auto; padding:0 1rem; }
.heading { text-align:center; margin-bottom:2rem; }
.title { font-size:2.15rem; font-weight:900; color:var(--cor-primaria); }
.subtitle { color:var(--cor-azul-light); }
.grid { display:grid; grid-template-columns: 1fr; gap:1.22rem; }
.sidebar { grid-column: 1; }
.content { grid-column: 1; }
@media (min-width: 1024px) { .grid { grid-template-columns: 1fr 2.8fr; } .sidebar { grid-column:auto; } .content{ grid-column:auto; } }
.blue-glass { background:rgba(52,152,219,0.11) !important; border:1.5px solid var(--cor-azul-prim) !important; box-shadow:0 3.5px 19px rgba(52,152,219,0.13) !important; }
.button-main{ background:var(--cor-azul-prim); color:var(--cor-primaria); border-radius: 12px; font-weight: 700; box-shadow: 0 2px 20px rgba(58,134,255,0.10); padding: 10px 24px; transition: background 0.15s, box-shadow 0.15s; border:none; outline:none; }
.button-main:hover{ background:var(--cor-azul-sec); box-shadow: 0 6px 24px rgba(58,134,255,0.12); }
@media(max-width:700px){ .container{padding:0 2vw;} }
</style>