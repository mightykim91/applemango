/* Join.vue */

<template>
    <div id="join">
    <header/>
    <div class="join">
        <h2 class="comm__title">LOGIN</h2>
        <div class="ipt__box">
            <input type="text" class="ipt" placeholder="ID" v-model="user.id">
        </div>
        <div class="ipt__box">
            <input type="password" class="ipt" placeholder="Password" v-model="user.password" @keyup.enter="login()">
        </div>
        <div class="ipt__btn">
            <a href="#" class="btn btn--confirm btn--large" v-on:click="login()">LOGIN</a>
        </div>
    </div>
    </div>
</template>
<script>
    import axios from 'axios'
    import constants from "../../constants.js"; 
    const BACKEND_URL = constants.URL

    export default  {
        data() {
            return {
                user : {
                    id : '',
                    password : ''
                }
            }
        },
        methods : {
            join : function () {
                if (this.user.id == '') {alert('아이디를 입력해주세요.');return;}
                if (this.user.password == '') {alert('비밀번호를 입력해주세요.');return;}


                axios.get(BACKEND_URL + 'user/login?' + 'uid=' + this.user.id + '&upw=' + this.user.password)
                .then(response => {
                    if (response.data.status){
                        alert("로그인 성공");
                        alert(response.data.object);
                        this.setCookies(this.user.id);
                        //alert(ses);
                    }

                    this.$router.push({ path: '/'})
                })

                alert(this.$cookies.get('auth-token'));

            },

            setCookies(token) {
                this.$cookies.set('auth-token', token)
                this.isLoggedIn = true
                
            },

        },
        created () {
        }
    }
</script>
