<template>
    <div>
        <h1>검색결과</h1>
        <div class="d-flex justify-center">
            <v-card class="my-3" v-for="rst in restaurants" v-bind:key="rst.id" width="500">
                <v-container class="ma-0 pa-0">
                    <v-row>
                        <v-col cols="3" class="d-flex justify-center align-center">
                            <div id="logo-container" class="rounded-circle p-3" style="background-color:gray">
                                <v-icon large>fa-utensils</v-icon>
                            </div>
                        </v-col>
                        <v-col cols="9">
                            <v-card-title>
                                <v-btn text @click="goDetail(rst.rid)" class="pa-0 ma-0 text-h6">
                                    {{ rst.rname }}
                                </v-btn>    
                            </v-card-title>
                            <v-card-text class="text-left">
                                <p>주소: {{ rst.raddr }}</p>
                                <p>연락처: {{ rst.rphone }}</p>
                            </v-card-text>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card>
        </div>
    </div>
</template>

<script>
import constants from '../../constants.js'

import axios from 'axios'

const BACKEND_URL = constants.URL

export default {
    name: 'SearchResult',
    mounted() {
        this.search(this.$store.getters.getKeyword)
    },
    data(){
        return {
            allMenus: [],
            restaurants: [],
        }
    },
    methods:{
        search: function(keyword){
            var allMenus = ''
            axios.get(BACKEND_URL + 'menu/all')
            .then(response => {
                allMenus = response.data //전체메뉴
                
                //검색어로 필터링
                var restaurants = new Set();
                allMenus.forEach(menu => {
                    if (menu.mname === keyword){
                        restaurants.add(menu.mrid) //레스토랑id, 메뉴이름
                    }
                })//END OF FOR EACH
                restaurants = Array.from(restaurants)
                restaurants.forEach(rst => {
                    axios.get(BACKEND_URL + 'rst/detail?rid=' + rst)
                    .then(response => {
                        this.restaurants.push(response.data)
                        
                    })
                })

            })//END OF GET RESPONSE
            
        },
        goDetail: function(restaurantId){
            this.$router.push({name: 'storeDetail', params:{ rid: restaurantId }})
        }
    },
}
</script>

<style>

</style>