import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
// src/main.js
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import BootstrapVue3 from 'bootstrap-vue-3'

// 语言切换组件
import { createI18n } from 'vue-i18n'
import ja from './locales/ja.json'
import zh from './locales/zh.json'
const savedLang = localStorage.getItem('lang') || 'ja'
const i18n = createI18n({
  locale: localStorage.getItem('lang') || 'ja',
  locale: savedLang,
  fallbackLocale: 'ja',
  messages: {
    ja,
    zh,
  },
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(BootstrapVue3)
app.use(i18n)
app.mount('#app')



