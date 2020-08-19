<template>
    <div class="container">
        <map-component/>
        <hr>

    <v-container>
      <v-row no-gutters>
        <v-col>
          <img class = "scale" id = "image" v-on:click="search('돈까스')" src="../assets/katsu.jpg"/>
        </v-col>
        <v-col><img class = "scale" id = "image" v-on:click="search('파스타')" src="../assets/pasta.jpg"/></v-col>
        <v-col><img class = "scale" id = "image" v-on:click="search('짜장면')" src="../assets/blackbean.jpg"/></v-col>
      </v-row>
    </v-container>
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
          console.log('https://i3a503.p.ssafy.io/'+'search/result/'+word)
          this.$router.push({ name: 'SearchResult', params: { keyword: word }})
          // this.$router.push('search/result/'+ word)
          // location.replace('https://i3a503.p.ssafy.io/'+'search/result/'+word)
        },
    }
}
</script>

<style>

#image {
  cursor:pointer; 
  width:300px;
  height: 250px;
  display: inline-block;
  transition: .5s ease;
  backface-visibility: hidden;
}

/* .container:hover .image {
  opacity: 0.3;
} */
/* 
.text {
  background-color: #4CAF50;
  color: white;
  font-size: 16px;
  padding: 16px 32px;
} */

.scale {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;   /* 부드러운 모션을 위해 추가*/
}
.scale:hover {
  transform: scale(1.5);
  -webkit-transform: scale(1.5);
  -moz-transform: scale(1.5);
  -ms-transform: scale(1.5);
  -o-transform: scale(1.5);
  opacity: 0.3;
}
</style>