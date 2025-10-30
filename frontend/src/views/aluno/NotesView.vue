<template>
  <div class="notes-root">
    <div class="container">
      <div class="heading">
        <h1 class="title">Minhas Anotações</h1>
        <p class="subtitle">Organize seu conhecimento</p>
      </div>
      <div class="grid">
        <div class="sidebar">
          <GlassCard class="h-full">
            <div class="flex justify-between items-center mb-6">
              <h2 class="text-xl font-bold">Anotações</h2>
              <button @click="createNewNote" class="bg-emerald-600 hover:bg-emerald-500 w-8 h-8 rounded-full flex items-center justify-center">
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
          <GlassCard class="h-full flex flex-col">
            <NoteEditor 
              v-if="selectedNote" 
              :note="selectedNote" 
              @save="saveNote"
              @delete="deleteNote"
            />
            <div v-else class="flex flex-col items-center justify-center h-full text-gray-500 py-20">
              <i class="fas fa-sticky-note text-5xl mb-4 opacity-30"></i>
              <p class="text-xl">Selecione uma anotação ou crie uma nova</p>
              <button @click="createNewNote" class="mt-6 px-6 py-3 bg-emerald-600 hover:bg-emerald-500 rounded-lg transition-colors">
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
.notes-root { background:#fcfcfc; color:#17181e; min-height:100vh; padding:2rem 0; }
.container { max-width:1100px; margin:0 auto; padding:0 1rem; }
.heading { text-align:center; margin-bottom:1.25rem; }
.title { font-size:2rem; font-weight:800; }
.subtitle { color:#6b6b6b; }
.grid { display:grid; grid-template-columns: 1fr; gap:1rem; }
.sidebar { grid-column: 1; }
.content { grid-column: 1; }
@media (min-width: 1024px) { .grid { grid-template-columns: 1fr 3fr; } .sidebar { grid-column:auto; } .content{ grid-column:auto; } }
</style>