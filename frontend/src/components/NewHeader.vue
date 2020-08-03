<template>
  <v-app-bar app color="transparent">
        <v-row class="mx-auto my-auto">
            <v-col cols="3">
                <v-toolbar-title v-on:click="home" style="cursor:grab">APPLE MANGO</v-toolbar-title>
            </v-col>
            <v-col cols="2">
                <v-select solo :items="searchOptions"></v-select>
            </v-col>
            <v-col cols="4">
                <v-text-field
                single-line 
                solo placeholder="검색어를 입력해주세요"
                prepend-inner-icon="mdi-antenna"
                ></v-text-field>
            </v-col>
            <v-col cols="1">
                <v-btn>검색하기</v-btn>
            </v-col>
        </v-row>
  </v-app-bar>
</template>

<script>

export default {

    name : 'NewHeader',
    data(){
        return {
            searchOptions : ['거리순', '평점순']
        }
    },
    methods:{
        home: function(){
            this.$router.push({name: 'Home'})
        }
    }

}
</script>

<style>

</style>