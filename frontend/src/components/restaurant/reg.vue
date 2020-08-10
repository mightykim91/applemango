<template>
  <div id="app" class="container text-left">
      <h2 class="text-center">음식점 등록 신청</h2>
      <div>
        <div class="form-group">
          <!-- <label for="rname">*상호명</label>
          <input type="text" class="form-control" id="rname" ref="rname" placeholder="상호명을 입력하세요" v-model="requestInfo.restaurantInfo.rname"> -->
          <v-text-field v-model="requestInfo.restaurantInfo.rname" label="상호명" :rules="[rules.required]" required></v-text-field>
        </div>
        <div class="form-group">
          <!-- <label for="rbranch">*지점명</label>
          <input type="text" class="form-control" id="rbranch" ref="rbranch" placeholder="지점명을 입력하세요" v-model="requestInfo.restaurantInfo.rbranch"> -->
          <v-text-field v-model="requestInfo.restaurantInfo.rbranch" label="지점명" :rules="[rules.required]" required></v-text-field>
        </div>
        <div class="form-group">
          <!-- <label for="ruid">*아이디</label>
          <textarea type="text" class="form-control" id="ruid" ref="userName" placeholder="아이디를 입력하세요" v-model="requestInfo.userName"></textarea> -->
        </div>
        <div class="form-group">
          <!-- <label for="rphone">전화번호</label>
          <textarea type="text" class="form-control" id="rphone" ref="rphone" placeholder="전화번호를 입력하세요" v-model="requestInfo.restaurantInfo.rphone"></textarea> -->
          <v-text-field v-model="requestInfo.restaurantInfo.rphone" label="전화번호" :rules="[rules.required]" required></v-text-field>
        </div>
        <div class="form-group">
          <label for="raddr">주소</label>
          <v-text-field 
          readonly 
          class="form-control" 
          id="raddr" 
          ref="raddr" 
          placeholder="주소를 입력하세요" 
          v-model="requestInfo.restaurantInfo.raddr">
          </v-text-field>
          <address-search v-on:insertAddress="addAddress"></address-search>
        </div>
        <!-- <div class="text-right">
          <button class="btn btn-primary" @click="regHandler">등록</button>
        </div> -->
      </div>
      <v-dialog v-model="dialog" persistent max-width="500">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="primary"
            dark
            v-bind="attrs"
            v-on="on"
            @click="regHandler"
          >
            등록 신청
          </v-btn>
        </template>
        <v-card>
          <v-card-title class="headline">식당 등록 요청이 완료되었습니다.</v-card-title>
          <v-card-text class="text-left">관리자의 심사를 거친 후 식당 등록이 완료됩니다.</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue" text @click="dialog = false">확인</v-btn>
          </v-card-actions>
        </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios';

import constants from "../../constants.js";
import AddressSearch from '../AddressSearch.vue'

const BACKEND_URL = constants.URL


export default {
    name:'reg',
    components: {
      AddressSearch
    },
    methods: {
        // checkHandler() {
        // let err = true;
        // let msg = '';
        // !this.rname && ((msg = '상호명을 입력해주세요'), (err = false), this.$refs.rname.focus());
        // err && !this.rbranch && ((msg = '지점명을 입력해주세요'), (err = false), this.$refs.rbranch.focus());
        // err && !this.ruid && ((msg = '아이디를 입력해주세요'), (err = false), this.$refs.userName.focus());
        // if (!err) alert(msg);
        // else this.regHandler();
        // },
        regHandler() {
            Object.values(this.requestInfo.restaurantInfo).forEach(value => {
              console.log(value)
            })
            axios
                .post(BACKEND_URL + 'register/restaurants', this.requestInfo)
                .then( response => { 
                    console.log('response : ', JSON.stringify(response, null, 2)) 
                    if (response.data == "success") {
                        this.regSuccess = true
                    }
                }).catch( error => { console.log('failed', error) })
        },
        addAddress: function(address){
          console.log("HEYHEYHEY")
          this.requestInfo.restaurantInfo.raddr = address
        }
    },
    data: () => {
        return {
          requestInfo:{
            userName: 'test', //test purpose, needs to be revised later with authentication
            restaurantInfo:{
            rname:'',
            rbranch:'',
            rphone:'',
            raddr:'',
            regSuccess:false
            }
          },
          dialog: false,
          rules: {
            required: value => !!value || '필수 입력 사항입니다.'
          },
          forError: false
          
        }
    }
}
</script>
<style>
</style>
