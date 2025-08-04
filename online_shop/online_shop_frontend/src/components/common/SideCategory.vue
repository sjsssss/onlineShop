<template>
  <div class="side-category">
    <h5>{{ $t('category.title') }}</h5>

    <!-- 商品分類 -->
    <div v-for="section in safeArray(sections)" :key="section.label" class="category-section">
      <div class="section-header">{{ $t(section.label) }}</div>
      <ul>
        <li v-for="item in safeArray(section.items)" :key="item?.name || item">
          <router-link v-if="item?.path" :to="item.path">{{ $t(item.name) }}</router-link>
          <span v-else>{{ $t(item?.name || '') }}</span>
        </li>
      </ul>
    </div>

    <!-- 公式SNS -->
    <div class="category-section">
      <div class="section-header">▼ {{ $t('category.official_account') }}</div>
      <div class="sns-icons">
        <img class="wechat-qr" src="../../assets/QRCode.jpg" alt="WeChat" style="height: 100%; width: 100%;"/>
        <p class="sns-label">WeChat</p>
      </div>
    </div>

    <!-- 営業日カレンダー -->
    <div class="category-section">
      <div class="section-header">▼ {{ $t('category.calendar') }}</div>
      <div class="calendar-block">
        <CalendarDisplay />
        <div class="legend">
          <div><span class="legend-box yellow"></span> {{ $t('category.today') }}</div>
          <div><span class="legend-box pink"></span> {{ $t('category.closed') }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import CalendarDisplay from '../common/CalendarDisplay.vue'

const safeArray = (arr) => Array.isArray(arr) ? arr : []

const sections = [
  {
    label: 'category.recommend',
    items: [
      { name: 'category.seasonal', path: '/products/seasonal' },
      { name: 'category.free_shipping', path: '/products/free-shipping' }
    ]
  },
  {
    label: 'category.asian_food',
    items: [
      { name: 'category.frozen_meat', path: '/products/frozen-meat' },
      { name: 'category.frozen_chinese', path: '/products/frozen-chinese' },
      { name: 'category.chinese_deli', path: '/products/deli' },
      { name: 'category.fermented', path: '/products/fermented' }
    ]
  }
]
</script>

<style scoped>
.side-category {
  width: 220px;
  background: #fff;
  border: 1px solid #ddd;
  padding: 1rem;
  font-size: 0.95rem;
}

.category-section {
  margin-bottom: 1.5rem;
}

.section-header {
  font-weight: bold;
  margin-bottom: 0.5rem;
  color: #c63;
  border-left: 5px solid orange;
  padding-left: 0.5rem;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 6px;
}

a {
  color: #333;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

.sns-icons {
  text-align: center;
}

.sns-icons img {
  width: 60px;
  margin: 5px 8px;
}

.wechat-qr {
  width: 100px;
  margin: 10px auto;
}

.sns-label {
  font-size: 0.85rem;
  color: #666;
  margin-top: 4px;
}

.calendar-block {
  margin-top: 10px;
}

.legend {
  font-size: 0.8rem;
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-top: 10px;
}

.legend-box {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 1px solid #ccc;
  margin-right: 6px;
  vertical-align: middle;
}

.legend-box.yellow {
  background-color: #ffff99;
}

.legend-box.pink {
  background-color: #f9cccc;
}
</style>
