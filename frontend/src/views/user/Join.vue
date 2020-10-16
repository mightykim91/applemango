/* Join.vue */

<template>
    <div id="join">

    <v-app>
        <v-main >

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
                        label="ID"
                        name="ID"
                        prepend-icon="mdi-account"
                        type="text"
                        v-model="requestData.uid"
                        :rules="idrules"
                    ></v-text-field>

                    <v-text-field
                        id="password"
                        label="Password"
                        name="password"
                        prepend-icon="mdi-lock"
                        type="password"
                        v-model="requestData.upw"
                        :rules="passwordRules"
                    ></v-text-field>

                    <v-text-field
                        id="confirmPassword"
                        label="confirmPassword"
                        name="confirmPassword"
                        prepend-icon="mdi-lock"
                        type="password"
                        :rules="confirmPasswordRules"
                    ></v-text-field>


                    <v-text-field
                        label="Name"
                        name="Name"
                        prepend-icon="mdi-account"
                        type="text"
                        v-model="requestData.uname"
                    ></v-text-field>

                                       <v-text-field
                        label="Email"
                        name="Email"
                        prepend-icon="mdi-account"
                        type="text"
                        v-model="requestData.uemail"
                        :rules="emailRules"
                    ></v-text-field>

                    <v-text-field
                        label="Address"
                        name="Address"
                        prepend-icon="mdi-account"
                        type="text"
                        v-model="requestData.uaddr"
                    ></v-text-field>
                    <b-button id="show-btn" @click="$bvModal.show('bv-modal-example')">주소 검색 </b-button>
                    
                    <v-text-field
                        label="InstagramID"
                        name="InstagramID"
                        prepend-icon="mdi-account"
                        type="text"
                        v-model="requestData.uinstagramid"
                    ></v-text-field>

                    </v-form>
                </v-card-text>
                <v-card-actions>
                     <v-spacer></v-spacer>
                    <v-btn dark color="#FFCB3C" v-on:click="signUp">회원가입</v-btn>
                     <v-spacer></v-spacer>
                    
                </v-card-actions>
                </v-card>
            </v-col>

            <v-col
                cols="1"
                sm="12"
                md="6"
            ></v-col>
            </v-row>
 
        </v-main>
    </v-app>    
   
  


    <div>
    <!-- 주소찾기 Modal-->
    <b-modal id="bv-modal-example" hide-footer>
        <template v-slot:modal-title>
        주소 검색<code>$bvModal</code>
        </template>
        <div class="d-block text-center">
          <DaumPostcode
      :on-complete=handleAddress
        />
        </div>
        <b-button class="mt-3" block @click="$bvModal.hide('bv-modal-example')">Close Me</b-button>
    </b-modal>
    </div>



    </div>
</template>
<script>
    import axios from 'axios'
    import constants from "../../constants.js"; 
    import DaumPostcode from 'vuejs-daum-postcode'

//    import addressmodal from "../../components/user/AddressForm.vue"
    const BACKEND_URL = constants.URL

    export default  {
        name: 'Join',
        components: {
            DaumPostcode
        },
        data() {
            return {
                requestData: {
                    uid    : "",
                    upw    : "",
                    uname  : "",
                    uemail : "",
                    uphone : "",
                    uaddr  :"",
                    uinstagramid:"",
                },
                user : {
                    id : '',
                    password : ''
                },
                addressData:{
                    address : ""
                },
                
                idrules: [
                    value => !!value || 'Required.',
                    value => (value && value.length >= 6) || 'Min 6 characters',
                ],

                passwordRules: [
                    (value) => !!value || 'Please type password.',
                    (value) => (value && value.length >= 7) || 'minimum 7 characters',
                    (value) => /(?=.*\d)/.test(value) || 'Must have one number',
                    (value) => /([!@$%])/.test(value) || 'Must have one special character [!@#$%]'
                ],

                confirmPasswordRules: [
                    (value) => !!value || 'type confirm password',
                    (value) => value === this.requestData.upw || 'The password confirmation does not match.',
                ],


                emailRules: [
                    v => !!v || 'E-mail is required',
                    v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
                ],
            }
        },
        methods : {
            handleAddress : function(data) {

                console.log("data : " + data)



                let fullAddress = data.roadAddress // 카카오 map api 호환하기 위해 도로명주소로 호출
                let extraAddress = ''
                if (data.addressType === 'R') {
                    if (data.bname !== '') {
                    extraAddress += data.bname
                    }
                    if (data.buildingName !== '') {
                    extraAddress += (extraAddress !== '' ? `, ${data.buildingName}` : data.buildingName)
                    }
                    fullAddress += (extraAddress !== '' ? ` (${extraAddress})` : '')
                }


                this.requestData.uaddr = fullAddress;
                console.log("주소저장 : " + this.requestData.uaddr)
                this.$bvModal.hide('bv-modal-example')

            },

            signUp: function(){
                axios.post(`${BACKEND_URL}user/signup`, this.requestData)
                .then(response => {
                    console.log(response.data)
                    alert("회원가입 성공")
                    this.$router.push({ name: 'Login' })
                })
            },

        },
        created () {
        },
        
    }
</script>