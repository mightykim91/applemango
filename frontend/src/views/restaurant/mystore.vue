<template>
    <div class="mystore">
        <mystore-header/>
        <div class="container">
        <br><br>
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
    </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import Header from '@/components/Header.vue'
    import constants from "../../constants.js";
      const BACKEND_URL = constants.URL


    export default {
        name:'mystore',
        props: {
        ruid: String //declare props type
        },
        components: {
            'mystore-header' : Header
        },
        mounted() {

            axios.get(BACKEND_URL + '/rst/list?uid='+this.$route.params.ruid).then(({ data }) => {
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

</style>