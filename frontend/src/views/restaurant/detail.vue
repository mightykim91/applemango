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
        <p>메뉴정보</p>
        <hr>
        <div v-if="requestData.menus.length > 0">
            <table class="table table-bordered table-condensed">
                <colgroup>
                    <col :style="{width: '25%'}" />
                    <col :style="{width: '25%'}" />
                    <col :style="{width: '25%'}" />
                    <col :style="{width: '25%'}" />
                </colgroup>
                <tr v-for="(menu,index) in requestData.menus" :key="index">
                    <td class="text-center">메뉴번호 : {{menu.mid}}</td>
                    <td class="text-center">메뉴이름 : {{menu.mname}}</td>
                    <td class="text-center">메뉴가격 : {{menu.mprice}}원</td>
                    <td class="text-center">메뉴사진 : {{menu.mimage}}</td>
                </tr>
            </table>
        </div>
        <div v-else>
        등록된 메뉴 정보가 없습니다.
        </div></div>
        <detail-review v-bind:restaurantId="rid"/>
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
            }
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
        regHandler() {
        }
    },
    
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
</style>