<template>
  <div id="store-container">
      <store v-for="(index, s) in sample" :key="index" :content="s"/>
  </div>
</template>

<script>
import Store from './Store.vue';

export default {
    name: 'StoreList',
    components: {
        Store
    },
    data() {
        return {
            sample: [1,2,3]
        }
    }

}
</script>

<style scoped>
#store-container {
    display: grid;
    grid-template-rows: repeat(3, 1fr);
    grid-row-gap: 5px;
}
</style>