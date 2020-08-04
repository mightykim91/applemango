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
                    <button>{{favors}}</button>
                </v-card>
            </v-row>
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
                favorlist : {
                    uid : '',
                    rid : ''
                }
            }

        },
        methods : {

        },

        mounted(){
            
            axios.get(`${BACKEND_URL}user/favors/${this.$cookies.get('auth-token')}`)
            .then(response => {
                this.favorlist = response.data;
                console.log(response);
            })
        },
        created () {
        }
    }
</script>
