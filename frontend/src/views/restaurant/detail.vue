<template>
<div class="detail">
    <div class="container">
        
        <div class = "rstInfo">
        <p><font class="titlefont">{{requestData.rst.rname}} </font> {{requestData.rst.rbranch}} 지점</p><hr>
        <!-- 이미지 값 requestData.rst.rimg값으로 나중에 변경 -->
        <img id="sigimg" src = "https://www.dcapp.org/sites/default/files/styles/dcapp_business_logo/public/paik-korean-noodle-centreville.jpg?itok=JBkf5XVT"/>
        <pre><font class="content">
        {{requestData.rst.rdescription}}
        번호 {{requestData.rst.rphone}} 
        주소 {{requestData.rst.raddr}}
        </font></pre>
        </div>

        <br clear="left">

        <div class="menuInfo">
            
            <!-- 메뉴 등록 모달 창 -->
            Menu <b-button v-b-modal.regMenu>등록</b-button>
                 
            <b-modal id="regMenu" ref="modal" 
                title="메뉴 등록" @show="resetModal" @hidden="resetModal" @ok="reghandleOk">
                <form ref="form">
                    <b-form-group  
                        label-for="input" invalid-feedback="required">
                        이름<b-form-input v-model="newname"  required></b-form-input>
                        <b-form-checkbox v-model="newissig" requried>메인메뉴 </b-form-checkbox> 
                        가격 <b-form-input v-model="newprice" required></b-form-input>
                        <!-- 이미지 업로드 or 이미지 주소 복사(현재는 이미지 주소) -->
                        이미지 <b-form-input v-model="newimage" required></b-form-input>
                    </b-form-group>
                </form>
            </b-modal>
        <hr>
        <div v-if="requestData.menus.length > 0">
            <table class="table table-bordered table-condensed">
                <colgroup>
                    <col :style="{width: '20%'}" />
                    <col :style="{width: '25%'}" />
                    <col :style="{width: '15%'}" />
                    <col :style="{width: '25%'}" />
                    <col :style="{width: '15%'}" />
                </colgroup>
                <tr>
                    <th></th>
                    <th class="text-center">이름</th>
                    <th class="text-center">가격</th>
                    <th class="text-center">사진</th>
                    <th class="text-center"></th>
                </tr>
                <tr v-for="(menu,index) in requestData.menus" :key="index">
                    <td class="text-center">{{menu.mid}}</td>
                    <td class="text-center">{{menu.mname}}</td>
                    <td class="text-center">{{menu.mprice}}원</td>
                    <td class="text-center"><img id = "menuimg" :src="menu.mimage"/></td>
                    <td>
                        <b-link v-b-modal.modMenu>수정</b-link><br>
                        <b-link v-b-modal.delMenu>삭제</b-link>       
                    </td>
                        <!-- 메뉴 수정하는 모달 창 -->
                        <b-modal id="modMenu" title="메뉴 수정" @ok="modhandleSubmit">
                            <form>
                                <b-form-group invalid-feedback="required">
                                    {{menu.mname}}
                                    이름<b-form-input v-model="newname" :placeholder= "menu.mname" :value="menu.mname" requried></b-form-input>
                                    <b-form-checkbox v-model="newissig" requried>메인메뉴</b-form-checkbox> 
                                    가격 <b-form-input v-model="newprice" :placeholder= "menu.mprice " required></b-form-input>
                                    <!-- 이미지 업로드 or 이미지 주소 복사(현재는 이미지 주소) -->
                                    이미지 <b-form-input v-model="newimage" :placeholder= "menu.mimage" required></b-form-input>
                                </b-form-group>
                            </form>
                        </b-modal>

                        <!-- 메뉴 삭제하기 모달 창-->
                        <b-modal id="delMenu" title="메뉴삭제" @ok= delhandleSubmit(menu.mid)><p>{{menu.mname}}을(를) 정말 삭제 하시겠습니까?</p></b-modal>
                    </tr>
            </table>
        </div>
        <div v-else>
        등록된 메뉴 정보가 없습니다.
        </div></div>
        <detail-review/>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import Review from '@/components/review/ReviewList.vue';
import constants from '../../constants.js'

//local
const BACKEND_URL = constants.URL
//AWS
// const BACKEND_URL = 'http://i3a503.p.ssafy.io'

export default {
    name:'Detail',
    props: {
        rid: Number
    },
    components: {
        'detail-review' : Review
    },
    data: () => {
        return {
            requestData: {
                rst: [],
                menus: []
            },
            newissig:false,
            newname:'',
            newprice:'',
            newimage:'',
            menuid:''
        }
    },
    mounted() {
        axios.get(BACKEND_URL + '/rst/detail', {params: {'rid':this.rid}})
        .then(response => {
            console.log(response.data)
            this.requestData.rst = response.data
        })

        axios.get(BACKEND_URL + '/menu/list', {params: {'mrid':this.rid}})
        .then(response => {
            console.log(response.data)
            this.requestData.menus = response.data
        })
    },
    methods: {
        //메뉴등록처리
        resetModal() {
            this.newissig = false,
            this.newname = '',
            this.newprice = '',
            this.newimage = ''
        },
        reghandleOk(bvModalEvt) {
        bvModalEvt.preventDefault()
        this.reghandleSubmit()
        console.log("Ok Sign")
        },
        reghandleSubmit: function() {
            axios.post(BACKEND_URL + '/menu/reg' , { 
                'mrid':this.rid, 
                'missig': this.newissig, 
                'mname':this.newname,
                'mprice':this.newprice, 
                'mimage':this.newimage
                }).then(response => {
                console.log(response.data)
                this.$nextTick(() => {
                    this.$bvModal.hide('regMenu')
                        })
                })
        },

        //메뉴수정처리
        modhandleSubmit: function() {
            console.log("mod 도달")
            axios.post(BACKEND_URL + '/menu/mod' , { 'mrid':this.rid, 'missig': this.newissig, 
                'mname':this.newname,'mprice':this.newprice, 'mimage':this.newimage}).then(response => {
                console.log(response.data)
                this.$nextTick(() => {
                    this.$bvModal.hide('modMenu')
                        })
                })
        },

        //메뉴삭제처리
        delhandleSubmit: function(mid) {
            console.log("삭제할 메뉴 번호:"+mid);
            axios.get(BACKEND_URL + '/menu/del?mid=' + mid).then(response => {
                console.log(response.data)
                this.$nextTick(() => {
                    this.$bvModal.hide('delMenu')
                    })
                })
        },
    }
}
</script>

<style>
* {
    margin: 0;
    padding: 0px;
}
.rstInfo {
    width: 100%;
    height: 240px;
    text-align:left;
    margin : 5px;
    padding: 5px;
}
.menuInfo {
    text-align: left;
    margin : 20px;
    padding: 5px;
}
.titlefont {font-size: 50px;}
.content {font-size: 25px;}
#sigimg {float:left}
#menuimg {width: 240px; height:200px;}
</style>