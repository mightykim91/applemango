<template> 
  <v-row justify="center" class="pa-1 m-0">
    <v-dialog v-model="dialog" persistent max-width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="black"
          text
          v-bind="attrs"
          v-on="on"
        >
          자세히보기
        </v-btn>
      </template>
      <v-card v-if="decline === false">
        <div class="d-flex justify-space-between">
            <v-card-title class="headline">등록 요청된 식당 정보</v-card-title>
            <v-icon class="ma-3" v-on:click="dialog = false">fa-times</v-icon>
        </div>
        <v-card-text class="text-left black--text text-body1">
            <p>신청자 ID: {{ request.userName.uname }}</p>
            <p>상호명: {{ request.restaurantInfo.rname }}</p>
            <p>지점명: {{ request.restaurantInfo.rbranch }}</p>
            <p>주소: {{ request.restaurantInfo.raddr }}</p>
            <p>전화번호: {{request.restaurantInfo.rphone }}</p>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue" text @click="registerRestaurant">등록하기</v-btn>
          <v-btn color="blue" text @click="decline = true">거절하기</v-btn>
        </v-card-actions>
      </v-card>

      <v-card v-if="decline === true">
          <div class="d-flex justify-space-between">
            <v-card-title class="headline">요청 거절 메세지 작성</v-card-title>
            <v-icon class="ma-3" v-on:click="dialog = false; decline = false">fa-times</v-icon>
          </div>
          <v-card-text>
              <v-textarea 
              outlined 
              placeholder="요청 거절 이유를 작성해주세요."
              v-model=declineMessage
              >
              </v-textarea>
          </v-card-text>
          <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue" text @click="declineRegistration">메세지 보내기</v-btn>
          </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import axios from 'axios'

import constants from '../../constants.js'

const BACKEND_URL = constants.URL

export default {
    name:"Restaurant",
    props:{
        request:Object
    },
    data(){
        return {
            dialog:false, //모달 트리거
            decline:false, //사용자 요청 거절 메세지 트리거
            declineMessage: '' //요청 거절 메세지 
        }
    },
    methods:{
        registerRestaurant: function(){
            axios.post(BACKEND_URL + 'register/accept', {params: {requestId: parseInt(this.request.requestId)}})
            .then(response => {
                console.log(response.data)
            })
            .catch(error => {
                console.log(error)
            })
            this.dialog = false
            this.$emit('refresh')
        },
        declineRegistration: function(){
            //거절메세지 요청 주소(axios사용)
            this.dialog = false;
            this.decline = false;

        }
    }

}
</script>

<style>

</style>