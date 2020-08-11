/* login.vue */

<template>
    <div id="receive-insta">

    <div>
    <br><br>
        <h1>인스타 크롤링 사진 데이터 리스트</h1>
        
        <!--크롤링 데이터 리스트 컨테이너-->
        <v-container fluid>
            <v-row>
                <v-card flat class="text-xs-center ma-3" v-for="instadata in instadatalist" v-bind:key="instadata.instaid">
                    
                    <v-img :src="instadata.iurl"  max-width="200" max-height="300" ></v-img>
                    <input v-model="mid" placeholder="변경할 메뉴 mid - demo"><br>
                    <button v-on:click="changePicture(instadata.iurl,mid)">사진 변경</button>
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
        name: "InstaReceive",
         components :{
            
        },
        data() {
           return {
            instadatalist : {
                iid : '',
                rname : '',
                rbranch : '',
                instaid : '',
                iurl : '',
                likes : '',
                idate : ''

            },
            user : {
                    id : '',
                    password : ''
            },
            imageData : {
                    mid : '',
                    mimage : ''
            }
            
        }

        },
        methods : {
            changePicture: function(url,mid){
               this.imageData.mimage = url;
               this.imageData.mid = mid;
               axios.post(`${BACKEND_URL}instagram/update`,this.imageData)
                .then(response => {
                    console.log(this.imageData)
                    console.log(response.data)
                    this.comments.unshift(response.data) //새로운댓글 배열에 추가후 배열의 처음으로 이동.
                    
                    
              }) 
            }
        },
        mounted(){
            
            axios.get(`${BACKEND_URL}instagram/all`)
            .then(response => {
                this.instadatalist = response.data;
                console.log(response);
            })
        },

        created () {
        },
       /* watch:{
            imageData:function(){ //changePicture를 수행해서 imageData.mimage가 바뀌면 
              
              this.$router.push({ name: 'comment', params: { trigger : 123 }}) // IG Userid를 가져오는 함수 실행 
            },
        }, */ 
    }
</script>
