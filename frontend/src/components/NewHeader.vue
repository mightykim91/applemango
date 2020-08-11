<template>
    <v-app-bar app color="transparent" height="80">
        <v-row id="nav-menus">
            <v-col align-self="center" cols="2">
                <!-- <v-toolbar-title v-on:click="home" style="cursor:grab"></v-toolbar-title> -->
                <img id="logo" v-on:click="home" style="cursor:grab" src="../assets/applemango.png"/>
            </v-col>
            <v-col align-self="center" cols="3">
                <v-select
                :select="searchFilter"
                hide-details 
                solo 
                :items="searchOptions"
                v-model="searchFilter"></v-select>
            </v-col>
            <v-col align-self="center" cols="4">
                <v-text-field
                hide-details
                height="10px"
                single-line 
                solo placeholder="검색어를 입력해주세요"
                prepend-inner-icon="fa-search"
                v-model="searchWord"
                ></v-text-field>
                
            </v-col>
            <v-col align-self="center" cols="1">
                <v-btn>검색하기</v-btn>
            </v-col>
            <v-col align-self="center" cols="2">
                <v-icon
                class="pa-3"
                color="black" 
                v-if="this.$store.state.userType === 'Admin'"
                @click="$router.push({ name: 'AdminPage' })"
                >
                fa-user-cog
                </v-icon>
                <v-icon
                class="pa-3"
                color="black" 
                v-if="this.$cookies.get('auth-token')"
                >
                fa-envelope
                </v-icon>
            </v-col>
        </v-row>
    </v-app-bar>
</template>

<script>
// import axios from 'axios'
// import constants from '../constants.js'

import logo from '../assets/applemango.png'

// const BACKEND_URL = constants.URL

export default {

    name : 'NewHeader',
    data(){
        return {
            searchOptions : ['거리순', '평점순'],
            searchWord:'',
            searchFilter: '거리순',
            navLogo: logo,
            userType: ''
        }
    },
    // created(){
    //     if(this.$cookies.get('auth-token')){
    //         console.log(this.$cookies.get('auth-token'))
    //         axios.get(BACKEND_URL + 'user/info?uid=' + this.$cookies.get('auth-token'))
    //         .then(response => {
    //             console.log(response.data)
    //             this.userInfo = response.data
    //             if (response.data.ukind == 3){ //관리자
    //                 this.isAdmin = true
    //             }
    //             else if (response.data.ukind == 1){ //사업자
    //                 this.isOwner = true
    //             }
    //             else {
    //                 this.isCutomer = true //일반회원
    //             }
    //         })
    //     }
    // },
    methods:{
        home: function(){
            this.$router.push({ name: 'Home' })
        }
    }

}
</script>

<style scoped>
#logo{
    width:100px;
    height:70px;
}
</style>

