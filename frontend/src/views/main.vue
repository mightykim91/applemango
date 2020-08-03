<template>
    <div id="main">
    <main-header/>
    <dir>main page</dir>
    
    </div>
</template>

<script>

import Header from '../components/Header.vue'

export default {
    name : 'main',
    data() {
        return {
           
        }
       
    },
    components :{
        'main-header' : Header
    },
    methods: {
        
    }
}
</script>

<style>

</style>