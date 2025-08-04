<template>
  <div class="home-container">
    <SideCategory class="side-category" v-show="!isMobile" />

    <div class="product-detail-container" v-if="product">
      <!-- 商品图片 -->
      <div class="left-section">
        <img :src="product.image" class="main-image" @click="showZoom = true" />
        <div class="thumbnail-list">
          <img :src="product.image" class="thumbnail" />
          <img :src="product.image" class="thumbnail" />
        </div>
      </div>

      <!-- 商品详细信息 -->
      <div class="right-section">
        <h2 class="product-title">【常温便】{{ product.name }}</h2>
        <p class="product-code">商品コード：{{ product.code }}</p>
        <p class="product-price">
          <span class="label">価格：</span>
          <span class="price">￥{{ product.price }}（税込）</span>
        </p>
        <p class="product-point">ポイント：{{ product.point }}</p>
        <div class="product-qty">
          数量：
          <select v-model="selectedQty">
            <option v-for="n in 10" :key="n" :value="n">{{ n }}</option>
          </select>
        </div>

        <div class="action-buttons">
          <button class="btn add-to-cart">🛒 {{ $t('chart.add_to_cart') }}</button>
          <button class="btn favorite">🤍 {{ $t('chart.add_shopping_list') }}</button>
        </div>

        <div class="description-block">
          <p class="desc-title">【商品名】{{ product.name }}</p>
          <p class="desc-text">【原材料】{{ product.ingredients }}</p>
          <p class="desc-text">【原産地】{{ product.origin }}</p>
          <p class="desc-text">【内容量】{{ product.weight }}</p>
        </div>
      </div>

      <div v-if="showZoom" class="zoom-overlay" @click="showZoom = false">
        <img :src="product.image" class="zoom-image" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import SideCategory from '../components/common/SideCategory.vue'

// 从路由中获取ID
const route = useRoute()
const selectedQty = ref(1)
const showZoom = ref(false)
const id = parseInt(route.params.id)
const isMobile = ref(false)
const showSidebar = ref(false)

