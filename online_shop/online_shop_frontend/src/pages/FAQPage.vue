<template>
  <div class="home-container">
    <SideCategory class="side-category" v-show="!isMobile || showSidebar" />

    <div class="main-content">
      <!-- <Carousel :slides="slides" /> -->

      <!-- 分类按钮 -->
      <div class="faq-buttons">
        <button @click="scrollTo('order')">{{ $t('faq.order_title') }}</button>
        <button @click="scrollTo('shipping')">{{ $t('faq.shipping_title') }}</button>
        <button @click="scrollTo('other')">{{ $t('faq.other_title') }}</button>
      </div>

      <!-- FAQ 部分 -->
      <section class="faq-section">
        <h2 id="order">{{ $t('faq.order_title') }}</h2>
        <div v-for="item in faqItems.order" :key="item.id" class="faq-item">
          <p class="question">Q. {{ $t(`faq.${item.q}`) }}</p>
          <p class="answer">A. {{ $t(`faq.${item.a}`) }}</p>
        </div>

        <h2 id="shipping">{{ $t('faq.shipping_title') }}</h2>
        <div v-for="item in faqItems.shipping" :key="item.id" class="faq-item">
          <p class="question">Q. {{ $t(`faq.${item.q}`) }}</p>
          <p class="answer">A. {{ $t(`faq.${item.a}`) }}</p>
        </div>

        <h2 id="other">{{ $t('faq.other_title') }}</h2>
        <div v-for="item in faqItems.other" :key="item.id" class="faq-item">
          <p class="question">Q. {{ $t(`faq.${item.q}`) }}</p>
          <p class="answer">A. {{ $t(`faq.${item.a}`) }}</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import SideCategory from '../components/common/SideCategory.vue'
import Carousel from '../components/common/Carousel.vue'
import { ref } from 'vue'

const faqItems = ref({
  order: [
    { id: 1, q: 'order_change_q', a: 'order_change_a' },
    { id: 2, q: 'cancel_q', a: 'cancel_a' },
    { id: 3, q: 'receipt_q', a: 'receipt_a' },
    { id: 4, q: 'invoice_q', a: 'invoice_a' },
    { id: 5, q: 'no_reply_q', a: 'no_reply_a' },
    { id: 6, q: 'credit_card_q', a: 'credit_card_a' }
  ],
  shipping: [
    { id: 7, q: 'shipping_cost_q', a: 'shipping_cost_a' },
    { id: 8, q: 'frozen_mix_q', a: 'frozen_mix_a' },
    { id: 9, q: 'mail_delivery_q', a: 'mail_delivery_a' },
    { id: 10, q: 'overseas_q', a: 'overseas_a' },
    { id: 11, q: 'return_exchange_q', a: 'return_exchange_a' },
    { id: 12, q: 'gift_q', a: 'gift_a' }
  ],
  other: [
    { id: 13, q: 'member_required_q', a: 'member_required_a' },
    { id: 14, q: 'point_expiry_q', a: 'point_expiry_a' },
    { id: 15, q: 'physical_store_q', a: 'physical_store_a' }
  ]
})

const scrollTo = (id) => {
  const el = document.getElementById(id)
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}
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
  padding: 20px;
  border-radius: 6px;
}

.faq-item {
  margin-bottom: 20px;
}

.question {
  font-weight: bold;
  color: #333;
  margin-bottom: 4px;
}

.answer {
  margin-left: 12px;
  color: #666;
}
</style>
