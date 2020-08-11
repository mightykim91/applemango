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
            <h1 style="text-align: left;">Menu <b-button v-b-modal.regMenu>등록</b-button></h1>
                 
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
        <div v-if="requestData.menus">
            <v-container fluid>
            <v-row>
                <v-card flat v-for="(menu,index) in requestData.menus" :key="index">
                    <div v-if="menu.mimage" ><v-img :src="menu.mimage"  id="menuimg"></v-img></div>
                    <div v-else><v-img src="../../assets/noimage.png"  id="menuimg"></v-img></div>
                    <div v-if="menu.missig" ><v-img src="../../assets/star.png" style="width:5%" id = "sigimg"></v-img></div>
                    {{menu.mname}} / {{menu.mprice}}원
                    <b-link v-b-modal = "'modMenu'" @click="sendInfo(menu)">수정</b-link>&nbsp;
                    <b-link v-b-modal = "'delMenu'" @click="sendInfo(menu)">삭제</b-link>

                </v-card>
            </v-row>
        </v-container>
        </div>
        <div v-else>
        등록된 메뉴 정보가 없습니다.
        </div></div>
        <!-- 메뉴 수정하는 모달 창 -->
        <b-modal id="modMenu" title="메뉴 수정" @ok="modhandleSubmit(mid)">
            <form>
                <b-form-group invalid-feedback="required">
                    이름<b-form-input v-model="newname" />
                    <b-form-checkbox v-model="newissig" requried>메인메뉴</b-form-checkbox> 
                    가격 <b-form-input v-model="newprice"  required></b-form-input>
                    <!-- 이미지 업로드 or 이미지 주소 복사(현재는 이미지 주소) -->
                    이미지 <b-form-input v-model="newimage" required></b-form-input>
                 </b-form-group>
            </form>
        </b-modal>

        <!-- 메뉴 삭제하기 모달 창-->
        <b-modal id="delMenu" title="메뉴삭제" @ok= delhandleSubmit(mid)><p>{{newname}}을(를) 정말 삭제 하시겠습니까?</p></b-modal>

        <detail-review/>
        <h1 style="text-align: left;">Location</h1><hr>
        <div v-if="requestData.rst.rlat != 0"><div id="map">지도</div></div>
        <div v-else>위치 정보가 없습니다.</div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import Review from '@/components/review/ReviewList.vue';
import constants from '../../constants.js'

//local
const BACKEND_URL = constants.URL
const MAP_URL = constants.MAP
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
            mid:'',
            newissig:false,
            newname:'',
            newprice:'',
            newimage:'',
            menuid:'',

            name:'멀캠',
            addr:'서울특별시 강남구 역삼동 테헤란로 212'
        }
    },
    mounted() {
        axios.get(BACKEND_URL + 'rst/detail', {params: {'rid':this.rid}})
        .then(response => {
            console.log(response.data)
            this.requestData.rst = response.data

            this.addr = this.requestData.rst.raddr
            this.name = this.requestData.rst.rname

            console.log("이름 주소"+this.name+this.addr)

        })

        axios.get(BACKEND_URL + 'menu/list', {params: {'mrid':this.rid}})
        .then(response => {
            console.log("menu list:" + response.data)
            this.requestData.menus = response.data
        })

        if (window.kakao && window.kakao.maps) {
            this.initMap();
        } else {
            const script = document.createElement('script');
            /* global kakao */
            script.onload = () => kakao.maps.load(this.initMap());
            //script.src = 'http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=a367e1fe90bc271522126e07ddfc6338'
            script.src = MAP_URL
            document.head.appendChild(script);
        }
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
            axios.post(BACKEND_URL + 'menu/reg' , { 
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
        modhandleSubmit: function(mid) {
            console.log("mod 도달")
            axios.post(BACKEND_URL + 'menu/mod?mid='+ mid , { 'mrid':this.rid, 'missig': this.newissig, 
                'mname':this.newname,'mprice':this.newprice, 'mimage':this.newimage}).then(response => {
                console.log(response.data)
                this.$nextTick(() => {
                    this.$bvModal.hide('modMenu')
                        })
                })
        },
        sendInfo(menu) {
            this.mid = menu.mid,
            this.newname = menu.mname,
            this.newprice = menu.mprice,
            this.newissig = menu.missig,
            this.newimage = menu.mimage
            console.log("sendInfo확인"+this.newname)
        },

        //메뉴삭제처리
        delhandleSubmit: function(mid) {
            console.log("삭제할 메뉴 번호:"+mid);
            axios.get(BACKEND_URL + 'menu/del?mid=' + mid).then(response => {
                console.log(response.data)
                this.$nextTick(() => {
                    this.$bvModal.hide('delMenu')
                    })
                })
        },

        //지도
        initMap() {
            var container = document.getElementById('map');
            var options = {
              center: new kakao.maps.LatLng(37.501320, 127.039654),
              level: 5
            };
            var map = new kakao.maps.Map(container, options);
            //map.setMapTypeId(kakao.maps.MapTypeId);

            var geocoder = new kakao.maps.services.Geocoder();
            
            geocoder.addressSearch(this.addr, (result, status) => {
                // 정상적으로 검색이 완료됐으면 
                if (status == kakao.maps.services.Status.OK) {
                    var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
                    // 결과값으로 받은 위치를 마커로 표시합니다
                    var marker = new kakao.maps.Marker({
                        map: map,
                        position: coords
                    });
                    // 인포윈도우로 장소에 대한 설명을 표시합니다
                    var infowindow = new kakao.maps.InfoWindow({
                        content: '<div style="width:150px;text-align:center;padding:6px 0;">'+this.name+'</div>'
                    });
                    infowindow.open(map, marker);
                    // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
                    map.setCenter(coords);
                }
            });
        }//end of initMap
    }//end of methods 
}//end of export default
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
#map {width: 100%; height:480px;}
</style>
