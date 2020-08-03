/* header.vue */

<template>
<div class = "header">
    <div  v-if="$cookies.isKey('auth-token')">
    <div style="float:right">
        <b-avatar></b-avatar>
        {{$cookies.get('auth-token')}} 님 환영합니다.
        <a href="#" class="btn" v-on:click="logout()" >로그아웃</a>
    </div>
        <!--로고(홈버튼)-->
        <router-link to="/" class="btn--text" style="color:black;">
            <img id="apmg" src = "../assets/applemango.png"/></router-link>
        <div class = "topnav">
            <b-nav tabs>
                <b-nav-item exact exact-active-class="active" to = "/">Main</b-nav-item>
                <b-nav-item exact exact-active-class="active">My Page</b-nav-item>
                <b-nav-item exact exact-active-class="active" v-bind:to= "{ name: 'mystore', params: { ruid: 'test' }}">My Store</b-nav-item>
                <b-nav-item disabled>Disabled</b-nav-item>
            </b-nav>
    </div>
    </div>
    <div v-else>
            <router-link to="/user/login" class="btn--text" >로그인</router-link>
    </div>
</div>

</template>
<script>

import axios from 'axios'
    
const BACKEND_URL = 'http://localhost:8080/'

export default {
    name : 'main-header',
    data: () => {
        return {
            
        }
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
.header {
    background-color: gold;
    width : 100%;
    height: 200px;
    text-align: center;
    padding: 10px;
}
/* Style the topnav links */
.topnav {
  display: block;
  color: #f2f2f2;
  padding: auto;
  text-align: center;
  margin-left: 80%;
  margin-top:2%;
}
#apmg {
    width:240x;
    height: 100px;
}
</style>