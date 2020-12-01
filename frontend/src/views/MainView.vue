<template>
<div>
    <h1 id="map-header">내 주변 맛집</h1>
    <hr id="map-division-line">
    <div class="map-container">
      <!-- <map-component/> -->
      <newMapComponent class="item-map"/>
      <!-- <v-container>
        <v-row no-gutters>
          <v-col class = "scale" v-on:click="search('돈까스')">
              <img id = "image" src="../assets/katsu.jpg"/>
              <div class="text" >돈까스</div>
          </v-col>
          <v-col class = "scale" v-on:click="search('파스타')">
              <img id = "image" src="../assets/pasta.jpg"/>
              <div class="text">파스타</div>
          </v-col>
          <v-col class = "scale" v-on:click="search('짜장면')">
              <img id = "image" src="../assets/blackbean.png"/>
              <div class="text">짜장면</div>
          </v-col>
        </v-row>
      </v-container> -->
      <store-list class="item-store"></store-list>
    </div>
</div>
</template>

<script>
// import MapComponent from '../components/mainView/MapComponent.vue'
import NewMapComponent from '../components/mainView/newMapComponent.vue'
import StoreList from '../components/mainView/StoreList.vue'
// import constants from "../constants.js";
// const BACKEND_URL = constants.URL

export default {
    name : 'Home',
    components: {
        // 'map-component': MapComponent,
        NewMapComponent,
        StoreList
    },
    // data() {
    //     return {
    //     }
    // }
    methods: {
        search: function(word){
          console.log('https://i3a503.p.ssafy.io/'+'search/result/'+word)
          this.$store.commit('search', word)
          this.$router.push({ name: 'SearchResult', params: { keyword: word }})
          // this.$router.push('search/result/'+ word)
          // location.replace('https://i3a503.p.ssafy.io/'+'search/result/'+word)
        },
    }
}
</script>

<style scoped>

@font-face {
    font-family: 'BinggraeMelona-Bold';
    src: url('../assets/fonts/BinggraeMelona-Bold.ttf') format('truetype');
}

#map-header {
    font-family: 'BinggraeMelona-Bold';
    text-align: left;
    margin-bottom: 0;
}

#map-division-line {
    margin-top: 5px;
    margin-bottom: 10px;
    border: 0;
    width: 1200px;
    height: 2px;
    background-color: #ffaa2b;
}

.map-container {
  display: flex;
  width: 1200px;
  height: 500px;
}

.item-map {
  width: 800px;
  height: 500px;
}

.item-store {
  margin-left: 5px;
  width: 400px;
  height: 500px;
}

.scale {
  cursor:pointer;
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;   /* 부드러운 모션을 위해 추가*/
}
.scale:hover {
  transform: scale(1.6);
  -webkit-transform: scale(1.6);
  -moz-transform: scale(1.6);
  -ms-transform: scale(1.6);
  -o-transform: scale(1.6);
}

#image { 
  width:300px;
  height: 250px;
  display: inline-block;
  transition: .5s ease;
  backface-visibility: hidden;
}

.text {
  opacity: 0;
  font-weight: bold;
  transform: translate( -50%, -50% );
  position: absolute;
	top: 50%;
	left: 50%;
  font-size: 32px;
  color: black;
  /* background-color: gold; */
  /* padding: 8px 16px; */
}

.scale:hover #image {
  opacity: 0.5;
}

.scale:hover .text {
  opacity: 1;
}

</style>