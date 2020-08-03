<template>
  <v-app id="app">
    <v-system-bar app>
      <v-row justify="end" no-gutters v-if="!this.$cookies.isKey('auth-token')">
        <v-col cols="1" class="px-1"><router-link :to="{name: 'Login'}" class="black--text">로그인</router-link></v-col>
        <v-col cols="1" class="px-1"><router-link :to="{name: 'SignUp'}" class="black--text">회원가입</router-link></v-col>
      </v-row>
      <v-row justify="end" no-gutters v-else>
        <v-col cols="1" class="px-1">로그아웃</v-col>
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

export default {

  components: {
    'navigation' : NewHeader
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
