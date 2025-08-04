<template>
  <div class="home-container">
    <SideCategory class="side-category" v-show="!isMobile || showSidebar" />

    <div class="main-content">
      <Carousel :slides="slides" />

      <ProductSearch @search="handleSearch" />

      <div class="product-list">
        <ProductCard
          v-for="product in paginatedProducts"
          :key="product.name"
          :product="product"
          @add-to-cart="handleAddToCart"
        />
      </div>

      <div class="pagination">
        <button :disabled="currentPage === 1" @click="prevPage">«</button>
        <span>{{ currentPage }} / {{ totalPages }}</span>
        <button :disabled="currentPage === totalPages" @click="nextPage">»</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import Carousel from '../components/common/Carousel.vue'
import SideCategory from '../components/common/SideCategory.vue'
import ProductCard from '../components/product/ProductCard.vue'
import ProductSearch from '../components/product/ProductSearch.vue'
import { ref, computed } from 'vue'

const slides = ref([
  { src: new URL('../assets/banner1.jpg', import.meta.url).href, title: 'Comming Soon', description: 'グランドオープンをお楽しみに！' },
  { src: new URL('../assets/banner2.jpg', import.meta.url).href, title: '中華物産', description: '豊富な商品を自由にお選びいただけます。' },
  { src: new URL('../assets/banner3.jpg', import.meta.url).href, title: '中華物産', description: '豊富な商品を自由にお選びいただけます。' }
])




