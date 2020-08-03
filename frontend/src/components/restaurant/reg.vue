<template>
<div id="app" class="container">
    <h2 class="text-center">Regist Your Restaurant</h2>
    <div>
      <div class="form-group">
        <label for="rname">*상호명</label>
        <input type="text" class="form-control" id="rname" ref="rname" placeholder="상호명을 입력하세요" v-model="rname">
      </div>
      <div class="form-group">
        <label for="rbranch">*지점명</label>
        <input type="text" class="form-control" id="rbranch" ref="rbranch" placeholder="지점명을 입력하세요" v-model="rbranch">
      </div>
      <div class="form-group">
        <label for="ruid">*아이디</label>
        <textarea type="text" class="form-control" id="ruid" ref="ruid" placeholder="아이디를 입력하세요" v-model="ruid"></textarea>
      </div>
      <div class="form-group">
        <label for="rphone">전화번호</label>
        <textarea type="text" class="form-control" id="rphone" ref="rphone" placeholder="전화번호를 입력하세요" v-model="rphone"></textarea>
      </div>
      <div class="form-group">
        <label for="raddr">주소</label>
        <textarea type="text" class="form-control" id="raddr" ref="raddr" placeholder="주소를 입력하세요" v-model="raddr"></textarea>
      </div>
      <div class="text-right">
        <button class="btn btn-primary" @click="checkHandler">등록</button>
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import constants from "../../constants.js";
    const BACKEND_URL = constants.URL


export default {
    name:'reg',
    components: {
    },
    methods: {
        checkHandler() {
        let err = true;
        let msg = '';
        !this.rname && ((msg = '상호명을 입력해주세요'), (err = false), this.$refs.rname.focus());
        err && !this.rbranch && ((msg = '지점명을 입력해주세요'), (err = false), this.$refs.rbranch.focus());
        err && !this.ruid && ((msg = '아이디를 입력해주세요'), (err = false), this.$refs.ruid.focus());
        if (!err) alert(msg);
        else this.regHandler();
        },
        regHandler() {
            axios
                .post(BACKEND_URL + '/rst/reg', {

                                                                'rid':this.rid, 
                                                                'ruid':this.ruid, 
                                                                'rphone':this.rphone,
                                                                'raddr':this.raddr })
                .then( response => { 
                    console.log('response : ', JSON.stringify(response, null, 2)) 
                    if (response.data.status) {
                        this.regSuccess = true
                    }
                }).catch( error => { console.log('failed', error) })
        }
    },
    data: () => {
        return {
            rname:'',
            rbranch:'',
            ruid:'',
            rphone:'',
            raddr:'',
            regSuccess:false
        }
    }
}
</script>
<style>
</style>
