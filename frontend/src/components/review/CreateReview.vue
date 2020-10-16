<template>
  <div>
      <h1>새로운 리뷰 작성</h1>
      <v-form class="review-creation-form">
          <v-text-field outlined v-model="requestData.title" label="제목"></v-text-field>
          <v-textarea outlined v-model="requestData.description" label="내용"></v-textarea>
          <v-select outlined :items="rating" v-model="requestData.star" label="평점"></v-select>
          <v-btn dark v-on:click="createReview">제출</v-btn> 
      </v-form>
  </div>
</template>

<script>

import axios from 'axios'
import constants from '../../constants.js'

const BACKEND_URL = constants.URL

export default {
    name: "ReviewForm",
    props: {
        rid: Number //declare props type
    },
    data(){
        return {
            requestData: {
                userId: this.$cookies.get('auth-token'),
                restaurantId: this.rid,
                title:'',
                description:'',
                star:'',
                },
            rating: [1,1.5,2,2.5,3,3.5,4,4.5,5]
        }
    },
    methods:{
        createReview: function(){
            this.requestData.userId = this.$cookies.get('auth-token')
            axios.post(`${BACKEND_URL}review/new`, this.requestData)
            .then(response => {
                console.log(response.data)
                this.$router.push({ name: 'storeDetail', params:{rid: Number(this.rid)} })
            })
        },
    }
}
</script>

<style>
.review-creation-form{
    margin: 0px 100px;
}
</style>