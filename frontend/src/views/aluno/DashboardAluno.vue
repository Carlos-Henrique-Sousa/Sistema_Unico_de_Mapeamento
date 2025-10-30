<template>
  <div class="dashboard-root">
    <header class="header">
      <div>
        <h1 class="title">Meu Dashboard</h1>
        <p class="subtitle">Visão geral do seu desempenho</p>
      </div>
    </header>

    <section class="cards-grid">
      <div class="card kpi">
        <div class="kpi-label">Atividades Pendentes</div>
        <div class="kpi-value accent-blue">5</div>
      </div>
      <div class="card kpi">
        <div class="kpi-label">Próxima Prova</div>
        <div class="kpi-value">02/12</div>
      </div>
      <div class="card kpi">
        <div class="kpi-label">Desempenho</div>
        <div class="kpi-value accent-green">85%</div>
        <div class="bar"><span style="width:85%"></span></div>
      </div>
    </section>

    <section class="panels">
      <div class="card panel">
        <h3 class="panel-title">Atalhos Rápidos</h3>
        <div class="quick-actions">
          <router-link class="qa" to="/aluno/activities">Atividades</router-link>
          <router-link class="qa" to="/aluno/exams">Provas</router-link>
          <router-link class="qa" to="/aluno/notes">Anotações</router-link>
          <router-link class="qa" to="/aluno/classroom">Minha Sala</router-link>
        </div>
      </div>
      <div class="card panel">
        <h3 class="panel-title">Resumo Semanal</h3>
        <ul class="list">
          <li><span>Atividades entregues</span><b>7</b></li>
          <li><span>Tempo de estudo</span><b>4h 20m</b></li>
          <li><span>Mensagens no chat</span><b>12</b></li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.dashboard-root { padding: 2rem; background:#fcfcfc; color:#17181e; }
.header { display:flex; align-items:center; justify-content:space-between; margin-bottom:1.25rem; }
.title { font-size: 2rem; font-weight: 800; letter-spacing:-0.01em; }
.subtitle { color:#6b6b6b; margin-top:0.25rem; }

.cards-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap:1rem; margin-bottom:1rem; }
.card { background:#fcfcfc; border:1.5px solid rgba(23,24,30,0.08); border-radius:14px; padding:1rem; }
.kpi { display:flex; flex-direction:column; gap:0.5rem; }
.kpi-label { color:#6b6b6b; font-size:0.9rem; }
.kpi-value { font-size:1.9rem; font-weight:800; line-height:1; }
.accent-blue { color:#0f1e3f; }
.accent-green { color:#2d531a; }
.bar { margin-top:0.25rem; height:6px; background:rgba(23,24,30,0.06); border-radius:999px; overflow:hidden; }
.bar span { display:block; height:100%; background:#2d531a; }

.panels { display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:1rem; }
.panel-title { font-size:1rem; font-weight:700; margin-bottom:0.75rem; }
.quick-actions { display:flex; flex-wrap:wrap; gap:0.5rem; }
.qa { padding:0.5rem 0.75rem; border:1.5px solid rgba(23,24,30,0.12); border-radius:10px; color:#17181e; text-decoration:none; background:#fcfcfc; }
.qa:hover { border-color:rgba(23,24,30,0.25); }
.list { display:flex; flex-direction:column; gap:0.5rem; }
.list li { display:flex; align-items:center; justify-content:space-between; padding:0.35rem 0; color:#17181e; }
.list span { color:#6b6b6b; }
</style>