const allProducts = ref([
    {id: 1, name: '甜畅 海螺酥 80g', price: Math.round(128 * 1.08), image: new URL('@/assets/product/product1.jpg', import.meta.url).href},
    {id: 2, name: '烤翅要逆天味小浣熊', price: Math.round(118 * 1.08), image: new URL('@/assets/product/product2.jpg', import.meta.url).href},
    {id: 3, name: '番茄红烩味小浣熊', price: Math.round(118 * 1.08), image: new URL('@/assets/product/product3.jpg', import.meta.url).href},
    {id: 4, name: '双叶 黄桃罐头580g', price: Math.round(338 * 1.08), image: new URL('@/assets/product/product4.jpg', import.meta.url).href},
    {id: 5, name: '双叶 梨罐头580g', price: Math.round(338 * 1.08), image: new URL('@/assets/product/product5.jpg', import.meta.url).href},
    {id: 6, name: '蒜香友盛 蒜香青豆240g', price: Math.round(38 * 1.08), image: new URL('@/assets/product/product6.jpg', import.meta.url).href},
    {id: 7, name: '友盛 山楂条 200g', price: Math.round(208 * 1.08), image: new URL('@/assets/product/product7.jpg', import.meta.url).href},
    {id: 8, name: '奥赛山楂饴150g', price: Math.round(188 * 1.08), image: new URL('@/assets/product/product8.jpg', import.meta.url).href},
    {id: 9, name: '小马哥 大辣片 70g', price: Math.round(108 * 1.08), image: new URL('@/assets/product/product9.jpg', import.meta.url).href},
    {id: 10, name: '伊利草莓味牛奶片16g*10板/盒', price: Math.round(78 * 1.08), image: new URL('@/assets/product/product10.jpg', import.meta.url).href},
    {id: 11, name: '小马哥 相思卷 80g', price: Math.round(108 * 1.08), image: new URL('@/assets/product/product11.jpg', import.meta.url).href},
    {id: 12, name: '小马哥 网红辣丝 70g', price: Math.round(108 * 1.08), image: new URL('@/assets/product/product12.jpg', import.meta.url).href},
    {id: 13, name: '卧龙小麻花 烧烤味208g', price: Math.round(408 * 1.08), image: new URL('@/assets/product/product13.jpg', import.meta.url).href},
    {id: 14, name: '卧龙 老灶卧龙锅巴 爆辣味200g', price: Math.round(398 * 1.08), image: new URL('@/assets/product/product14.jpg', import.meta.url).href},
    {id: 15, name: '金沙河 原味挂面 500g', price: Math.round(338 * 1.08), image: new URL('@/assets/product/product15.jpg', import.meta.url).href},
    {id: 16, name: '桥头 重庆麻辣烫底料 麻辣味 150g ', price: Math.round(318 * 1.08), image: new URL('@/assets/product/product16.jpg', import.meta.url).href},
    {id: 17, name: '桥头 拿手毛血旺调料 麻辣味 160g ', price: Math.round(318 * 1.08), image: new URL('@/assets/product/product17.jpg', import.meta.url).href},
    {id: 18, name: '海底捞 清汤火锅底料 110g', price: Math.round(418 * 1.08), image: new URL('@/assets/product/product18.jpg', import.meta.url).href},
    {id: 19, name: '海底捞 番茄火锅底料200g', price: Math.round(438 * 1.08), image: new URL('@/assets/product/product19.jpg', import.meta.url).href},
    {id: 20, name: '海底捞 麻辣香锅调味料220g ', price: Math.round(438 * 1.08), image: new URL('@/assets/product/product20.jpg', import.meta.url).href},
    {id: 21, name: '乌江 泡萝卜丁 下饭菜 60g', price: Math.round(88 * 1.08), image: new URL('@/assets/product/product21.jpg', import.meta.url).href},
    {id: 22, name: '海天 老抽王500ml', price: Math.round(288 * 1.08), image: new URL('@/assets/product/product22.jpg', import.meta.url).href},
    {id: 23, name: '海天海鲜酱油500ml ', price: Math.round(338 * 1.08), image: new URL('@/assets/product/product23.jpg', import.meta.url).href},
    {id: 24, name: '海天红烧老抽酱油500ml', price: Math.round(268 * 1.08), image: new URL('@/assets/product/product24.jpg', import.meta.url).href},
    {id: 25, name: '镇江香醋 500ml', price: Math.round(168 * 1.08), image: new URL('@/assets/product/product25.jpg', import.meta.url).href},
    {id: 26, name: '宝鼎天鱼醋精500m', price: Math.round(278 * 1.08), image: new URL('@/assets/product/product26.jpg', import.meta.url).href},
    {id: 27, name: '海天 招牌蚝油270g ', price: Math.round(188 * 1.08), image: new URL('@/assets/product/product27.jpg', import.meta.url).href},
    {id: 28, name: '海天 招牌蚝油725g', price: Math.round(398 * 1.08), image: new URL('@/assets/product/product28.jpg', import.meta.url).href},
    {id: 29, name: '海天 老抽王1750ml ', price: Math.round(778 * 1.08), image: new URL('@/assets/product/product29.jpg', import.meta.url).href},
    {id: 30, name: '果艳 小米煎饼 200g ', price: Math.round(348 * 1.08), image: new URL('@/assets/product/product30.jpg', import.meta.url).href},
    {id: 31, name: '娃哈哈爽歪歪200ml*4个', price: Math.round(558 * 1.08), image: new URL('@/assets/product/product31.jpg', import.meta.url).href},
    {id: 32, name: '引口馋 大面筋 72g 辣条', price: Math.round(168 * 1.08), image: new URL('@/assets/product/product32.jpg', import.meta.url).href},
    {id: 33, name: '康师傅 青梅绿茶 500ml', price: Math.round(158 * 1.08), image: new URL('@/assets/product/product33.jpg', import.meta.url).href},
    {id: 34, name: '康师傅 茉莉清茶 500ml', price: Math.round(158 * 1.08), image: new URL('@/assets/product/product34.jpg', import.meta.url).href},
    {id: 35, name: '康师傅 水蜜桃500ml', price: Math.round(158 * 1.08), image: new URL('@/assets/product/product35.jpg', import.meta.url).href},
    {id: 36, name: '康师傅 酸梅汤500ml', price: Math.round(158 * 1.08), image: new URL('@/assets/product/product36.jpg', import.meta.url).href},
    {id: 37, name: '康师傅 冰红茶 整箱', price: Math.round(158 * 1.08), image: new URL('@/assets/product/product37.jpg', import.meta.url).href},
    {id: 38, name: '康师傅 绿茶 500ml', price: Math.round(158 * 1.08), image: new URL('@/assets/product/product38.jpg', import.meta.url).href},
    {id: 39, name: '康师傅 芒果小酪500ml', price: Math.round(158 * 1.08), image: new URL('@/assets/product/product39.jpg', import.meta.url).href},
    {id: 40, name: '康师傅 茉莉蜜茶 500ml', price: Math.round(158 * 1.08), image: new URL('@/assets/product/product40.jpg', import.meta.url).href},
    {id: 41, name: '康师傅 冰糖雪梨500ml', price: Math.round(158 * 1.08), image: new URL('@/assets/product/product41.jpg', import.meta.url).href},
    {id: 42, name: '康师傅桶面 香辣牛肉面         ', price: Math.round(258 * 1.08), image: new URL('@/assets/product/product42.jpg', import.meta.url).href},
    {id: 43, name: '康师傅 桶面 金汤肥牛面', price: Math.round(258 * 1.08), image: new URL('@/assets/product/product43.jpg', import.meta.url).href},
    {id: 44, name: '康师傅 桶面 小鸡炖蘑菇', price: Math.round(258 * 1.08), image: new URL('@/assets/product/product44.jpg', import.meta.url).href},
    {id: 45, name: '康师傅桶面 鲜虾鱼板面', price: Math.round(258 * 1.08), image: new URL('@/assets/product/product45.jpg', import.meta.url).href},
    {id: 46, name: '康师傅 酸辣牛肉面 5连包', price: Math.round(528 * 1.08), image: new URL('@/assets/product/product46.jpg', import.meta.url).href},
    {id: 47, name: '康师傅 桶面 老坛酸菜面 ', price: Math.round(258 * 1.08), image: new URL('@/assets/product/product47.jpg', import.meta.url).href},
    {id: 48, name: '康师傅 老坛酸菜面 5连包', price: Math.round(528 * 1.08), image: new URL('@/assets/product/product48.jpg', import.meta.url).href},
    {id: 49, name: '劲仔厚豆干香辣味20g*20包', price: Math.round(38 * 1.08), image: new URL('@/assets/product/product49.jpg', import.meta.url).href},
    {id: 50, name: '劲仔 深海小鱼 卤香味12g', price: Math.round(38 * 1.08), image: new URL('@/assets/product/product50.jpg', import.meta.url).href},
    {id: 51, name: '劲仔深海小鱼 糖醋味 12g', price: Math.round(38 * 1.08), image: new URL('@/assets/product/product51.jpg', import.meta.url).href},
    {id: 52, name: '劲仔深海小鱼 酱汁味12g', price: Math.round(38 * 1.08), image: new URL('@/assets/product/product52.jpg', import.meta.url).href},
    {id: 53, name: '劲仔 深海小鱼 12g', price: Math.round(38 * 1.08), image: new URL('@/assets/product/product53.jpg', import.meta.url).href},
    {id: 54, name: ' 陶和笙 椰丝麻栳68g', price: Math.round(228 * 1.08), image: new URL('@/assets/product/product54.jpg', import.meta.url).href},
    {id: 55, name: '卫龙 亲嘴烧 味麦辣鸡汁口 24g', price: Math.round(58 * 1.08), image: new URL('@/assets/product/product55.jpg', import.meta.url).href},
    {id: 56, name: '卫龙 大面筋 白色袋装106g ', price: Math.round(208 * 1.08), image: new URL('@/assets/product/product56.jpg', import.meta.url).href},
    {id: 57, name: '延城小菜 豆皮小菜 辣条 12g ', price: Math.round(68 * 1.08), image: new URL('@/assets/product/product57.jpg', import.meta.url).href},
    {id: 58, name: '康师傅 红葱头葱香排骨面 5连包', price: Math.round(528 * 1.08), image: new URL('@/assets/product/product58.jpg', import.meta.url).href},
    {id: 59, name: '康师傅 香辣牛肉面 5连包', price: Math.round(528 * 1.08), image: new URL('@/assets/product/product59.jpg', import.meta.url).href},
    {id: 60, name: '康师傅 桶面 红烧牛肉味 ', price: Math.round(258 * 1.08), image: new URL('@/assets/product/product60.jpg', import.meta.url).href},
    {id: 61, name: '康师傅 红烧牛肉面 5连包 ', price: Math.round(528 * 1.08), image: new URL('@/assets/product/product61.jpg', import.meta.url).href},
    {id: 62, name: '田小花 肥汁土豆粉 红油味 ', price: Math.round(558 * 1.08), image: new URL('@/assets/product/product62.jpg', import.meta.url).href},
    {id: 63, name: '田小花 流汁大宽粉 酸辣味 黄袋 274g', price: Math.round(558 * 1.08), image: new URL('@/assets/product/product63.jpg', import.meta.url).href},
    {id: 64, name: '泰山 八宝粥 原味 ', price: Math.round(238 * 1.08), image: new URL('@/assets/product/product64.jpg', import.meta.url).href},
    {id: 65, name: '娃哈哈 八宝粥 红枣小米', price: Math.round(238 * 1.08), image: new URL('@/assets/product/product65.jpg', import.meta.url).href},
    {id: 66, name: '娃哈哈 百合莲子八宝粥', price: Math.round(238 * 1.08), image: new URL('@/assets/product/product66.jpg', import.meta.url).href},
    {id: 67, name: '娃哈哈八宝粥 木糖醇 ', price: Math.round(238 * 1.08), image: new URL('@/assets/product/product67.jpg', import.meta.url).href},
    {id: 68, name: '乡姑 红油榨菜丝 150g', price: Math.round(118 * 1.08), image: new URL('@/assets/product/product68.jpg', import.meta.url).href},
    {id: 69, name: '吉香居 咸菜 麻辣三丝 180g ', price: Math.round(138 * 1.08), image: new URL('@/assets/product/product69.jpg', import.meta.url).href},
    {id: 70, name: '王致和 韭菜花酱 320g', price: Math.round(258 * 1.08), image: new URL('@/assets/product/product70.jpg', import.meta.url).href},
    {id: 71, name: '吉香居 咸菜 红油豇豆150g ', price: Math.round(168 * 1.08), image: new URL('@/assets/product/product71.jpg', import.meta.url).href},
    {id: 72, name: '王致和 红辣腐乳 340g 豆腐乳', price: Math.round(328 * 1.08), image: new URL('@/assets/product/product72.jpg', import.meta.url).href},
    {id: 73, name: '王致和 大块红腐乳340g ', price: Math.round(328 * 1.08), image: new URL('@/assets/product/product73.jpg', import.meta.url).href},
    {id: 74, name: '老干妈 辣三丁油辣椒280g ', price: Math.round(328 * 1.08), image: new URL('@/assets/product/product74.jpg', import.meta.url).href},
    {id: 75, name: '老干妈 风味豆豉油辣椒280g', price: Math.round(328 * 1.08), image: new URL('@/assets/product/product75.jpg', import.meta.url).href},
    {id: 76, name: '老干妈 牛肉味豆豉油辣椒 210g ', price: Math.round(328 * 1.08), image: new URL('@/assets/product/product76.jpg', import.meta.url).href},
    {id: 77, name: '铁成东北酸菜 500g/袋', price: Math.round(158 * 1.08), image: new URL('@/assets/product/product77.jpg', import.meta.url).href},
])

const currentPage = ref(1)
const productsPerPage = 16

const totalPages = computed(() => Math.ceil(allProducts.value.length / productsPerPage))
const paginatedProducts = computed(() =>
  allProducts.value.slice((currentPage.value - 1) * productsPerPage, currentPage.value * productsPerPage)
)

const nextPage = () => currentPage.value < totalPages.value && currentPage.value++
const prevPage = () => currentPage.value > 1 && currentPage.value--




function handleSearch(filters) {
  console.log('搜索条件:', filters)
  // 可扩展 API 过滤逻辑
}

function handleAddToCart(product) {
  alert(`${product.name} をカートに追加しました ✅`)
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
}

.main-content {
  flex: 1;
  min-width: 0;
}

.product-list {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin-bottom: 20px;
}

@media (max-width: 1280px) {
  .product-list {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 900px) {
  .product-list {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .product-list {
    grid-template-columns: repeat(1, 1fr);
  }
}



.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  font-size: 16px;
  margin-bottom: 40px;
}

.pagination button {
  padding: 6px 12px;
  font-size: 16px;
  background-color: #666;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.pagination button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
