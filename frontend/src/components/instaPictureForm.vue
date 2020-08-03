<template>
  <div>
      <v-text-field 
      v-model="instaData.content"
      label="인스타데이터">

      </v-text-field>
      <button v-on:click="submit">댓글등록</button>
      
  </div>
</template>

<script>
export default {
    name:'CommentForm',
    data(){
        return {
            commentData:{
                reviewId:1,
                userId:'test', //For testing purpose, need to be revised later.
                content:'',
            }
        }
    },
    methods:{
        submit: function(){
            this.$emit("create",this.commentData)
            console.log(this.commentData)
        }
    }

}
</script>

<style>

</style>
