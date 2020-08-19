<template>
        <div class="box" style="max-width: 1720px; max-height:auto">
        
        <p>{{this.$route.params.ruid}}님의 가게 <router-link :to="{name: 'reg', params: { ruid: this.$route.params.ruid}}" class="black--text">
                                                    <v-icon color="green">mdi-file-plus</v-icon>
                                                </router-link></p>
        
        <div v-if="rsts" class="wrapper">
            <a v-for="(rst, index) in rsts" :key="index + '_rsts'">
                <figure>
                    <img v-if="rst.rimage" :src="rst.rimage"  id="rimg"/>
                    <img v-else src="../../assets/noimage.png"  id="rimg"/>
                    <figcaption>
                        <h3 style="text-align:center;"><router-link :to="{ name: 'storeDetail', params: { rid: rst.rid }}">{{rst.rname}}</router-link></h3><br>
                        <v-icon>mdi-phone</v-icon> {{rst.rphone}}<br>
                        <v-icon>mdi-map-marker</v-icon> {{rst.raddr}}<br><br>
                        <v-icon class="mx-2" style="float:right;" fab large dark color="red" v-b-modal = "'delRst'" @click="sendInfo(rst)">mdi-delete</v-icon>
                        <v-icon class="mx-2" style="float:right;" fab large dark color="cyan" v-b-modal = "'modRst'" @click="sendInfo(rst)">mdi-pencil</v-icon>

                        <!-- <b-link v-b-modal = "'modRst'" @click="sendInfo(rst)">수정</b-link>&nbsp; -->
                        <!-- <b-link v-b-modal = "'delRst'" @click="sendInfo(rst)">삭제</b-link> -->   
                    </figcaption>
                </figure>
            </a>
        </div>
        <div v-else>
            등록된 상점이 없습니다.
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
                    이미지<b-form-input v-model="newimage"/>
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
.wrapper{
    column-count: 4;
    column-gap: 10px;
    column-width: 300px;
    -webkit-column-count: 4;
    -webkit-column-gap: 10px;
    -webkit-column-width: 300px;
}

.wrapper figure{
    display: inline-block;
    border: 1px solid rgba(0,0,0,0.2);
    width: 350px;
    height: 500px;
    margin: 0;
    margin-bottom: 10px;
    padding: 3px;
}
.wrapper figure img{
    width: 100%;
}
.wrapper figure figcaption{
    border-top: 1px solid rgba(0,0,0,0.2);
    padding: 10px;
    margin-top: 3px;
    text-align: left;
}

/* .card{
    display: inline-block;
    width: 300px;
    height: 500px;
    border: 1px solid #cecece;
    text-align: left;
    margin-top: 5px;
}
.card img{
    width: 100%;
    border: 1px solid #cecece;
    margin-top: 0;
} */




</style>