<template>
  <div class="classroom-view">
    <h1>Minha Sala de Aula</h1>
    <p>Sala 1A - Professora Mariana</p>
    <div class="map-container card-style">
      <ClassroomMap2D 
        :rows="5" :cols="8"
        :groupMode="'single'"
        :snapToGrid="true"
        :students="[]"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import ClassroomMap2D from '@/components/classroom/ClassroomMap2D.vue'
</script>

<style scoped>
.classroom-view { padding: 2.3rem 0; background:var(--cor-fundo); color:var(--cor-primaria); min-height:100vh; }
.classroom-view h1 { font-size: 2.1rem; margin-bottom: 0.35rem; font-weight:900; color:var(--cor-primaria); }
.classroom-view p { color: var(--cor-azul-light); margin-bottom: 1.2rem; font-size:1.15rem; font-weight:500; letter-spacing:0.01em; }
.map-container { padding:1.5rem 0.85rem 1rem 0.85rem; }
@media(max-width:700px){ .classroom-view{padding:1rem 2vw;} .map-container{padding:0.7rem;}}
</style>
