<template>
  <div class="summary-card bg-gradient-to-br rounded-2xl p-6" :class="color">
    <div class="flex justify-between items-start">
      <div>
        <h3 class="text-lg font-semibold mb-2">{{ title }}</h3>
        <p class="text-3xl font-bold">{{ value }}</p>
      </div>
      <div class="bg-white/20 p-3 rounded-xl">
        <i :class="icon" class="text-xl"></i>
      </div>
    </div>
    <div class="mt-4">
      <div class="h-2 bg-white/20 rounded-full overflow-hidden">
        <div class="h-full bg-white rounded-full" :style="{ width: progress + '%' }"></div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'SummaryCard',
  props: {
    title: { type: String, required: true },
    value: { type: [String, Number], required: true },
    icon: { type: String, required: true },
    color: { type: String, default: 'bg-cyan-600' },
    progress: { type: Number, default: 0 }
  }
});
</script>