/* login.vue */

<template>
    <div id="receive-insta">
    <main-header/>
    <div>
    <br><br>
        <h1>인스타 크롤링 사진 데이터 리스트</h1>
        
        <!--크롤링 데이터 리스트 컨테이너-->
        <v-container fluid>
            <v-row>
                <v-card flat class="text-xs-center ma-3" v-for="instadata in instadatalist" v-bind:key="instadata.instaid">
                    
                    <v-img :src="instadata.iurl"  max-width="200" max-height="300" ></v-img>
                     <b-button id="show-btn" @click="$bvModal.show('show-menu-modal')">메뉴 변경</b-button>
                    <input v-model="mid" placeholder="변경할 메뉴 mid - demo"><br>
                    <button v-on:click="changePicture(instadata.iurl,mid)">사진 변경</button>
                </v-card>
            </v-row>
        </v-container>

    </div>

    <div>
    <!-- 메뉴선택 Modal-->
    <b-modal id="show-menu-modal" hide-footer>
        <template v-slot:modal-title>
        메뉴 선택<code>$bvModal</code>
        </template>
        <div class="d-block text-center">


        </div>
        <b-button class="mt-3" block @click="$bvModal.hide('bv-modal-example')">Close Me</b-button>
    </b-modal>
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
            
            axios.get(`${BACKEND_URL}/instagram/select/1`) // select/{irid} 레스토랑 정보 인자로 받아와서 넣어주면 댐!
            .then(response => {
                this.instadatalist = response.data;
                console.log(response);
            })

            axios.get(BACKEND_URL + 'menu/list', {params: {'mrid':this.rid}})
            .then(response => {
                console.log("menu list:" + response.data)
                this.requestData.menus = response.data
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
