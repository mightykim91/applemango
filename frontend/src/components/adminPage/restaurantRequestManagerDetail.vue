<template> 
  <v-row justify="center">
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
      <v-card>
        <v-card-title class="headline">등록 요청된 식당 정보</v-card-title>
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
          <v-btn color="blue" text @click="dialog = false">거절하기</v-btn>
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
            dialog:false
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
    }

}
</script>

<style>

</style>