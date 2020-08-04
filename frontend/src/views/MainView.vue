<template>
    <div>
        <map-component/>
    </div>
</template>

<script>

// import Header from '../components/Header.vue'
// import NewHeader from '../components/NewHeader.vue'
import MapComponent from '../components/mainView/MapComponent.vue'

export default {
    name : 'main',
    components: {
        'map-component': MapComponent
    }
    // data() {
    //     return {
           
    //     }
       
    // },
    // components :{
    //     'main-header' : NewHeader
    // },
    // methods: {
        
    // }
}
</script>

<style>

</style>