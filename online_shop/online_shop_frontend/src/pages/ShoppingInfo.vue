<template>
  <div class="home-container">
    <SideCategory class="side-category" v-show="!isMobile || showSidebar" />

    <div class="main-content">
      <!-- <Carousel :slides="slides" /> -->

      <!-- 分类按钮 -->
      <div class="faq-buttons">
        <button @click="scrollTo('order')">{{ $t('order_guide.title') }}</button>
        <button @click="scrollTo('membership')">{{ $t('membership.title') }}</button>
        <button @click="scrollTo('point')">{{ $t('point.title') }}</button>
      </div>

      <!-- FAQ 各区块 -->
      <section class="faq-section">
        <h2 id="order">{{ $t('order_guide.title') }}</h2>
        <h3 class="intro-text">{{ $t('order_guide.intro') }}</h3>
        <div v-for="item in faq.order" :key="item.id" class="faq-item">
          <p class="question">{{ $t(`order_guide.${item.q}`) }}</p>
          <p class="answer">　・{{ $t(`order_guide.${item.a}`) }}</p>
        </div>

        <h2 id="membership">{{ $t('membership.title') }}</h2>
        <h3 class="intro-text">　　{{ $t('membership.intro') }}</h3>
        <h3 class="intro-text">　　{{ $t('membership.benefit') }}</h3>
        <div v-for="item in faq.membership" :key="item.id" class="faq-item">
        <p class="question">{{ $t(`membership.${item.q}`) }}</p>
        <p class="answer" v-html="`　　・${$t(`membership.${item.a}`)}`"></p>
        </div>


        <h2 id="point">{{ $t('point.title') }}</h2>
        <div v-for="item in faq.point" :key="item.id" class="faq-item">
          <p class="question">■ {{ $t(`point.${item.q}`) }}</p>
          <p class="answer">　・{{ $t(`point.${item.a}`) }}</p>
        </div>
        <h3 class="intro-text">　　{{ $t('point.note') }}</h3>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import SideCategory from '../components/common/SideCategory.vue'
import Carousel from '../components/common/Carousel.vue'

const scrollTo = (id) => {
  const el = document.getElementById(id)
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}

// 映射 language JSON 中的 key（语言包中应包含这些 key）
const faq = ref({
  order: [
    { id: 1, q: 'step1_title', a: 'step1_text' },
    { id: 2, q: 'step2_title', a: 'step2_text' },
    { id: 3, q: 'step3_title', a: 'step3_text' },
    { id: 4, q: 'step4_title', a: 'step4_text' },
    { id: 5, q: 'step5_title', a: 'step5_text' },
    { id: 6, q: 'step6_title', a: 'step6_text' }
  ],
  membership: [
    { id: 7, q: 'edit_title', a: 'edit_text' },
    { id: 8, q: 'password_title', a: 'password_reset' },
    { id: 10, q: 'service_title', a: 'service_text' },
    { id: 12, q: 'newsletter_title', a: 'newsletter_text' },
    { id: 16, q: 'withdraw_title', a: 'withdraw_text' }
  ],
  point: [
    { id: 16, q: 'title', a: 'text' },
  ]
})
</script>

<style scoped>
.home-container {
  display: flex;
  padding: 20px 60px;
  gap: 24px;
  background: #f1e7cb;
}

.side-category {
  width: 240px;
  flex-shrink: 0;
}

.main-content {
  flex-grow: 1;
  min-width: 0;
}

.faq-buttons {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.faq-buttons button {
  background: #7ac028;
  color: white;
  padding: 10px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.faq-section {
  background: #fff;
  padding: 30px;
  border-radius: 6px;
}

.faq-item {
  margin-bottom: 28px;
}

.question {
  font-weight: bold;
  color: #2c3e50;
  font-size: 16px;
  margin-bottom: 6px;
}

.answer {
  font-size: 14px;
  color: #555;
  margin-left: 10px;
}
.intro-text {
  font-size: 15px;
  margin-bottom: 12px;
  color: #333;
  font-weight: normal;
}

</style>
