/* Join.vue */

<template>
    <div id="mypage">
    <main-header/>
    <div>
    <br><br>
        <h1>즐겨찾기 리스트</h1>
        
        <!--크롤링 데이터 리스트 컨테이너-->
        <v-container fluid>
            <v-row>
                <v-card flat class="text-xs-center ma-3" v-for="favors in favorlist" v-bind:key="favors.rid">                    
                    <button>{{favors}}</button><br>
                    <button>{{favors.uid}}</button><br>
                    <button>{{favors.rid}}</button>
                </v-card>
            </v-row>
        </v-container>

        <v-list>
            <template  v-for="favors in favorlist">
                <v-list-item :key="favors.fid">
                    {{favors}}

                </v-list-item>
            </template>
        </v-list>
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
                favorlist : {
                    fid : '',
                    uid : '',
                    rid : ''
                }
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
