<template>
  <div>
    <p>식당 등록 요청 관리</p>
    {{ requests }}
  </div>
</template>

<script>
import axios from 'axios'

import constans from '../../constants.js'

const BACKEND_URL = constans.URL

export default {
    name: 'restaurantRequestManager',
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
    })
    .catch(error => {
      console.log(error)
    })
  }

}
</script>

<style>

</style>