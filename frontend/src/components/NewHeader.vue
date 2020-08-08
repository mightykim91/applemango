<template>
    <v-app-bar app color="transparent" height="80">
        <v-row id="nav-menus">
            <v-col align-self="center" cols="3">
                <!-- <v-toolbar-title v-on:click="home" style="cursor:grab"></v-toolbar-title> -->
                <img id="logo" src="../assets/applemango.png"/>
            </v-col>
            <v-col align-self="center" cols="2">
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
        </v-row>
    </v-app-bar>
</template>

<script>

import logo from '../assets/applemango.png'

export default {

    name : 'NewHeader',
    data(){
        return {
            searchOptions : ['거리순', '평점순'],
            searchWord:'',
            searchFilter: '거리순',
            navLogo: logo
        }
    },
    methods:{
        home: function(){
            this.$router.push({name: 'Home'})
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

