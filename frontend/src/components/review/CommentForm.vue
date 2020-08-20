<template>
  <div>
      <p class="text-left headline my-2">댓글작성</p>
      <v-container class="pa-0">
          <v-row>
              <v-col
              class="pr-0"
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
              class="pl-1"
              cols="2">
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

export default {
    name:'CommentForm',
    props: {
        reid:Number,
        commentCreated: Boolean
    },
    data(){
        return {
            commentData:{
                reviewId: this.reid, //need to revise this too!
                userId: '', //For testing purpose, need to be revised later.
                content:'',
            }
        }
    },
    methods:{
        submit: function(){
            this.commentData.userId = this.$cookies.get('auth-token')
            this.$emit("create",this.commentData)
        },
    },
    watch:{
        commentCreated: function(){
            console.log('댓글 등록 완료!')
            this.commentData.content = ''
        }
    }
}
</script>

<style>

</style>