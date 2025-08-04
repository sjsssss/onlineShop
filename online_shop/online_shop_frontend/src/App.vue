<script setup></script>

<template>
  <!-- <Navbar @toggle-sidebar="showSidebar = !showSidebar" /> -->
  <NavBar />
  <div class="main">
    <router-view />
  </div>
</template>


<script setup>
import NavBar from './components/common/NavBar.vue'
</script>

<style scoped>
.main{
  background-color: #f1e7cb;
    min-height: 100vh;
  margin: 0;
  padding: 0;
  overflow-x: hidden; /* 避免横向滚动带来的空白 */
}
</style>