<template>
  <div id="app">
    <Header :isHeader="isHeader"/>

  

<input type="button" class="big-button" value="페이스북 로그인" @click="facebookLogin()"/>

<p id="status"></p>

<input type="button" class="big-button" value="페이스북 로그아웃" @click="facebookLogout()"/>
 
    <!-- <router-view/> -->



  </div>
</template>


<script src="https://use.fontawesome.com/releases/v5.2.0/js/all.js"></script>  
<script> 
import './assets/css/style.scss' 
import Header from './components/common/Header.vue'
import constants from './lib/constants' 
import Facebook from './Facebook.js'

export default {
  name: 'App',
  components: { 
    Header
  },
  created() {
      let url = this.$route.name;
      if(!window.FB) Facebook.Init();
      this.checkUrl(url);
  },
  watch: {
      $route (to){

          this.checkUrl(to.name);
      }
  },
  methods : {
      checkUrl(url) { 

          let array = [
              constants.URL_TYPE.USER.LOGIN,
              constants.URL_TYPE.USER.JOIN,
          ];

          let isHeader = true;
          array.map(path => {
              if (url === path)
                  isHeader = false;
          })
          this.isHeader = isHeader;

      },
      facebookLogin(){
        if(localStorage.getItem('JWT_token')) return alert('이미 로그인 되어 있습니다.');
        Facebook.Login();
      },
      facebookLogout(){
        Facebook.Logout();
      }
      
  },
  data: function () {
        return {
            isHeader: true,
            constants
        } 
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; 
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
