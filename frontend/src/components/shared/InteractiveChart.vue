<template>
  <div class="chart-wrapper">
    <div v-if="title || $slots.actions" class="chart-header">
      <div class="chart-title-section">
        <h3 v-if="title" class="chart-title">{{ title }}</h3>
        <p v-if="subtitle" class="chart-subtitle">{{ subtitle }}</p>
      </div>
      <div v-if="$slots.actions" class="chart-actions">
        <slot name="actions"></slot>
      </div>
    </div>
    
    <div class="chart-controls" v-if="chartTypes.length > 1">
      <button 
        v-for="type in chartTypes" 
        :key="type"
        @click="currentType = type"
        :class="['control-btn', { active: currentType === type }]"
      >
        <svg v-if="type === 'line'" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
        </svg>
        <svg v-else-if="type === 'bar'" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="3" y="3" width="7" height="18"/>
          <rect x="14" y="8" width="7" height="13"/>
        </svg>
        <svg v-else-if="type === 'pie'" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"/>
          <path d="M12 2v10l6 6"/>
        </svg>
        <span>{{ type }}</span>
      </button>
    </div>
    
    <div class="chart-container" ref="chartContainer">
      <canvas ref="chartCanvas"></canvas>
      
      <div v-if="loading" class="chart-loading">
        <div class="spinner"></div>
        <p>Carregando dados...</p>
      </div>
      
      <div v-if="!loading && (!data || data.datasets?.length === 0)" class="chart-empty">
        <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
          <line x1="9" y1="9" x2="15" y2="15"/>
          <line x1="15" y1="9" x2="9" y2="15"/>
        </svg>
        <p>Nenhum dado disponível</p>
      </div>
    </div>
    
    <div v-if="showLegend && data?.datasets" class="chart-legend">
      <div 
        v-for="(dataset, index) in data.datasets" 
        :key="index"
        class="legend-item"
        @click="toggleDataset(index)"
        :class="{ 'legend-disabled': hiddenDatasets.includes(index) }"
      >
        <span 
          class="legend-color" 
          :style="{ background: dataset.backgroundColor || dataset.borderColor }"
        ></span>
        <span class="legend-label">{{ dataset.label }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, nextTick } from 'vue'

const props = defineProps({
  data: {
    type: Object,
    required: true
  },
  type: {
    type: String,
    default: 'line',
    validator: (value) => ['line', 'bar', 'pie', 'doughnut', 'radar'].includes(value)
  },
  chartTypes: {
    type: Array,
    default: () => []
  },
  options: {
    type: Object,
    default: () => ({})
  },
  title: {
    type: String,
    default: ''
  },
  subtitle: {
    type: String,
    default: ''
  },
  showLegend: {
    type: Boolean,
    default: true
  },
  loading: {
    type: Boolean,
    default: false
  },
  responsive: {
    type: Boolean,
    default: true
  },
  animated: {
    type: Boolean,
    default: true
  }
})

const chartCanvas = ref(null)
const chartContainer = ref(null)
const currentType = ref(props.type)
const hiddenDatasets = ref([])
const chart = ref(null)

const defaultOptions = {
  responsive: true,
  maintainAspectRatio: true,
  aspectRatio: 2,
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      backgroundColor: 'rgba(0, 0, 0, 0.8)',
      padding: 12,
      borderRadius: 8,
      titleFont: {
        size: 14,
        weight: 'bold'
      },
      bodyFont: {
        size: 13
      }
    }
  },
  animation: {
    duration: 750,
    easing: 'easeInOutQuart'
  }
}

onMounted(() => {
  if (props.data && !props.loading) {
    renderChart()
  }
})

watch(() => props.data, () => {
  if (!props.loading) {
    renderChart()
  }
}, { deep: true })

watch(() => props.loading, (newVal) => {
  if (!newVal && props.data) {
    nextTick(() => renderChart())
  }
})

watch(currentType, () => {
  renderChart()
})

const renderChart = () => {
  if (!chartCanvas.value || props.loading) return
  
  // Simulação de renderização (substitua com Chart.js real)
  const ctx = chartCanvas.value.getContext('2d')
  
  // Limpar canvas
  ctx.clearRect(0, 0, chartCanvas.value.width, chartCanvas.value.height)
  
  // Desenhar gráfico simples de demonstração
  const width = chartCanvas.value.width
  const height = chartCanvas.value.height
  
  if (currentType.value === 'line' || currentType.value === 'bar') {
    drawLineOrBar(ctx, width, height)
  } else if (currentType.value === 'pie' || currentType.value === 'doughnut') {
    drawPie(ctx, width, height)
  }
}

