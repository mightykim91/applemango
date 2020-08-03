<template>
    <div id="header" v-if="isHeader">
        <h1>
            <router-link v-bind:to="{name:constants.URL_TYPE.POST.MAIN}">
                SS_log
            </router-link>
        </h1>
        <MyModal @close="closeModal" v-if="modal">
                    <!-- default 슬롯 콘텐츠 -->
        <div class="user" id="login">

        <div class="wrapC table">
            <div class="middle">
                <h1>SS_log</h1>
                <div class="input-wrap">
                    <input v-model="email"
                        id="email" 
                        placeholder="이메일을 입력해주세요"
                        type="text"/>
                </div>
                <div class="input-wrap">
                    <input v-model="password" type="password"
                        id="password"
                        placeholder="영문, 숫자 혼용 8자 이상"/>
                </div>
                <button class="btn btn--back btn--login" @click="doSend">
                    로그인 하기
                </button>
                <div class="add-option">
                    <div class="wrap">
                        <p>아직 회원이 아니신가요?</p>
                        <router-link v-bind:to="{name:constants.URL_TYPE.USER.JOIN}" class="btn--text">
                            회원가입
                        </router-link>
                    </div>

                </div>
            </div>
        </div>
    </div>
                    
                    </MyModal>
        <div class="right">
          <div>
                <button @click="openModal">로그인</button>
                
           </div>
         
            <router-link v-bind:to="{name:constants.URL_TYPE.USER.INFO}" class="login-btn">
                회원목록
            </router-link>
            
           
       
            
        </div>  
        
    </div>
</template>   

<script> 
    import constants from '../../lib/constants'
    import MyModal from './MyModal.vue'
    export default {
        name: 'Header',
        components: { 
            MyModal 
        },
        props: ['isHeader'],
        computed:{
        },
        watch: {
        },
        created() {
        },
        methods : {
            openModal() {
                this.modal = true
                },
            closeModal() {
                this.modal = false
                },
            doSend() {
                if (this.email.length > 0 && this.password.length > 0) {
                    alert("이메일은" + this.email + "입니다.")
                    this.closeModal()
                } else{
                    alert('이메일,비밀번호를 입력해주세요.')
                }
                
            }
        },
        data: function() {
           return {
               constants,
               keyword : "",
               modal: false,
               message: '',
           }
        },

    }
</script>
