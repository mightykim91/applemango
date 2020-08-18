<template>
    <div class="container">
        <map-component/>
        <hr>

    <v-container>
      <v-row no-gutters>
        <v-col><img class = "image" v-on:click="search('돈까스')" src="../assets/katsu.jpg"/></v-col>
        <v-col><img class = "image" v-on:click="search('파스타')" src="../assets/pasta.jpg"/></v-col>
        <v-col><img class = "image" v-on:click="search('짜장면')" src="../assets/blackbean.jpg"/></v-col>
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
          console.log('https://i3a503.p.ssafy.io/'+'search/result/'+word)
          this.$router.push('search/result/'+ word)
          // location.replace('https://i3a503.p.ssafy.io/'+'search/result/'+word)
        },
    }
}
</script>

<style>

.image {
  cursor:grab; 
  width:300px;
  height: 250px;
  display: inline-block;
  transition: .5s ease;
  backface-visibility: hidden;
}

.middle {
  transition: .5s ease;
  position:absolute;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  text-align: center;
}

/* .container:hover .image {
  opacity: 0.3;
} */
.text {
  background-color: #4CAF50;
  color: white;
  font-size: 16px;
  padding: 16px 32px;
}
</style>