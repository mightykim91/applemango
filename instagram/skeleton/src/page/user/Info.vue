<template>
 <div v-if="items.length">
      
      <table class="table table-bordered table-condensed">
        <colgroup>
          <col :style="{ width: '10%' }" />
          <col :style="{ width: '50%' }" />
          <col :style="{ width: '15%' }" />
          <col :style="{ width: '25%' }" />
        </colgroup>
        <tr>
          <th>닉네임 목록</th>
        </tr>
        <tr v-for="(User, index) in items" :key="index + '_items'">
          <td>
            <router-link :to="{name: 'read' , params: {id: User.uid }}">
            
            <button class="btn btn-primary" style="margin-top:10px;">
                {{User.uid}}
              </button></router-link>
          </td>
          
        </tr>
      </table>
    </div>
    <div v-else class="text-center">
      회원이 없습니다.
    </div>
</template>

<script> 
import axios from 'axios';
export default {
  name: 'Info',
  data: function() {
    return {
      items: []
    };
  },
  created() {
     axios
      .get("http://localhost:8080/account/list")
      .then(({ data }) => {
        this.items = data;
      });
  },
  watch: {
     
  },
  methods : {
     
  },
  
}
</script>

<style>

</style>
