<template>
        <div class="container">
        
        <p>{{this.$route.params.ruid}}님의 가게 정보</p>
        <router-link :to="{name: 'reg', params: { ruid: this.$route.params.ruid}}" class="black--text">등록</router-link>
        <div v-if="rsts">
            <v-container fluid>
            <v-row>
                <v-card flat v-for="(rst, index) in rsts" :key="index + '_rsts'">
                    <div v-if="rst.rimage" ><v-img :src="rst.rimage"  id="rimg"></v-img></div>
                    <div v-else><v-img src="../../assets/noimage.png"  id="rimg"></v-img></div>
                    <h3><router-link :to="{ name: 'storeDetail', params: { rid: rst.rid }}">{{rst.rname}}</router-link></h3><br>
                    전화번호 : {{rst.rphone}}<br>
                    주소 : {{rst.raddr}}
                    <b-link v-b-modal = "'modRst'" @click="sendInfo(rst)">수정</b-link>&nbsp;
                    <b-link v-b-modal = "'delRst'" @click="sendInfo(rst)">삭제</b-link>
                </v-card>
            </v-row>
        </v-container>
        </div>

        <!-- 레스토랑 수정하는 모달 창-->
        <b-modal id="modRst" title="레스토랑 수정" @ok="modhandleSubmit()">
            <form>
                <b-form-group invalid-feedback="required">
                    이름<b-form-input v-model="newname"/>
                    지점<b-form-input v-model="newbranch"/>
                    번호<b-form-input v-model="newphone"/>
                    주소<b-form-input v-model="newaddr"/>
                    <!-- 이미지 업로드 or 이미지 주소 복사(현재는 이미지 주소) -->
                    이미지<b-form-input v-model="newimage" required></b-form-input>
                    부가설명<b-form-input v-model="newdescription"/>
                 </b-form-group>
            </form>
        </b-modal>

        <!-- 메뉴 삭제하기 모달 창-->
        <b-modal id="delRst" title="메뉴삭제" @ok= delhandleSubmit(rid)><p>{{newname}}을(를) 정말 삭제 하시겠습니까?</p></b-modal>


    </div>
</template>

<script>
    import axios from 'axios';
    import constants from "../../constants.js";
    const BACKEND_URL = constants.URL
    export default {
        name:'mystore',
        props: {
            ruid: String //declare props type
        },
        components: {
            
        },
        mounted() {
            axios.get(BACKEND_URL + 'rst/list?uid='+this.$route.params.ruid).then(({ data }) => {
                console.log(BACKEND_URL + '/rst/list?uid='+this.$route.params.ruid)
                this.rsts = data;
            })
        },
        methods: {
            //레스토랑 정보 수정
            modhandleSubmit: function() {
                console.log("mod 도달")
                axios
                .post(BACKEND_URL + 'rst/mod' , { 'rid':this.rid, 
                                                  'rname':this.newname,      
                                                  'rbranch':this.newbranch,
                                                  'rphone':this.newphone,
                                                  'raddr':this.newaddr,
                                                  'rimage':this.newimage,
                                                  'rdescription':this.newdescription
                                                  })
                .then(response => {
                    console.log(response.data)
                    this.$nextTick(() => {
                        this.$bvModal.hide('modRst')
                    })
                    
                   // this.facebookLogin();
                        
                })
            },
            sendInfo(rst) {
                this.rid = rst.rid,
                this.newname = rst.rname,
                this.newbranch = rst.rbranch,
                this.newphone = rst.rphone,
                this.newaddr = rst.raddr,
                this.newimage = rst.rimage,
                this.newdescription = rst.rdescription
                console.log("sendInfo확인"+this.newname)
            },

            //레스토랑 정보 삭제
            delhandleSubmit: function(rid) {
                console.log("삭제할 메뉴 번호:"+ rid);
                axios.get(BACKEND_URL + 'rst/del?rid=' + rid).then(response => {
                    console.log(response.data)
                    this.$nextTick(() => {
                        this.$bvModal.hide('delRst')
                        })
                    })
            },
        },
        data: () => {
            return {
                rid:'',
                rsts: [],
                
                newname:'',
                newbranch:'',
                newphone:'',
                newaddr:'',
                newimage:'',
                newdescription:''
            }
        }
    }
</script>

<style>
* {
    margin: 0;
    padding: 0px;
}
.table {
    margin:auto;
    width:60%;
    text-align:left;
}
.left{
    position:fixed; 
    top:10%; 
    left:0px; 
    width:250px; 
    height:80%; 
    background-color: transparent;
    padding:40px 0; 
    overflow: hidden
  }
.left ul {padding: 0 30px; list-style:none;}
.left ul li { font-size:25px;  height:75px;} 
</style>