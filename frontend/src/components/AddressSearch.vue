<template>
  <v-dialog v-model="dialog" persistent max-width="500">
        <template v-slot:activator="{ on, attrs }">
        
          <v-icon
            id="search"
            color="black"
            dark
            v-bind="attrs"
            v-on="on"
          >
            fa-search
          </v-icon>
        
        </template>
        <v-card>
          <div class="d-flex justify-space-between">
            <v-card-title class="headline">주소 검색하기</v-card-title>
            <v-icon class="p-3" @click="dialog=false; requestParam.keyword=''; responseData=''; selectedAddress=''">fa-times</v-icon>
          </div>
          <v-card-text>
              <div class="d-flex justify-space-between text-right mt-2">
                <v-text-field
                    placeholder="도로명주소, 건물명, 또는 지번입력"
                    hint="검색어 예 : 도로명(반포대로 58), 건물명(독립기념관), 지번(삼성동 25)" 
                    v-model="requestParam.keyword"
                    @keyup.enter="getAddress"
                    >
                </v-text-field>
                <v-icon @click="getAddress">fa-search</v-icon>
              </div>
              <v-container v-if="responseData">
                  <v-card 
                  v-for="data in responseData" 
                  v-bind:key="data.id" 
                  class="text-left"
                  outlined>
                      <v-card-title class="text-subtitle-2"
                      @click="selectAddress(data.roadAddr, data)">도로명 주소: {{data.roadAddr}}</v-card-title>
                      <v-card-subtitle class="text-subtitle-2">
                          지번 주소: {{data.jibunAddr}}<br>우편번호: {{data.zipNo}}
                      </v-card-subtitle>
                      
                  </v-card>
                  <v-pagination :length="totalPage" v-model="pageNow"></v-pagination>
              </v-container>
              <v-card v-if="selectedAddress">
                  <v-card-title class="text-subtitle-2">{{ selectedAddress }}</v-card-title>
                  <v-card-text>
                    <label for="address-detail">자세한 주소</label>
                    <input 
                    type="text" 
                    class="form-control" 
                    id="address-detail" 
                    placeholder="자세한 주소를 적어주세요"
                    v-model="addressDetail"
                    >
                  </v-card-text>
                  <div class="text-right p-4">
                      <v-btn color="#FFF176"
                      @click="sendAddress"
                      >입력</v-btn>
                  </div>
              </v-card>
          </v-card-text>
          <!-- <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue" text @click="dialog=false">확인</v-btn>
          </v-card-actions> -->
        </v-card>
    </v-dialog>
</template>

<script>
import axios from 'axios'

const API_KEY = 'U01TX0FVVEgyMDIwMDgxMTAwMTEwNDExMDA0NTU='
const REQUEST_URL = 'http://www.juso.go.kr/addrlink/addrLinkApi.do'

export default {

    name:"AddressSearch",
    data(){
        return {
            dialog: false,
            requestParam:{
                confmKey: API_KEY,
                currentPage: 1, //default
                countPerPage: 15,
                keyword: '', //검색어
                resultType: 'json'
            },
            responseData:'',
            totalPage:0,
            pageNow: 1,
            selectedAddress:'',
            addressDetail:'',
        }
    },
    watch: {
        // pageNow: function(){console.log('changeDetected')}
        pageNow: function(){
            console.log('ChangeDetected')
            this.requestParam.currentPage = this.pageNow
            axios.get(REQUEST_URL, {params: this.requestParam})
            .then(response => {
                this.responseData = response.data.results.juso
            })
            
        }
    },
    methods:{
        getAddress: function(){
            axios.get(REQUEST_URL, {params: this.requestParam})
            .then(response => {
                console.log(this.responseData)
                if (response.data.results.juso) {
                    this.responseData = response.data.results.juso
                    console.log(Number(response.data.results.common.totalCount))
                    this.totalPage = parseInt(Number(response.data.results.common.totalCount) / this.requestParam.countPerPage)
                    this.totalPage += 1
                    
                }
                else {
                    this.responseData = "검색어를 입력해주시거나 주소를 확인해주세요"
                }
                this.calculatePages
            })
        },
        selectAddress: function(address, data){
            const confirmation = confirm(address + `를 주소로 선택하시겠습니까?`)
            if (confirmation) {
                this.selectedAddress = address
                this.responseData = ""
                console.log(data)
            }
        },
        sendAddress: function(){
            console.log("data sent")
            this.dialog = false
            this.requestParam.keyword=''; 
            this.responseData='';
            const fullAddress = this.selectedAddress + " " + this.addressDetail
            this.$emit("insertAddress",fullAddress)
            this.selectedAddress = ""
        }
    },
}
</script>

<style>

</style>