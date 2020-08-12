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
          <v-text-field 
          v-model="requestInfo.restaurantInfo.rphone" 
          hint="-를 제외하고 입력해주세요"
          label="전화번호" 
          :rules="[rules.required]" 
          required></v-text-field>
        </div>
        <div class="d-flex">
          <!-- <label for="raddr">주소</label> -->
          <v-text-field 
          readonly 
          id="raddr" 
          ref="raddr"
          label="식당 주소" 
          hint="주소 검색 아이콘을 클릭하여 주소를 입력하세요." 
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
          <div class="text-center p-3">
          <v-btn
            class="black--text" 
            color="#FFF176"
            v-bind="attrs"
            v-on="on"
          >
            등록 신청
          </v-btn>
          </div>
        </template>
        <v-card v-if="proceed">
          <v-card-title class="headline">식당 등록 요청이 완료되었습니다.</v-card-title>
          <v-card-text class="text-left">관리자의 심사를 거친 후 식당 등록이 완료됩니다.</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue" text @click="dialog = false; proceed=false">확인</v-btn>
          </v-card-actions>
        </v-card>
        <v-card v-else>
          <v-card-title class="headline">아래 정보로 식당 등록을 요청하시겠습니까?</v-card-title>
          <v-card-text class="text-left black--text">
            <p>상호명: {{ requestInfo.restaurantInfo.rname }}</p>
            <p>지점명: {{ requestInfo.restaurantInfo.rbranch }}</p>
            <p>전화번호: {{ requestInfo.restaurantInfo.rphone }}</p>
            <p>주소: {{ requestInfo.restaurantInfo.raddr }}</p>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn class="black--text" color="#FFF176" @click="dialog = false">아니오</v-btn>
            <v-btn class="black--text" color="#FFF176" @click="regHandler">네</v-btn>
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
    props:{ruid:String},
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
            //trigger Confirmation form
            //input value check
            Object.values(this.requestInfo.restaurantInfo).forEach(value => {
              console.log(value)
            })

            //confirmation
            this.requestInfo.userName = this.ruid
            axios.post(BACKEND_URL + 'register/restaurant', this.requestInfo)
            .then( response => { 
            console.log('response : ', JSON.stringify(response, null, 2)) 
            if (response.data == "success") {
              this.regSuccess = true
              }
            })
            .catch( error => { console.log('failed', error) })
            this.proceed = true
            
            
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
          forError: false,
          proceed: false,
          userInfo: '',
          
        }
    },
    created(){
      if (this.$cookies.get('auth-token')){
        //request userinfo
      }
      else {
        this.$router.push({ name: 'Login'})
      }
    }
}
</script>
<style>
</style>