const drawLineOrBar = (ctx, width, height) => {
  const padding = 40
  const graphWidth = width - padding * 2
  const graphHeight = height - padding * 2
  
  // Eixos
  ctx.strokeStyle = '#e5e7eb'
  ctx.lineWidth = 2
  ctx.beginPath()
  ctx.moveTo(padding, padding)
  ctx.lineTo(padding, height - padding)
  ctx.lineTo(width - padding, height - padding)
  ctx.stroke()
  
  // Dados de exemplo
  if (props.data?.datasets && props.data.datasets.length > 0) {
    props.data.datasets.forEach((dataset, datasetIndex) => {
      if (hiddenDatasets.value.includes(datasetIndex)) return
      
      const data = dataset.data || []
      const color = dataset.backgroundColor || dataset.borderColor || '#667eea'
      
      if (currentType.value === 'line') {
        ctx.strokeStyle = color
        ctx.lineWidth = 3
        ctx.beginPath()
        
        data.forEach((value, index) => {
          const x = padding + (graphWidth / (data.length - 1)) * index
          const y = height - padding - (value / 100) * graphHeight
          
          if (index === 0) {
            ctx.moveTo(x, y)
          } else {
            ctx.lineTo(x, y)
          }
        })
        
        ctx.stroke()
        
        // Pontos
        data.forEach((value, index) => {
          const x = padding + (graphWidth / (data.length - 1)) * index
          const y = height - padding - (value / 100) * graphHeight
          
          ctx.fillStyle = color
          ctx.beginPath()
          ctx.arc(x, y, 5, 0, Math.PI * 2)
          ctx.fill()
        })
      } else if (currentType.value === 'bar') {
        const barWidth = graphWidth / data.length * 0.6
        
        data.forEach((value, index) => {
          const x = padding + (graphWidth / data.length) * index + (graphWidth / data.length - barWidth) / 2
          const barHeight = (value / 100) * graphHeight
          const y = height - padding - barHeight
          
          ctx.fillStyle = color
          ctx.fillRect(x, y, barWidth, barHeight)
        })
      }
    })
  }
}

const drawPie = (ctx, width, height) => {
  const centerX = width / 2
  const centerY = height / 2
  const radius = Math.min(width, height) / 2 - 40
  
  if (props.data?.datasets && props.data.datasets[0]?.data) {
    const data = props.data.datasets[0].data
    const total = data.reduce((sum, val) => sum + val, 0)
    const colors = props.data.datasets[0].backgroundColor || [
      '#667eea', '#764ba2', '#f093fb', '#4facfe', '#43e97b'
    ]
    
    let startAngle = -Math.PI / 2
    
    data.forEach((value, index) => {
      if (hiddenDatasets.value.includes(index)) return
      
      const sliceAngle = (value / total) * Math.PI * 2
      
      ctx.fillStyle = colors[index] || colors[0]
      ctx.beginPath()
      ctx.moveTo(centerX, centerY)
      ctx.arc(centerX, centerY, radius, startAngle, startAngle + sliceAngle)
      ctx.closePath()
      ctx.fill()
      
      startAngle += sliceAngle
    })
    
    // Buraco para doughnut
    if (currentType.value === 'doughnut') {
      ctx.fillStyle = '#ffffff'
      ctx.beginPath()
      ctx.arc(centerX, centerY, radius * 0.6, 0, Math.PI * 2)
      ctx.fill()
    }
  }
}

const toggleDataset = (index) => {
  const idx = hiddenDatasets.value.indexOf(index)
  if (idx > -1) {
    hiddenDatasets.value.splice(idx, 1)
  } else {
    hiddenDatasets.value.push(index)
  }
  renderChart()
}
</script>

<style scoped>
.chart-wrapper {
  background: white;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
  gap: 1rem;
}

.chart-title-section {
  flex: 1;
}

.chart-title {
  margin: 0 0 0.25rem 0;
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
}

.chart-subtitle {
  margin: 0;
  font-size: 0.875rem;
  color: #6b7280;
}

.chart-actions {
  display: flex;
  gap: 0.5rem;
}

.chart-controls {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  padding: 0.5rem;
  background: #f9fafb;
  border-radius: 0.75rem;
  flex-wrap: wrap;
}

.control-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1rem;
  border: 2px solid transparent;
  background: white;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 500;
  color: #6b7280;
  text-transform: capitalize;
}

.control-btn:hover {
  background: #f3f4f6;
}

.control-btn.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-color: transparent;
}

.control-btn svg {
  width: 20px;
  height: 20px;
}

.chart-container {
  position: relative;
  min-height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}

canvas {
  max-width: 100%;
  height: auto;
}

.chart-loading,
.chart-empty {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  color: #9ca3af;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f4f6;
  border-top-color: #667eea;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.chart-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid #e5e7eb;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  padding: 0.5rem 0.75rem;
  border-radius: 0.5rem;
  transition: all 0.2s;
}

.legend-item:hover {
  background: #f9fafb;
}

.legend-item.legend-disabled {
  opacity: 0.4;
}

.legend-item.legend-disabled .legend-color {
  background: #d1d5db !important;
}

.legend-color {
  width: 16px;
  height: 16px;
  border-radius: 0.25rem;
  flex-shrink: 0;
}

.legend-label {
  font-size: 0.875rem;
  color: #374151;
  font-weight: 500;
}

@media (max-width: 768px) {
  .chart-wrapper {
    padding: 1rem;
  }
  
  .chart-header {
    flex-direction: column;
  }
  
  .chart-controls {
    overflow-x: auto;
    flex-wrap: nowrap;
  }
}
</style>