<template>
  <div class="product-card" @click="goToDetail">
    <img :src="product.image" :alt="product.name" class="product-image" />
    <div class="product-info">
      <h3 class="product-name">{{ product.name }}</h3>
      <p class="product-price">￥{{ product.price }}</p>
      <button class="add-btn" @click.stop="$emit('add-to-cart', product)">
        {{ $t('chart.add_to_cart') }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const props = defineProps({ product: Object })
const router = useRouter()

const goToDetail = () => {
  router.push({ name: 'ProductDetail', params: { id: props.product.id } })
}
</script>

<style scoped>
.product-card {
  border: 1px solid #ddd;
  border-radius: 6px;
  background-color: #fff;
  overflow: hidden;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s;
  display: flex;
  flex-direction: column;
}

.product-card:hover {
  transform: translateY(-4px);
}

.product-image {
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
}

.product-info {
  padding: 12px;
  text-align: center;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.product-name {
  font-size: 14px;
  margin-bottom: 8px;
}

.product-price {
  font-size: 16px;
  font-weight: bold;
  color: #c63;
  margin-bottom: 10px;
}

.add-btn {
  padding: 6px 12px;
  background-color: #2b7bc6;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.add-btn:hover {
  background-color: #1a5da0;
}
</style>
