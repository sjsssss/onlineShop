// composables/useSlides.js
import { ref, onMounted } from 'vue'
import axios from 'axios'

export function useSlides() {
  const slides = ref([])

  onMounted(async () => {
    const res = await axios.get('/api/carousel')
    slides.value = res.data
  })

  return { slides }
}
