<template>
  <div class="dashboard-root">
    <header class="header">
      <div>
        <h1 class="title">Meu Dashboard</h1>
        <p class="subtitle">Visão geral do seu desempenho</p>
      </div>
      <div class="avatar-wrap">
        <img class="avatar" src="/src/assets/logo.png" alt="Perfil" />
      </div>
    </header>
    <section class="cards-grid">
      <div class="card kpi kpi-blue-glass">
        <div class="kpi-label">Atividades Pendentes</div>
        <div class="kpi-value accent-blue">5</div>
      </div>
      <div class="card kpi kpi-glass">
        <div class="kpi-label">Próxima Prova</div>
        <div class="kpi-value accent-azul">02/12</div>
      </div>
      <div class="card kpi kpi-glass">
        <div class="kpi-label">Desempenho</div>
        <div class="kpi-value accent-green">85%</div>
        <div class="bar"><span style="width:85%; background:var(--cor-azul-sec)"></span></div>
      </div>
    </section>
    <section class="panels">
      <div class="card panel kpi-glass">
        <h3 class="panel-title">Atalhos Rápidos</h3>
        <div class="quick-actions">
          <router-link class="qa button-main" to="/aluno/activities">Atividades</router-link>
          <router-link class="qa button-main" to="/aluno/exams">Provas</router-link>
          <router-link class="qa button-main" to="/aluno/notes">Anotações</router-link>
          <router-link class="qa button-main" to="/aluno/classroom">Minha Sala</router-link>
        </div>
      </div>
      <div class="card panel kpi-glass">
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
.dashboard-root { padding: 2rem; min-height: 100vh; background: var(--cor-fundo); color: var(--cor-primaria); }
.header { display:flex; align-items:center; justify-content:space-between; margin-bottom:1.25rem; }
.title { font-size: 2.1rem; font-weight: 900; color: var(--cor-primaria); letter-spacing:-0.01em; }
.subtitle { color: var(--cor-azul-light); margin-top:0.25rem; font-size:1.08rem; font-weight:600; }
.avatar-wrap { margin-left:2rem; }
.avatar { width:48px; height:48px; border-radius:16px; box-shadow:0 2px 18px rgba(58,134,255,0.12); border:2px solid var(--cor-azul-prim); background:#fff; }
.cards-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:1.2rem; margin-bottom:1.2rem; }
.card { border-radius:18px; padding:1.3rem 1.2rem; box-shadow:0 3px 18px rgba(23,24,30,0.18),0 1.5px 6px rgba(58,134,255,0.054); }
.kpi-glass { background:rgba(255,255,255,0.07); border:1.4px solid rgba(52,152,219,0.18); }
.kpi-blue-glass { background:rgba(58,134,255,0.09); border:1.4px solid var(--cor-azul-prim); }
.kpi-label { color: var(--cor-cinza); font-size:1.1rem; font-weight:600; text-transform:uppercase; }
.kpi-value { font-size:2.2rem; font-weight:900; margin:10px 0 0 0; }
.accent-blue { color: var(--cor-azul-prim); }
.accent-green { color: #50fa7b; }
.bar { margin-top:0.4rem; height:7px; background:rgba(52,152,219,0.19); border-radius:999px; overflow:hidden; }
.bar span { display:block; height:100%; background:var(--cor-azul-prim); border-radius:998px; }
.panels { display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:1.1rem; }
.panel-title { font-size:1.07rem; font-weight:700; margin-bottom:0.7rem; color:var(--cor-primaria); }
.quick-actions { display:flex; flex-wrap:wrap; gap:0.5rem; }
.qa { font-size:1.01rem; min-width:117px; justify-content:center; align-items:center; display:inline-flex; text-align:center; border:none; margin-bottom:2px; }
.list { display:flex; flex-direction:column; gap:0.5rem; }
.list li { display:flex; align-items:center; justify-content:space-between; padding:0.38rem 0; color:var(--cor-primaria); font-size:1rem; font-weight: 600; }
.list span { color:var(--cor-cinza); font-size:0.97rem; font-weight:500; }
@media(max-width: 700px) {.dashboard-root { padding:1rem 2vw; }.cards-grid, .panels {grid-template-columns: 1fr;}}
</style>
