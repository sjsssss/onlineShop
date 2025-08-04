<template>
  <nav class="title-navbar d-flex justify-content-between align-items-center flex-wrap px-4">
    <router-link to="/" class="navbar-logo text-center mx-auto">
      巧巧屋物産
    </router-link>
  </nav>
  <nav class="custom-navbar d-flex justify-content-between align-items-center flex-wrap px-4">
    <!-- 左侧菜单 -->
    <ul class="nav left-menu d-none d-lg-flex">
      <li class="nav-item" v-for="item in leftItems" :key="item.path">
        <router-link class="nav-link" :to="item.path">{{ $t(item.label) }}</router-link>
      </li>
    </ul>

    <!-- 中间LOGO -->
    

    <!-- 右侧菜单 -->
    <div class="right-menu d-none d-lg-flex align-items-center">
      <!-- <span class="nav-link">{{ $t('site.mypage') }}</span>
      <span class="nav-link">{{ $t('site.logout') }}</span>
      <span class="nav-link">{{ $t('site.cart') }}</span> -->

      <!-- 语言切换 -->
      <div class="dropdown ms-3">
        <button class="btn btn-sm btn-light dropdown-toggle" type="button" data-bs-toggle="dropdown">
          {{ currentLangLabel }}
        </button>
        <ul class="dropdown-menu dropdown-menu-end">
          <li><a class="dropdown-item" href="#" @click.prevent="switchLang('ja')">日本語</a></li>
          <li><a class="dropdown-item" href="#" @click.prevent="switchLang('zh')">中文</a></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale, t } = useI18n()

const leftItems = ref([
  { label: 'site.home', path: '/'},
  { label: 'site.products', path: '/products' },
  { label: 'site.shoppingInfo', path: '/shopping-info' },
  { label: 'site.faq', path: '/faq' },
  { label: 'site.contact', path: '/contact' }
])

const currentLangLabel = computed(() =>
  locale.value === 'ja' ? t('site.japanese') : t('site.chinese')
)

const switchLang = (lang) => {
  locale.value = lang
  localStorage.setItem('lang', lang)
}

if (localStorage.getItem('lang')) {
  locale.value = localStorage.getItem('lang')
}
</script>

<style scoped>
.custom-navbar {
  background-color: #fddda2fd;
  /* border-bottom: 2px solid #ccc; */
  padding: 3px 0;
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 0.9rem;
  position: relative;
}
.title-navbar {
  background-color: #fddda2fd;
  /* border-bottom: 2px solid #ccc; */
  padding: 20px 0;
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 1.2rem;
  position: relative;
}

.nav-link {
  color: #333;
  margin: 0 10px;
  cursor: pointer;
}
.nav-link:hover {
  color: #d35400;
  text-decoration: underline;
}

.navbar-logo {
  font-size: 2.5rem;
  font-weight: bold;
  color: #222;
  white-space: nowrap;
}

.dropdown-menu {
  font-size: 0.9rem;
}

/* 手机适配（隐藏大菜单，建议加 toggle 按钮） */
@media (max-width: 991px) {
  .left-menu,
  .right-menu {
    display: none !important;
  }

  .navbar-logo {
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
