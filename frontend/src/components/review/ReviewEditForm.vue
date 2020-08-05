<template>
  <div>
      <h1>리뷰 수정</h1>
      <v-form class="review-creation-form">
          <v-text-field v-model="review.title" label="제목"></v-text-field>
          <v-textarea outlined v-model="review.description" label="내용"></v-textarea>
          <v-text-field v-model="review.star" label="평점"></v-text-field>
          <v-btn dark v-on:click="editReview">제출</v-btn> 
      </v-form>
  </div>
</template>

<script>

import constants from '../../constants.js'

import axios from 'axios'

export default {

    name: 'ReviewEditForm',
    props: {
        rid: Number
    },
    data(){
      return {
        review: '',
      }
    },
    mounted(){
      axios.get(constants.URL + 'review/' + this.rid)
      .then(response => {
        this.review = response.data
      })
    },
    methods: {
      editReview: function(){
        axios.put(constants.URL + 'review/update/' + this.rid,{
          title: this.review.title,
          description: this.review.description,
          star: this.review.star
        })
        .then(response => {
          console.log(response)
        })
        // this.$router.push({name: 'storeDetail', params:{rid:this.review.restaurantId}})
        this.$router.go(-1)
      }
    }

}
</script>

<style>

</style>