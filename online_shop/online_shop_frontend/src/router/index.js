import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/HomePage.vue'
import ProductsPage from '../pages/ProductsPage.vue'
import ShoppingInfo from '../pages/ShoppingInfo.vue'
import FAQPage from '../pages/FAQPage.vue'
import ContactPage from '../pages/ContactPage.vue'
import ProductDetail from '../pages/ProductDetail.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/products', component: ProductsPage },
  { path: '/shopping-info', component: ShoppingInfo },
  { path: '/faq', component: FAQPage },
  { path: '/contact', component: ContactPage },
  { path: '/product/:id', name: 'ProductDetail', component: ProductDetail }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router


