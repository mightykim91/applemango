<template>
  <div>
      <h4 class="text-left">댓글작성</h4>
      <v-container class="px-0">
          <v-row>
              <v-col
              cols="10">
                <v-textarea
                solo
                autofocus
                counter="200"
                no-resize
                height="100px"
                v-model="commentData.content">
                </v-textarea>
              </v-col>
              <v-col
              cols="2">
                  <!-- <v-btn
                  height="100px" 
                  dark v-on:click="submit">댓글 등록</v-btn> -->
                  <v-btn
                  height="100px" 
                  dark 
                  v-on:click="submit">댓글 등록</v-btn>
              </v-col>
          </v-row>
      </v-container>
  </div>
</template>

<script>


//local
// const BACKEND_URL = "http://localhost:8080/"


export default {
    name:'CommentForm',
    props: {
        reid:Number,
    },
    data(){
        return {
            commentData:{
                reviewId: this.reid, //need to revise this too!
                userId:'test', //For testing purpose, need to be revised later.
                content:'',
            }
        }
    },
    methods:{
        submit: function(){
            this.$emit("create",this.commentData)
            console.log(this.commentData)
            
        },
        // registerComment: function(){
        //     axios.post(`${BACKEND_URL}comment/new`,this.commentData)
        //     .then(response => {
        //         console.log(response.data)
        //         this.$emit("create", response.data)
        //         this.commentData.content = ''
        //         // this.comments.unshift(response.data) //새로운댓글 배열에 추가후 배열의 처음으로 이동.
        //     })
        // }
        
    }

}
</script>

<style>

</style>