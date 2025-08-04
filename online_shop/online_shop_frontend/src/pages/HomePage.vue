<template>
  <div class="home-container">
    <!-- 导航栏（移动端） -->
    <!-- <div class="mobile-header" v-if="isMobile">
      <button class="menu-btn" @click="toggleSidebar">☰</button>
      <h2 class="store-title">Asian Store</h2>
    </div> -->


    <!-- 左侧分类栏 -->
    <SideCategory class="side-category" v-show="!isMobile || showSidebar" />

    <!-- 主内容 -->
    <div class="main-content">
      <Carousel :slides="slides" />

      <div class="intro-text">
        <h4>{{ $t('introduce.introduce1') }}</h4>
        <p>{{ $t('introduce.introduce2') }}</p>
      </div>

      <div class="shop-info-wrapper">
          <h4 class="section-title">📄 {{ $t('home.shop_info') }}</h4>
          <table class="shop-info-table">
            <tr>
              <th>{{ $t('home.shop_name') }}</th>
              <td>{{ $t('home.shop_name_value') }}</td>
            </tr>
            <tr>
              <th>{{ $t('home.address') }}</th>
              <td v-html="$t('home.address_value')"></td>
            </tr>
            <tr>
              <th>{{ $t('home.business_hours') }}</th>
              <td>{{ $t('home.business_hours_value') }}</td>
            </tr>
          </table>
        </div>

      <!-- 地图与店铺信息 -->
      <div class="info-section">
        <div class="map-wrapper">
          <h4 class="section-title">📍 {{ $t('home.access') }}</h4>
          <MapView />
        </div>

        
      </div>

      <!-- 日历（只在手机端显示） -->
      <div v-if="isMobile" class="calendar-mobile">
        <h4 class="section-title">📅 {{ $t('category.calendar') }}</h4>
        <CalendarDisplay />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Carousel from '../components/common/Carousel.vue'
import SideCategory from '../components/common/SideCategory.vue'
import MapView from '../components/homePage/MapView.vue'
import CalendarDisplay from '../components/common/CalendarDisplay.vue'

const slides = ref([
  {
    src: new URL('../assets/banner1.jpg', import.meta.url).href,
    alt: 'スライド1',
    title: 'Comming Soon',
    description: 'グランドオープンをお楽しみに！'
  },
  {
    src: new URL('../assets/banner2.jpg', import.meta.url).href,
    alt: 'スライド2',
    title: '中華物産',
    description: '豊富な商品を自由にお選びいただけます。'
  },
  {
    src: new URL('../assets/banner3.jpg', import.meta.url).href,
    alt: 'スライド3',
    title: '中華物産',
    description: '豊富な商品を自由にお選びいただけます。'
  }
])

const isMobile = ref(false)
const showSidebar = ref(false)

const toggleSidebar = () => {
  showSidebar.value = !showSidebar.value
}

onMounted(() => {
  const updateMobile = () => {
    isMobile.value = window.innerWidth <= 768
  }
  updateMobile()
  window.addEventListener('resize', updateMobile)
})
</script>

<style scoped>
.home-container {
  display: flex;
  flex-wrap: wrap;
  padding: 20px 60px;
  background: #f1e7cb;
}

/* 左侧分类栏 */
.side-category {
  width: 220px;
  flex-shrink: 0;
}

/* 主区域 */
.main-content {
  flex: 1;
  min-width: 0;
  padding: 0 20px;
}

/* 移动端隐藏分类栏 */
@media (max-width: 768px) {
  .side-category {
    display: none;
  }
}

/* 导航栏样式 */
.mobile-header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #ff9900;
  color: #fff;
}

.menu-btn {
  font-size: 24px;
  background: none;
  border: none;
  color: white;
}

.store-title {
  font-size: 20px;
}

/* 店铺信息与地图横排（PC） */
.info-section {
  display: flex;
  gap: 30px;
  margin-top: 50px;
}

/* 移动端改为纵向 */
@media (max-width: 768px) {
  .info-section {
    flex-direction: column;
  }
}

.map-wrapper,
.shop-info-wrapper {
  flex: 1;
}

/* 店铺信息表 */
.shop-info-table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
}

.shop-info-table th,
.shop-info-table td {
  border: 1px solid #ccc;
  padding: 10px;
  text-align: left;
}

.shop-info-table th {
  background-color: #f0f8ff;
  width: 30%;
}

.section-title {
  margin: 30px 0 10px;
  font-size: 1.2rem;
  text-align: left;
  border-left: 5px solid orange;
  padding-left: 10px;
}

.intro-text {
  margin-top: 30px;
  background-color: #fff8e1;
  padding: 20px;
  border: 1px solid #f5d28e;
  border-radius: 8px;
}

.intro-text h4 {
  font-size: 1.1rem;
  margin-bottom: 8px;
  color: #d35400;
}

.intro-text p {
  color: #555;
  font-size: 0.95rem;
}

.calendar-mobile {
  margin-top: 40px;
}
</style>
