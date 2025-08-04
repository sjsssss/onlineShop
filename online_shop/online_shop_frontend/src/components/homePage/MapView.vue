<!-- src/components/MapView.vue -->
<template>
  <div>
    <div id="map" style="height: 400px;"></div>
    <div style="text-align: center; margin-top: 10px;">
      <a
        class="btn btn-outline-primary btn-sm"
        :href="googleMapsUrl"
        target="_blank"
        rel="noopener noreferrer"
      >
        Google マップで開く
      </a>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

// 公司地址的经纬度（埼玉県草加市氷川町）
const lat = 35.8366
const lng = 139.8034

// Google Maps URL（新标签页中打开）
const googleMapsUrl = ref(`https://www.google.com/maps?q=${lat},${lng}`)

const initMap = () => {
  const map = L.map('map').setView([lat, lng], 20)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map)

  L.marker([lat, lng]).addTo(map)
    .bindPopup('巧巧屋物産')
    .openPopup()
}

onMounted(() => {
  initMap()
})
</script>

<style scoped>
.btn {
  font-size: 0.85rem;
}
</style>
