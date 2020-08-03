<template>
  <div>
    삭제중...
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Delete",
  created() {
    const params = this.$route.params.uid;
    axios
      .post("http://localhost:8080/account/delete",{
         uid: this.$route.params.uid, 
         password: this.$route.params.password , 
         email: this.$route.params.email 
      })
      .then(({ data }) => {
        let msg = "삭제 처리시 문제가 발생했습니다.";
        if (data === "success") {
          msg = "삭제가 완료되었습니다.";
        }
        alert(msg);
        this.$router.push("/user/read");
      });
  }
};
</script>

<style></style>
