<template>
  <v-container>
      <v-row>
        <!--메뉴 목록 시작-->
        <v-col cols="3" class="pa-1" style="background-color:skyblue">
          <div class="d-flex flex-column">
            <v-btn text v-on:click="currentPage=1">식당 등록 요청 관리</v-btn>
            <v-btn text v-on:click="currentPage=2">메뉴2</v-btn>
            <p class="my-2">메뉴3</p>
          </div>
        </v-col>
        <!--메뉴 목록 종료-->

        <!--메뉴 내용 시작-->
        <v-col cols="9" class="pa-1" style="background-color:gray">
          <v-container v-if="currentPage === 1">
            <restaurant-request-manager></restaurant-request-manager>
          </v-container>
        </v-col>
        <!--메뉴 내용 종료-->
      </v-row>
  </v-container>
</template>

<script>
import restaurantRequestManager from '../../components/adminPage/restaurantRequestManager.vue'

export default {
  name: 'AdminPage',
  components:{
    restaurantRequestManager
  },
  data(){
    return {
      currentPage: '', //menu to show, 'rrm':restaurant request manager
    }
  },
}
</script>

<style>

</style>