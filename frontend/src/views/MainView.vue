<template>
    <div class="container">
        <map-component/>
        <hr>
    <v-container>
      <v-row no-gutters>
        <img class = "image" v-on:click="search('돈까스')" src="../assets/katsu.jpg"/>
        <div class = "middle"><div class="text">돈까스</div></div>
      </v-row>
      <hr><h1>#파스타</h1>
      <v-row no-gutters>
        <img v-on:click="search('파스타')" style="cursor:grab; width:50%" src="../assets/pasta.jpg"/>
      </v-row>
      <v-row no-gutters>
        <img v-on:click="search('짜장면')" style="cursor:grab; width:50%" src="../assets/blackbean.jpg"/>
      </v-row>
     
      
    </v-container>
    <!-- <div class="container">
        <img src="../assets/katsu.jpg" class="image" style="width:20%">
        <div class="middle">
            <div class="text" href="search/result/짜장면">돈까스</div>
        </div>
    </div>
    <br>

    <div class="container">
        <img src="../assets/pasta.jpg" alt="Avatar" class="image" style="width:20%">
        <div class="middle">
            <div class="text">파스타</div>
        </div>
    </div>

    <div class="container">
          <img src="../assets/blackbean.jpg" alt="Avatar" class="image" style="width:20%">
          <div class="middle">
              <div class="text">짜장면</div>
          </div>
    </div> -->

    </div>
</template>

<script>
import MapComponent from '../components/mainView/MapComponent.vue'
// import constants from "../constants.js";
// const BACKEND_URL = constants.URL

export default {
    name : 'Home',
    components: {
        'map-component': MapComponent
    },
    // data() {
    //     return {
    //     }
    // }
    methods: {
        search: function(word){
          console.log(word)
          this.$router.push({ name: 'SearchResult' , params:{'keyword':this.keyword}})
        },
    }
}
</script>

<style>

.image {
  cursor:grab; 
  width:50%;
  height: auto;
  opacity: 1;
  display: block;
  transition: .5s ease;
  backface-visibility: hidden;
}

.middle {
  transition: .5s ease;
  opacity: 0;
  position:absolute;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  text-align: center;
}

.container:hover .image {
  opacity: 0.3;
}

.container:hover .middle {
  opacity: 1;
}

.text {
  background-color: #4CAF50;
  color: white;
  font-size: 16px;
  padding: 16px 32px;
}
</style>