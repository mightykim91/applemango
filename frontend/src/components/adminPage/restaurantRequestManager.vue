<template>
  <div>
    <h1 class="text-center mb-3">식당 등록 요청 관리</h1>
    <hr>
    <table class="table table-borderless" v-if="requests.length > 0">
        <thead class="text-center">
            <th scope="col">#</th>
            <th scope="col">식당이름</th>
            <th scope="col">요청자</th>
            <th scope="col"> </th>
        </thead>
        <tbody class="text-center">
            <tr scope="col" v-for="(request, index) in requests" v-bind:key="request.id">
                <th>{{ index + 1 }}</th>
                <td>{{ request.restaurantInfo.rname }}</td>
                <td>{{ request.userName.uname }}</td>
                <restaurantRequestManagerDetail v-bind:request="request" v-on:refresh="refresher"></restaurantRequestManagerDetail>
            </tr>
        </tbody>
    </table>
    <p v-else>들어온 요청이 없습니다.</p>
  </div>
</template>

<script>
import axios from 'axios'

import constans from '../../constants.js'

import restaurantRequestManagerDetail from '../adminPage/restaurantRequestManagerDetail.vue'

const BACKEND_URL = constans.URL

export default {
    name: 'restaurantRequestManager',
    components: {
        restaurantRequestManagerDetail
    },
    data(){
        return {
        requests: []
        }
    },
    created(){
    //식당 등록 요청 정보 불러오기
    axios.get(BACKEND_URL + 'register/all')
    .then(response => {
      this.requests = response.data
      console.log(response.data)
    })
    .catch(error => {
      console.log(error)
    })
  },
  methods: {
      refresher: function(){
          axios.get(BACKEND_URL + 'register/all')
          .then(response => {
              this.requests = response.data
          })
      }
  }

}
</script>

<style>

</style>