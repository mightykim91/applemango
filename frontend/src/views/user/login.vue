/* login.vue */

<template>
    <div id="login">
    
    <v-app id="inspire">
        <v-main>

            <v-row
            align="center"
            justify="center"
            >
            <v-col
                cols="1"
                sm="12"
                md="6"
            >
                <v-card class="elevation-12">
                <v-toolbar
                    color="#FFCB3C"
                    dark
                    flat
                >
                    <v-toolbar-title>Login</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                        <v-btn
                        :href="source"
                        icon
                        large
                        target="_blank"
                        v-on="on"
                        >
                        <v-icon>mdi-code-tags</v-icon>
                        </v-btn>
                    </template>
                    <span>Source</span>
                    </v-tooltip>
                </v-toolbar>
                <v-card-text>
                    <v-form>
                    <v-text-field
                        label="Login"
                        name="login"
                        prepend-icon="mdi-account"
                        type="text"
                        v-model="user.id"
                    ></v-text-field>

                    <v-text-field
                        id="password"
                        label="Password"
                        name="password"
                        prepend-icon="mdi-lock"
                        type="password"
                        v-model="user.password" @keyup.enter="login()"
                    ></v-text-field>
                    </v-form>
                </v-card-text>
                <v-card-actions>
                    <v-btn yellow @click="$router.push({ name: 'SignUp' })">Register</v-btn>
                    <v-spacer></v-spacer>
                    <v-btn color="#FFCB3C" v-on:click="login()">Login</v-btn>
                </v-card-actions>
                </v-card>
            </v-col>
            </v-row>
 
        </v-main>
    </v-app>

    <div class="login">
        <h2 class="comm__title">LOGIN</h2>

        
        
        <input type="hidden" th:name="${_csrf.parameterName}" th:value="${_csrf.token}" />

        <div class="ipt__box">
            <input type="text" class="ipt" placeholder="ID" v-model="user.id">
        </div>
        <div class="ipt__box">
            <input type="password" class="ipt" placeholder="Password" v-model="user.password" @keyup.enter="login()">
        </div>

        <v-btn dark v-on:click="login()">로그인</v-btn>

        <v-btn yellow @click="$router.push({ name: 'SignUp' })">회원가입</v-btn>

    </div>
    </div>
</template>
<script>
    import axios from 'axios'
    import constants from "../../constants.js";

    const BACKEND_URL = constants.URL


    export default  {
        name : 'login',

        data() {
            return {
                user : {
                    id : '',
                    password : ''
                },
            }
        },
        methods : {
            login : function () {
                if (this.user.id == '') {alert('아이디를 입력해주세요.');return;}
                if (this.user.password == '') {alert('비밀번호를 입력해주세요.');return;}


                axios.get(BACKEND_URL + 'user/login?' + 'uid=' + this.user.id + '&upw=' + this.user.password)
                .then(response => {
                    if (response.data.status){
                        alert("로그인 성공");
                        //alert(response.data.object);
                        this.setCookies(this.user.id);
                        //alert(ses);
                        this.$store.commit('login', response.data.object)
                        
                    }
                    this.$router.push({name:'Home'})
                })

                //alert(this.$cookies.get('auth-token'));

            },

            setCookies(token) {
                this.$cookies.set('auth-token', token)
                
            },

        },
        created () {
        }
    }
</script>
