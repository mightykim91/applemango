<template>
  <div>
    <table class="table table-bordered w-50">
      <tr>
        <th>이메일</th>
        <td>{{ item.email }}</td>
      </tr>
      <tr>
        <th>비밀번호</th>
        <td>{{ item.password }}</td>
      </tr>
      <tr>
        <th>닉네임</th>
        <td>{{ item.uid }}</td>
      </tr>
      <tr>
        <th>가입일</th>
        <td>{{ item.createDate }}</td>
      </tr>
      <tr>
        <th>프로필 사진 업로드</th>
        <td></td>
      </tr>
      <tr>
        <th>자기소개 글</th>
        <td></td>
      </tr>
   
    </table>

    <br />
    <div class="text-center">
      <router-link :to="{name:'info'}"
        ><button class="btn btn-primary">목록</button></router-link
      >
      <router-link :to="{ name:'update' , 
                          params:
                            { uid: item.uid, 
                              password: item.password , 
                              email: item.email ,
                              createDate: item.createDate }}"
        ><button class="btn btn-primary">수정</button></router-link
      >
      <router-link :to="{ name:'delete' , 
                           params:
                            { uid: item.uid, 
                              password: item.password , 
                              email: item.email 
                              }}"
        ><button class="btn btn-primary">삭제</button></router-link
      >
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Read",
  data: function() {
    return {
      item: {}
    };
  },
  created() {
    const param = this.$route.params.id;
    
    console.dir(param);
 
    axios
      .get(`http://localhost:8080/account/read/`+ param)
      .then(({ data }) => {
        console.dir(data);
        this.item = data;
      });
  }
};
</script>

<style></style>
