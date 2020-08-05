/* Join.vue */

<template>
    <div id="mypage">
    <main-header/>
    <div>
    <br><br>
        <h1>즐겨찾기 리스트</h1>
        
        <!--크롤링 데이터 리스트 컨테이너-->
    <v-container id="favorlist" style="border-bottom:solid 1px">
        
        <v-list>
            <template  v-for="favors in favorlist">
                <v-list-item :key="favors.fid" v-bind:to= "{ name: 'storeDetail', params: { rid: favors.frid }}">
                    <v-list-item-avatar>
                        <v-img :src="favors.restaurant.rid"></v-img>
                    </v-list-item-avatar>
                    <v-list-item-content>
                    <v-list-item-title v-text="favors.restaurant.rname"></v-list-item-title>
                    <v-list-item-subtitle v-text="favors.restaurant.rbranch"></v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
            </template>
        </v-list>
    </v-container>
    </div>

    </div>
</template>


<script>
    import axios from 'axios'
    import constants from "../../constants.js"; 
  
    const BACKEND_URL = constants.URL
    
    export default  {
        data() {
            return {
                user : {
                    id : '',
                    password : ''
                },
                favorlist : []
            }

        },
        methods : {

        },

        mounted(){
            
            axios.get(`${BACKEND_URL}user/favors/list/${this.$cookies.get('auth-token')}`)
            .then(response => {
                this.favorlist = response.data;
                console.log(response);
            })

            axios.get(`${BACKEND_URL}user/favors/detail/${this.data.favorlist.rid}`)
            .then(response => {
                this.favorlist = response.data;
                console.log(response);
            })
        },
        created () {
        }
    }
</script>
