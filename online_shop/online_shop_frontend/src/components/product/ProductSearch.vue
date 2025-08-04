<template>
  <div class="product-search">
    <h2>{{ $t('product_search.title') }}</h2>

    <div class="search-row">
      <label>{{ $t('product_search.category') }}</label>
      <select v-model="form.category">
        <option value="">{{ $t('product_search.all_categories') }}</option>
        <option value="frozen">冷凍食品</option>
        <option value="snacks">お菓子</option>
      </select>

      <label>{{ $t('product_search.keyword') }}</label>
      <input v-model="form.keyword" type="text" />
      <label>{{ $t('product_search.price') }}</label>
      <input v-model="form.minPrice" type="number"/>
      <span>~</span>
      <input v-model="form.maxPrice" type="number"/>
      <button @click="submitSearch">{{ $t('product_search.search') }}</button>

    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['search'])

const form = ref({
  category: '',
  keyword: '',
  minPrice: '',
  maxPrice: ''
})

function submitSearch() {
  emit('search', form.value)
}
</script>

<style scoped>
.product-search {
  background: #f1e7cb;
  /* border: 1px solid #a1a0a0; */
  padding: 16px;
  margin: 20px 0;
  font-size: 0.95rem;
}

.search-row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
}

input,
select {
  padding: 6px 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

button {
  padding: 8px 16px;
  font-size: 14px;
  background-color: #444;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
