<template>
    <div class="user" id="join" v-if="signUpResult === false"> 
        <div class="wrapC table">
            <div class="middle">
                <h1>회원가입</h1>
                <div class="form-wrap">
                    <div class="input-wrap">
                        <input v-model="nickName"
                            id="nickname"
                            placeholder="닉네임을 입력해주세요" type="text"/>
                    </div>

                    <div class="input-wrap">
                        <input v-model="email" 
                            id="email"
                            placeholder="이메일을 입력해주세요"
                            type="text"/>
                    </div>

                    <div class="input-wrap password-wrap">
                        <input v-model="password"
                            id="password" 
                            :type="passwordType"
                            placeholder="비밀번호를 입력해주세요"/>
                        <span :class="{active : passwordType==='text'}">
                                <i class="fas fa-eye"></i>
                            </span>
                    </div>

                    <div class="input-wrap password-wrap">
                        <input v-model="passwordConfirm" 
                            id="password-confirm"
                            :type="passwordConfirmType"
                            placeholder="비밀번호를 한번 더 입력해주세요"/>
                        <span :class="{active : passwordConfirmType==='text'}">
                                <i class="fas fa-eye"></i> 
                            </span>
                    </div>
                </div>

                <label>
                    <input v-model="isTerm" type="checkbox" id="term"/>
                    <span>약관에 동의합니다</span>
                </label>

                <span class="go-term">약관 보기</span>

                <button class="btn" @click="createhandler">
                    <span>
                        작성완료
                    </span>
                </button>
            </div>

        </div> 
        

    </div>
    <div v-else>
        <p>회원가입이 완료되었습니다.</p>
        <p>회원가입 인증 메일이 발송되었습니다. 이메일을 확인해주세요.</p>
         <button class="btn" v-on:click="mainPage">
            메인페이지로
        </button>
    </div>

</template>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
    import '../../assets/css/user.scss'
    import axios from 'axios';
 
    export default {
        components: {
        },
        created(){
            
        },
        methods: {
            createhandler(){
            axios
                .post("http://localhost:8080/account/signup", { 
                    email:this.email,
                    nickname: this.nickName,
                    password: this.password
                
                })
                .then(({ data }) => {
                    let msg = '등록 처리시 에러가 발생했습니다.'; 
                    if (data.status) {
                        msg = '등록이 완료되었습니다.';
                        this.signUpResult = true
                    }
                    
                    alert(msg);
                    
                })
                .catch(() => {
                    alert('이메일형식(abc@abc.com) 또는 비밀번호(최소 8자이상, 특수문자 포함,숫자,문자포함)를 지켜주세요.');
                });
              
        },
        mainPage(){
             this.$router.push("/");
        }
           
        },
        watch: {

        },
        data: () => {
            return {
                email: '',
                nickName: '',
                password: '',
                passwordConfirm: '',
                isTerm: false,
                passwordType:"password",
                passwordConfirmType:"password",
                signUpResult: false,
            }
        }
        

    }

</script>


