<template>
  <div class="classroom-view">
    <h1>Minha Sala de Aula</h1>
    <p>Sala 1A - Professora Mariana</p>
    <div class="map-container">
      <ClassroomMap2D 
        :rows="5"
        :cols="8"
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
.classroom-view { padding: 2rem; background:#fcfcfc; color:#17181e; }
.classroom-view h1 { font-size: 2rem; margin-bottom: 0.25rem; }
.classroom-view p { color: #6b6b6b; margin-bottom: 1rem; }
.map-container { background:#fcfcfc; border:1.5px solid rgba(23,24,30,0.08); border-radius:14px; padding: 0.75rem; }
</style>
