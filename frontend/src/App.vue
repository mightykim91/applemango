<template>
  <v-app id="app">
    <!--v-system-bar app>
      <v-row justify="end" no-gutters v-if="!this.$cookies.isKey('auth-token')">
        <v-col cols="1" class="px-1"><router-link :to="{name: 'Login'}" class="black--text">로그인</router-link></v-col>
        <v-col cols="1" class="px-1"><router-link :to="{name: 'SignUp'}" class="black--text">회원가입</router-link></v-col>
      </v-row>
      <v-row justify="end" no-gutters v-else>
        <v-col cols="1" class="px-1"><span v-on:click="logout" class="text--black" style="cursor:grab">로그아웃</span></v-col>
        <v-col cols="1" class="px-1"><router-link :to="{name: 'mystore', params: { ruid: $cookies.get('auth-token')}}" class="black--text">My Store</router-link></v-col>

      </v-row>
    </v-system-bar-->
    <navigation/>
    
    <v-main>
      <v-container fluid class="mt-12">
        <router-view :key="$route.fullPath"></router-view>
      </v-container>
    </v-main>
    <!-- <router-view></router-view> -->
  </v-app>
  <!--original code-->
  <!-- <div id="app">
    <router-view></router-view>
  </div> -->
</template>

<script>
import axios from 'axios'
import constants from '../src/constants.js'
import NewHeader from '@/components/NewHeader.vue'

// import Vue from "vue";
// export var eventBus = new Vue();

const BACKEND_URL = constants.URL

export default {
  data() {
    return {
      uid : this.$cookies.get('auth-token')
    }
  },
  components: {
    'navigation' : NewHeader,
    //하위 컴포넌트로 등록
    /* eslint-disable vue/no-unused-components */

  },
  methods : {
        logout : function () {
            this.$cookies.remove('auth-token');
            axios.get(BACKEND_URL + 'user/logout')
                .then(response => {
                    if (response.data.status){
                        alert("로그아웃 성공");
                        alert(response.data.object);
                        //this.setCookies(this.user.id);
                        //alert(ses);
                    }
                    //this.$router.push({ path: '/'}) 같은 페이지로 새로고침 시 오류
                    
                    //Vuex통해 로그인 상태관리
                    this.$store.commit('logout')
                    location.reload();
                })
        },
        getLocation: function(){
          if(navigator.geolocation){
            console.log('geolocation is allowed')
            navigator.geolocation.getCurrentPosition(position => {
              var lat = position.coords.latitude
              var lon = position.coords.longitude
              console.log(this.$store,lat,lon)
              this.$store.commit('getLocation', [lat, lon])
            })
          }
          else{
            console.log('geolocation is not allowed')
          }
        }
        //이벤트버스
        // send: function() {
        //   eventBus.$emit('sendUid', this.uid);
        //   console.log("app.vue에서 id값 보냄"+ this.uid)
        // }
    },
    // beforeMount(){
    //     this.send()
    // }
    mounted(){
      //위치정보
      this.getLocation()
      
    }
}
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