// const toggleSidebar = () => {
//   showSidebar.value = !showSidebar.value
// }
const productList = [
  {
    id: 1,
    name: '甜畅 海螺酥',
    price: Math.round(128 * 1.08),
    code: '470000000001',
    point: Math.round(128 * 1.08 * 0.1),
    image: new URL('@/assets/product/product1.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '80g'
  },
  {
    id: 2,
    name: '烤翅要逆天味小浣熊',
    price: Math.round(118 * 1.08),
    code: '470000000002',
    point: Math.round(118 * 1.08 * 0.1),
    image: new URL('@/assets/product/product2.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '40g'
  },
  {
    id: 3,
    name: '番茄红烩味小浣熊',
    price: Math.round(118 * 1.08),
    code: '470000000003',
    point: Math.round(118 * 1.08 * 0.1),
    image: new URL('@/assets/product/product3.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '40'
  },
  {
    id: 4,
    name: ' 双叶 黄桃罐头',
    price: Math.round(338 * 1.08),
    code: '470000000004',
    point: Math.round(338 * 1.08 * 0.1),
    image: new URL('@/assets/product/product4.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '580g'
  },
  {
    id: 5,
    name: '双叶 梨罐头',
    price: Math.round(338 * 1.08),
    code: '470000000005',
    point: Math.round(338 * 1.08 * 0.1),
    image: new URL('@/assets/product/product5.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '580g'
  },
  {
    id: 6,
    name: '蒜香友盛 蒜香青豆',
    price: Math.round(38 * 1.08),
    code: '470000000006',
    point: Math.round(38 * 1.08 * 0.1),
    image: new URL('@/assets/product/product6.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '240g'
  },
  {
    id: 7,
    name: '友盛 山楂条',
    price: Math.round(208 * 1.08),
    code: '470000000007',
    point: Math.round(208 * 1.08 * 0.1),
    image: new URL('@/assets/product/product7.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '200g'
  },
  {
    id: 8,
    name: '奥赛山楂饴',
    price: Math.round(188 * 1.08),
    code: '470000000008',
    point: Math.round(188 * 1.08 * 0.1),
    image: new URL('@/assets/product/product8.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '150g'
  },
  {
    id: 9,
    name: '小马哥 大辣片',
    price: Math.round(108 * 1.08),
    code: '470000000009',
    point: Math.round(108 * 1.08 * 0.1),
    image: new URL('@/assets/product/product9.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '70g'
  },
  {
    id: 10,
    name: '伊利草莓味牛奶片',
    price: Math.round(78 * 1.08),
    code: '470000000010',
    point: Math.round(78 * 1.08 * 0.1),
    image: new URL('@/assets/product/product10.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '16g*10板/盒'
  },
  {
    id: 11,
    name: '小马哥 相思卷',
    price: Math.round(108 * 1.08),
    code: '470000000011',
    point: Math.round(108 * 1.08 * 0.1),
    image: new URL('@/assets/product/product11.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '80g'
  },
  {
    id: 12,
    name: '小马哥 网红辣丝',
    price: Math.round(108 * 1.08),
    code: '470000000012',
    point: Math.round(108 * 1.08 * 0.1),
    image: new URL('@/assets/product/product12.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '70g'
  },
  {
    id: 13,
    name: '卧龙小麻花 烧烤味',
    price: Math.round(408 * 1.08),
    code: '470000000013',
    point: Math.round(408 * 1.08 * 0.1),
    image: new URL('@/assets/product/product13.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '208g'
  },
  {
    id: 14,
    name: '卧龙 老灶卧龙锅巴 爆辣味',
    price: Math.round(398 * 1.08),
    code: '470000000014',
    point: Math.round(398 * 1.08 * 0.1),
    image: new URL('@/assets/product/product14.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '200g'
  },
  {
    id: 15,
    name: '金沙河 原味挂面',
    price: Math.round(338 * 1.08),
    code: '470000000015',
    point: Math.round(338 * 1.08 * 0.1),
    image: new URL('@/assets/product/product15.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500g'
  },
  {
    id: 16,
    name: '桥头 重庆麻辣烫底料 麻辣味',
    price: Math.round(318 * 1.08),
    code: '470000000016',
    point: Math.round(318 * 1.08 * 0.1),
    image: new URL('@/assets/product/product16.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '150g'
  },
  {
    id: 17,
    name: '桥头 拿手毛血旺调料 麻辣味',
    price: Math.round(318 * 1.08),
    code: '470000000017',
    point: Math.round(318 * 1.08 * 0.1),
    image: new URL('@/assets/product/product17.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '160g'
  },
  {
    id: 18,
    name: '海底捞 清汤火锅底料',
    price: Math.round(418 * 1.08),
    code: '470000000018',
    point: Math.round(418 * 1.08 * 0.1),
    image: new URL('@/assets/product/product18.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '110g'
  },
  {
    id: 19,
    name: '海底捞 番茄火锅底料',
    price: Math.round(438 * 1.08),
    code: '470000000019',
    point: Math.round(438 * 1.08 * 0.1),
    image: new URL('@/assets/product/product19.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '200g'
  },
  {
    id: 20,
    name: '海底捞 麻辣香锅调味料',
    price: Math.round(438 * 1.08),
    code: '470000000020',
    point: Math.round(438 * 1.08 * 0.1),
    image: new URL('@/assets/product/product20.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '220g'
  },
  {
    id: 21,
    name: '乌江 泡萝卜丁 下饭菜',
    price: Math.round(88 * 1.08),
    code: '470000000021',
    point: Math.round(88 * 1.08 * 0.1),
    image: new URL('@/assets/product/product21.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '60g'
  },
  {
    id: 22,
    name: '海天 老抽王',
    price: Math.round(288 * 1.08),
    code: '470000000022',
    point: Math.round(288 * 1.08 * 0.1),
    image: new URL('@/assets/product/product22.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 23,
    name: '海天海鲜酱油',
    price: Math.round(338 * 1.08),
    code: '470000000023',
    point: Math.round(338 * 1.08 * 0.1),
    image: new URL('@/assets/product/product23.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 24,
    name: '海天红烧老抽酱油',
    price: Math.round(268 * 1.08),
    code: '470000000024',
    point: Math.round(268 * 1.08 * 0.1),
    image: new URL('@/assets/product/product24.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 25,
    name: '镇江香醋',
    price: Math.round(168 * 1.08),
    code: '470000000025',
    point: Math.round(168 * 1.08 * 0.1),
    image: new URL('@/assets/product/product25.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 26,
    name: '宝鼎天鱼醋精',
    price: Math.round(278 * 1.08),
    code: '470000000026',
    point: Math.round(278 * 1.08 * 0.1),
    image: new URL('@/assets/product/product26.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 27,
    name: '海天 招牌蚝油',
    price: Math.round(188 * 1.08),
    code: '470000000027',
    point: Math.round(188 * 1.08 * 0.1),
    image: new URL('@/assets/product/product27.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '270g'
  },
  {
    id: 28,
    name: '海天 招牌蚝油',
    price: Math.round(398 * 1.08),
    code: '470000000028',
    point: Math.round(398 * 1.08 * 0.1),
    image: new URL('@/assets/product/product28.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '725g'
  },
  {
    id: 29,
    name: '海天 老抽王',
    price: Math.round(778 * 1.08),
    code: '470000000029',
    point: Math.round(778 * 1.08 * 0.1),
    image: new URL('@/assets/product/product29.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '1750ml'
  },
  {
    id: 30,
    name: '果艳 小米煎饼',
    price: Math.round(348 * 1.08),
    code: '470000000030',
    point: Math.round(348 * 1.08 * 0.1),
    image: new URL('@/assets/product/product30.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '200g'
  },
  {
    id: 31,
    name: '娃哈哈爽歪歪',
    price: Math.round(558 * 1.08),
    code: '470000000031',
    point: Math.round(558 * 1.08 * 0.1),
    image: new URL('@/assets/product/product31.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '200ml*4个'
  },
  {
    id: 32,
    name: '引口馋 大面筋辣条',
    price: Math.round(168 * 1.08),
    code: '470000000032',
    point: Math.round(168 * 1.08 * 0.1),
    image: new URL('@/assets/product/product32.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '72g'
  },
  {
    id: 33,
    name: '康师傅 青梅绿茶',
    price: Math.round(158 * 1.08),
    code: '470000000033',
    point: Math.round(158 * 1.08 * 0.1),
    image: new URL('@/assets/product/product33.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 34,
    name: '康师傅 茉莉清茶 ',
    price: Math.round(158 * 1.08),
    code: '470000000034',
    point: Math.round(158 * 1.08 * 0.1),
    image: new URL('@/assets/product/product34.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 35,
    name: '康师傅 水蜜桃',
    price: Math.round(158 * 1.08),
    code: '470000000035',
    point: Math.round(158 * 1.08 * 0.1),
    image: new URL('@/assets/product/product35.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 36,
    name: '康师傅 酸梅汤',
    price: Math.round(158 * 1.08),
    code: '470000000036',
    point: Math.round(158 * 1.08 * 0.1),
    image: new URL('@/assets/product/product36.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 37,
    name: '康师傅 冰红茶',
    price: Math.round(158 * 1.08),
    code: '470000000037',
    point: Math.round(158 * 1.08 * 0.1),
    image: new URL('@/assets/product/product37.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 38,
    name: '康师傅 绿茶',
    price: Math.round(158 * 1.08),
    code: '470000000038',
    point: Math.round(158 * 1.08 * 0.1),
    image: new URL('@/assets/product/product38.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 39,
    name: '康师傅 芒果小酪',
    price: Math.round(158 * 1.08),
    code: '470000000039',
    point: Math.round(158 * 1.08 * 0.1),
    image: new URL('@/assets/product/product39.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 40,
    name: '康师傅 茉莉蜜茶',
    price: Math.round(158 * 1.08),
    code: '470000000040',
    point: Math.round(158 * 1.08 * 0.1),
    image: new URL('@/assets/product/product40.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 41,
    name: '康师傅 冰糖雪梨',
    price: Math.round(158 * 1.08),
    code: '470000000041',
    point: Math.round(158 * 1.08 * 0.1),
    image: new URL('@/assets/product/product41.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500ml'
  },
  {
    id: 42,
    name: '康师傅桶面 香辣牛肉面',
    price: Math.round(258 * 1.08),
    code: '470000000042',
    point: Math.round(258 * 1.08 * 0.1),
    image: new URL('@/assets/product/product42.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '桶'
  },
  {
    id: 43,
    name: '康师傅 桶面 金汤肥牛面',
    price: Math.round(258 * 1.08),
    code: '470000000043',
    point: Math.round(258 * 1.08 * 0.1),
    image: new URL('@/assets/product/product43.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '105g'
  },
  {
    id: 44,
    name: '康师傅 桶面 小鸡炖蘑菇',
    price: Math.round(258 * 1.08),
    code: '470000000044',
    point: Math.round(258 * 1.08 * 0.1),
    image: new URL('@/assets/product/product44.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '105g'
  },
  {
    id: 45,
    name: '康师傅桶面 鲜虾鱼板面',
    price: Math.round(258 * 1.08),
    code: '470000000045',
    point: Math.round(258 * 1.08 * 0.1),
    image: new URL('@/assets/product/product45.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '105g'
  },
  {
    id: 46,
    name: '康师傅 酸辣牛肉面 5连包',
    price: Math.round(528 * 1.08),
    code: '470000000046',
    point: Math.round(528 * 1.08 * 0.1),
    image: new URL('@/assets/product/product46.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '5食入'
  },
  {
    id: 47,
    name: '康师傅 桶面 老坛酸菜面 ',
    price: Math.round(258 * 1.08),
    code: '470000000047',
    point: Math.round(258 * 1.08 * 0.1),
    image: new URL('@/assets/product/product47.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '105g'
  },
  {
    id: 48,
    name: '康师傅 老坛酸菜面 5连包',
    price: Math.round(528 * 1.08),
    code: '470000000048',
    point: Math.round(528 * 1.08 * 0.1),
    image: new URL('@/assets/product/product48.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '5食入'
  },
  {
    id: 49,
    name: '劲仔厚豆干香辣味',
    price: Math.round(38 * 1.08),
    code: '470000000049',
    point: Math.round(38 * 1.08 * 0.1),
    image: new URL('@/assets/product/product49.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '20g*20包'
  },
  {
    id: 50,
    name: '劲仔 深海小鱼 卤香味',
    price: Math.round(38 * 1.08),
    code: '470000000050',
    point: Math.round(38 * 1.08 * 0.1),
    image: new URL('@/assets/product/product50.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '12g'
  },
  {
    id: 51,
    name: '劲仔深海小鱼 糖醋味',
    price: Math.round(38 * 1.08),
    code: '470000000051',
    point: Math.round(38 * 1.08 * 0.1),
    image: new URL('@/assets/product/product51.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '12g'
  },
  {
    id: 52,
    name: '劲仔深海小鱼 酱汁味',
    price: Math.round(38 * 1.08),
    code: '470000000052',
    point: Math.round(38 * 1.08 * 0.1),
    image: new URL('@/assets/product/product52.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '12g'
  },
  {
    id: 53,
    name: '劲仔 深海小鱼',
    price: Math.round(38 * 1.08),
    code: '470000000053',
    point: Math.round(38 * 1.08 * 0.1),
    image: new URL('@/assets/product/product53.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '12g'
  },
  {
    id: 54,
    name: '陶和笙 椰丝麻栳',
    price: Math.round(228 * 1.08),
    code: '470000000054',
    point: Math.round(228 * 1.08 * 0.1),
    image: new URL('@/assets/product/product54.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '68g'
  },
  {
    id: 55,
    name: '卫龙 亲嘴烧 味麦辣鸡汁口',
    price: Math.round(58 * 1.08),
    code: '470000000055',
    point: Math.round(58 * 1.08 * 0.1),
    image: new URL('@/assets/product/product55.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '24g'
  },
  {
    id: 56,
    name: '卫龙 大面筋 白色袋装',
    price: Math.round(208 * 1.08),
    code: '470000000056',
    point: Math.round(208 * 1.08 * 0.1),
    image: new URL('@/assets/product/product56.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '106g'
  },
  {
    id: 57,
    name: '延城小菜 豆皮小菜 辣条',
    price: Math.round(68 * 1.08),
    code: '470000000057',
    point: Math.round(68 * 1.08 * 0.1),
    image: new URL('@/assets/product/product57.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '12g'
  },
  {
    id: 58,
    name: '康师傅 红葱头葱香排骨面',
    price: Math.round(528 * 1.08),
    code: '470000000058',
    point: Math.round(528 * 1.08 * 0.1),
    image: new URL('@/assets/product/product58.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '5食入'
  },
  {
    id: 59,
    name: '康师傅 香辣牛肉面',
    price: Math.round(528 * 1.08),
    code: '470000000059',
    point: Math.round(528 * 1.08 * 0.1),
    image: new URL('@/assets/product/product59.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '5食入'
  },
  {
    id: 60,
    name: '康师傅 桶面 红烧牛肉味 ',
    price: Math.round(258 * 1.08),
    code: '470000000060',
    point: Math.round(258 * 1.08 * 0.1),
    image: new URL('@/assets/product/product60.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '106g'
  },
  {
    id: 61,
    name: '康师傅 红烧牛肉面 5连包 ',
    price: Math.round(528 * 1.08),
    code: '470000000061',
    point: Math.round(528 * 1.08 * 0.1),
    image: new URL('@/assets/product/product61.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '5食入'
  },
  {
    id: 62,
    name: '田小花 肥汁土豆粉 红油味 ',
    price: Math.round(558 * 1.08),
    code: '470000000062',
    point: Math.round(558 * 1.08 * 0.1),
    image: new URL('@/assets/product/product62.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '271g'
  },
  {
    id: 63,
    name: '田小花 流汁大宽粉 酸辣味 黄袋',
    price: Math.round(558 * 1.08),
    code: '470000000063',
    point: Math.round(558 * 1.08 * 0.1),
    image: new URL('@/assets/product/product63.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '274g'
  },
  {
    id: 64,
    name: '泰山 八宝粥 原味',
    price: Math.round(238 * 1.08),
    code: '470000000064',
    point: Math.round(238 * 1.08 * 0.1),
    image: new URL('@/assets/product/product64.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '台湾',
    weight: '375ml'
  },
  {
    id: 65,
    name: '娃哈哈 八宝粥 红枣小米',
    price: Math.round(238 * 1.08),
    code: '470000000065',
    point: Math.round(238 * 1.08 * 0.1),
    image: new URL('@/assets/product/product65.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '360g'
  },
  {
    id: 66,
    name: '娃哈哈 百合莲子八宝粥',
    price: Math.round(238 * 1.08),
    code: '470000000066',
    point: Math.round(238 * 1.08 * 0.1),
    image: new URL('@/assets/product/product66.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '360g'
  },
  {
    id: 67,
    name: '娃哈哈八宝粥 木糖醇 ',
    price: Math.round(238 * 1.08),
    code: '470000000067',
    point: Math.round(238 * 1.08 * 0.1),
    image: new URL('@/assets/product/product67.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '360g'
  },
  {
    id: 68,
    name: '乡姑 红油榨菜丝',
    price: Math.round(118 * 1.08),
    code: '470000000068',
    point: Math.round(118 * 1.08 * 0.1),
    image: new URL('@/assets/product/product68.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '150g'
  },
  {
    id: 69,
    name: '吉香居 咸菜 麻辣三丝',
    price: Math.round(138 * 1.08),
    code: '470000000069',
    point: Math.round(138 * 1.08 * 0.1),
    image: new URL('@/assets/product/product69.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '180g'
  },
  {
    id: 60,
    name: '王致和 韭菜花酱',
    price: Math.round(258 * 1.08),
    code: '470000000070',
    point: Math.round(258 * 1.08 * 0.1),
    image: new URL('@/assets/product/product70.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '320g'
  },
  {
    id: 71,
    name: '吉香居 咸菜 红油豇豆',
    price: Math.round(168 * 1.08),
    code: '470000000071',
    point: Math.round(168 * 1.08 * 0.1),
    image: new URL('@/assets/product/product71.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '150g'
  },
  {
    id: 72,
    name: '王致和 红辣腐乳 豆腐乳',
    price: Math.round(328 * 1.08),
    code: '470000000072',
    point: Math.round(328 * 1.08 * 0.1),
    image: new URL('@/assets/product/product72.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '340g'
  },
  {
    id: 73,
    name: '王致和 大块红腐乳',
    price: Math.round(328 * 1.08),
    code: '470000000073',
    point: Math.round(328 * 1.08 * 0.1),
    image: new URL('@/assets/product/product73.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '340g'
  },
  {
    id: 74,
    name: '老干妈 辣三丁油辣椒',
    price: Math.round(328 * 1.08),
    code: '470000000074',
    point: Math.round(328 * 1.08 * 0.1),
    image: new URL('@/assets/product/product74.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '280g'
  },
  {
    id: 75,
    name: '老干妈 风味豆豉油辣椒',
    price: Math.round(328 * 1.08),
    code: '470000000075',
    point: Math.round(328 * 1.08 * 0.1),
    image: new URL('@/assets/product/product75.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '280g'
  },
  {
    id: 76,
    name: '老干妈 牛肉味豆豉油辣椒',
    price: Math.round(328 * 1.08),
    code: '470000000076',
    point: Math.round(328 * 1.08 * 0.1),
    image: new URL('@/assets/product/product76.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '210g'
  },
  {
    id: 77,
    name: '铁成东北酸菜',
    price: Math.round(158 * 1.08),
    code: '470000000077',
    point: Math.round(158 * 1.08 * 0.1),
    image: new URL('@/assets/product/product77.jpg', import.meta.url).href,
    ingredients: '略',
    origin: '中国',
    weight: '500g/袋'
  }
  
]

// 根据 ID 找出对应的商品
const product = computed(() => productList.find(p => p.id === id))
</script>

<style scoped>
/* 通用字体设置 */
* {
  font-family: 'Noto Sans JP', 'Helvetica Neue', Arial, sans-serif;
  box-sizing: border-box;
}

/* 页面容器设置 */
.home-container {
  display: flex;
  flex-direction: row;
  padding: 20px 40px;
  gap: 24px;
  background: #f1e7cb;
}

/* 商品详情容器 */
.product-detail-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 32px;
  background: #fff;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
  flex: 1;
}

/* 左侧图片区域 */
.left-section {
  width: 360px;
  flex-shrink: 0;
}

.main-image {
  width: 100%;
  border-radius: 8px;
  border: 1px solid #ccc;
  cursor: zoom-in;
}

.thumbnail-list {
  display: flex;
  gap: 8px;
  margin-top: 8px;
}

.thumbnail {
  width: 60px;
  height: 60px;
  object-fit: cover;
  border-radius: 4px;
  border: 1px solid #ccc;
}

/* 右侧详情信息区域 */
.right-section {
  flex: 1;
  min-width: 280px;
}

.product-title {
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 12px;
  color: #333;
}

.product-code {
  font-size: 13px;
  color: #888;
  margin-bottom: 8px;
}

.product-price {
  font-size: 18px;
  margin-bottom: 8px;
}

.label {
  font-weight: bold;
}

.price {
  color: #d40000;
  font-weight: bold;
}

.product-point {
  font-size: 14px;
  color: #666;
  margin-bottom: 12px;
}

.product-qty {
  font-size: 14px;
  margin-bottom: 16px;
}

select {
  margin-left: 8px;
  padding: 6px 8px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

/* 按钮区域 */
.action-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 16px;
}

.btn {
  padding: 10px 20px;
  font-size: 14px;
  border: none;
  cursor: pointer;
  border-radius: 6px;
  transition: 0.2s ease-in-out;
}

.add-to-cart {
  background-color: #d40000;
  color: white;
}

.favorite {
  background-color: #333;
  color: white;
}

.btn:hover {
  opacity: 0.9;
}

/* 描述区域 */
.description-block {
  margin-top: 20px;
  background: #f9f9f9;
  padding: 12px 16px;
  border-radius: 6px;
}

.desc-title {
  font-weight: bold;
  font-size: 15px;
  margin-bottom: 4px;
}

.desc-text {
  font-size: 14px;
  margin-bottom: 4px;
  color: #444;
}

/* 图片放大遮罩层 */
.zoom-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.85);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.zoom-image {
  max-width: 90%;
  max-height: 90%;
  border-radius: 8px;
  cursor: zoom-out;
}

/* ------------------------- */
/* ✅ 响应式支持：移动端样式 */
/* ------------------------- */
@media (max-width: 768px) {
  .home-container {
    flex-direction: column;
    padding: 16px;
  }

  .product-detail-container {
    flex-direction: column;
    padding: 16px;
  }

  .left-section {
    width: 100%;
  }

  .thumbnail-list {
    justify-content: center;
  }

  .right-section {
    width: 100%;
  }

  .btn {
    flex: 1 1 100%;
  }
}

</style>
