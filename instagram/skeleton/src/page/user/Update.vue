<template>
  <div>
    <table class="table table-bordered w-50">
      <tr>
        <th>닉네임</th>
        <td>
          <input
            type="text"
            class="form-control"
            id="uid"
            ref="uid"
            v-model="uid"
          />
        </td>
      </tr>
      <tr>
        <th>비밀번호</th>
        <td>
          <input
            type="text"
            class="form-control"
            id="password"
            ref="password"
            v-model="password"
          />
        </td>
      </tr>
      <tr>
        <th>이메일</th>
        <td>
          <input
            type="text"
            class="form-control"
            id="email"
            ref="email"
            v-model="email"
          />
        </td>
      </tr>
      <tr>
        <th>가입일</th>
        <td>
          <input
            type="text"
            class="form-control"
            id="createDate"
            ref="createDate"
            v-model="createDate"
          />
        </td>
      </tr>
      <tr>
        <th>자기소개 글</th>
        <td>
          <input
            type="text"
            class="form-control"
            id="introduce"
            ref="introduce"
            v-model="introduce"
          />
        </td>
      </tr>
      
    </table>

    <button class="btn btn-primary" @click="checkHandler">수정</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Update",
  data: function() {
    return {
      item: {},
      uid: this.$route.params.uid,
      password: this.$route.params.password,
      email: this.$route.params.email,
      createDate: this.$route.params.createDate,
      introduce: "",
  
    };
  },
  methods: {
    checkHandler() {
      let err = true;
      let msg = "";
      !this.uid &&
        ((msg = "uid를 입력해주세요"), (err = false), this.$refs.uid.focus());
      err &&
        !this.password &&
        ((msg = "password 입력해주세요"), (err = false), this.$refs.password.focus());

      if (!err) alert(msg);
      else this.updateButton();
    },
    updateButton() {
      //id 로 검색합니다
      axios
        .put("http://localhost:8080//", {
          uid: this.uid,
          password: this.password,
          email: this.email,
          createDate: this.createDate,
          introduce: this.introduce
      
        })
        .then(({ data }) => {
          let msg = "수정 처리시 문제가 발생했습니다.";
          if (data === "success") {
            msg = "수정이 완료되었습니다.";
          }
          alert(msg);
          this.$router.push("/list");
        });
    }
  },
  created() {
   
  }
};
</script>

<style></style>
