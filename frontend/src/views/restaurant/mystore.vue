<template>
        <div class="container">
        
        <router-link :to="{ name: 'receiveInsta' }">인스타그램 사진 링크</router-link><hr>
        <p>{{this.$route.params.ruid}}님의 가게 정보</p>
        
        <table class="table table-bordered table-condensed">
                <colgroup>
                    <col :style="{width: '30%'}" />
                    <col :style="{width: '50%'}" />
                    <col :style="{width: '20%'}" />
                </colgroup>
                <tr  v-for="(rst, index) in rsts" :key="index + '_rsts'">
                    <td class="text-center"><router-link :to="{ name: 'storeDetail', params: { rid: rst.rid }}"> {{rst.rname}} </router-link></td>
                    <td><pre>
                        이름: {{rst.rname}} ({{rst.rbranch}})
                        전화번호 : {{rst.rphone}}
                        주소: {{rst.raddr}}
                        설명: {{rst.rdescription}}
                    </pre></td>
                    <td>
                        <b-button variant="warning">수정</b-button>
                        <b-button variant="danger">삭제</b-button>
                    </td>
                </tr>
        </table>
    
       
        <br><br>
         <div class="left">
            <ul>
            <b-nav-item>즐겨찾기</b-nav-item>
            <b-nav-item>리뷰관리</b-nav-item>
            <b-nav-item>회원정보</b-nav-item>
            <b-nav-item>Instagram</b-nav-item>
            </ul>
         </div>

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
        },
        data: () => {
            return {
                rid:'',
                rsts: []
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