/* Join.vue */

<template>
    <div id="join">
    <header/>
   
   
    <div class="join">
        <h2 class="comm__title">회원가입</h2>


        <div>
        <v-form class = "sign-up-form">

            <v-text-field label="ID" :rules="rulesid" hide-details="auto" v-model="requestData.uid"></v-text-field>
            <v-text-field label="Password" v-model="requestData.upw"></v-text-field>
            <v-text-field label="Name" v-model="requestData.uname"></v-text-field>
            <v-text-field label="Email" v-model="requestData.uemail"></v-text-field>
            <v-text-field label="Phone" v-model="requestData.uphone"></v-text-field>
            <b-button id="show-btn" @click="$bvModal.show('bv-modal-example')">주소 검색</b-button>
            <v-text-field label="Address" v-model="requestData.uaddr"></v-text-field>
            <!--v-text-field label="Address Detail" v-model="addressData.address"></v-text-field 주소 디테일 필요하면 사용-->
           
            <v-text-field label="InstagramID" v-model="requestData.uinstagramid"></v-text-field>

            <v-btn dark v-on:click="signUp">회원가입</v-btn>
        </v-form>    
        </div>
        
        


        <!--
                <tbody>
                    <tr>
                        <th width="180">주소</th>
                        <td colspan="3">
                            <div v-if="addressinfo.address =='' || addressinfo.address == null">
                                <input type="text" class="w-30per">
                                <p>{{ child }}</p>

                                <button class="btn-default dp-inblock ml-05" @click="showModal('post')">주소검색</button>
                            </div>
                            
                        </td>
                    </tr>
                </tbody>
        <div class="ipt__btn">
            <a href="#" class="btn btn--confirm btn--large" v-on:click="signUp">회원가입하기</a>
        </div-->
    </div>


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
                
                rulesid: [
                    value => !!value || 'Required.',
                    value => (value && value.length >= 6) || 'Min 6 characters',
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
        }
    }
</script>
