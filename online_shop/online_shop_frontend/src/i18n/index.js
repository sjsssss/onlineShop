import { createI18n } from 'vue-i18n'
import ja from './ja.json'
import zh from './zh.json'

// 从 localStorage 中读取语言设置，默认为日语
const savedLocale = localStorage.getItem('locale') || 'ja'

const i18n = createI18n({
  legacy: false,
  locale: savedLocale,
  fallbackLocale: 'ja',
  messages: {
    ja,
    zh,
  },
})

export default i18n
