<template>
  <div>
      <h1>새로운 리뷰 작성</h1>
      <v-form class="review-creation-form">
          <v-text-field v-model="requestData.title" label="제목"></v-text-field>
          <v-textarea outlined v-model="requestData.description" label="내용"></v-textarea>
          <v-text-field v-model="requestData.star" label="평점"></v-text-field>
          <v-btn dark v-on:click="createReview">제출</v-btn> 
      </v-form>
  </div>
</template>

<script>

import axios from 'axios'
import constants from '../../constants.js'
//local BACKEND_URL
// const BACKEND_URL = 'http://localhost:8080'
const BACKEND_URL = constants.URL

export default {
    name: "ReviewForm",
    props: {
        rid: Number //declare props type
    },
    data(){
        return {
            requestData: {
                userId:'test',
                restaurantId: this.rid,
                title:'',
                description:'',
                star:'',
                }
        }
    },
    methods:{
        createReview: function(){
            axios.post(`${BACKEND_URL}review/new`, this.requestData)
            .then(response => {
                console.log(response.data)
                this.$router.push({ name: 'Review' })
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