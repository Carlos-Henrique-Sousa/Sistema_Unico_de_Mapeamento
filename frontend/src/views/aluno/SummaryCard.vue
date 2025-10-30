<template>
  <div class="summary-root">
    <div class="row">
      <div>
        <h3 class="title">{{ title }}</h3>
        <p class="value">{{ value }}</p>
      </div>
      <div class="icon-wrap">
        <i :class="icon" class="icon"></i>
      </div>
    </div>
    <div class="bar"><span :style="{ width: progress + '%' }"></span></div>
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
    color: { type: String, default: '#0f1e3f' },
    progress: { type: Number, default: 0 }
  }
});
</script>

<style scoped>
.summary-root { background:#fcfcfc; border:1.5px solid rgba(23,24,30,0.08); border-radius:14px; padding:1rem; color:#17181e; }
.row { display:flex; align-items:flex-start; justify-content:space-between; }
.title { font-size:0.95rem; color:#6b6b6b; margin-bottom:0.25rem; }
.value { font-size:1.6rem; font-weight:800; }
.icon-wrap { background:rgba(23,24,30,0.06); border:1px solid rgba(23,24,30,0.1); border-radius:12px; padding:0.5rem; }
.icon { font-size:1.1rem; }
.bar { margin-top:0.75rem; height:6px; background:rgba(23,24,30,0.06); border-radius:999px; overflow:hidden; }
.bar span { display:block; height:100%; background:#2d531a; }
</style>