<template>
  <v-app id="app">
    <v-system-bar app>
      <v-row justify="end" no-gutters v-if="!this.$cookies.isKey('auth-token')">
        <v-col cols="1" class="px-1"><router-link :to="{name: 'Login'}" class="black--text">로그인</router-link></v-col>
        <v-col cols="1" class="px-1"><router-link :to="{name: 'SignUp'}" class="black--text">회원가입</router-link></v-col>
      </v-row>
      <v-row justify="end" no-gutters v-else>
        <v-col cols="1" class="px-1"><span v-on:click="logout" class="text--black" style="cursor:grab">로그아웃</span></v-col>
      </v-row>
    </v-system-bar>
    <navigation/>
    <v-main>
      <v-container fluid class="mt-12">
        <router-view></router-view>
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

import NewHeader from '@/components/NewHeader.vue'
import axios from 'axios'
import constants from '../src/constants.js'

const BACKEND_URL = constants.URL

export default {

  components: {
    'navigation' : NewHeader
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
                    location.reload();
                })
        }
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
