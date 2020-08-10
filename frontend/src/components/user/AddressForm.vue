<template>
  <div id="addressmodal" >
      <div v-show="show">
      <div id="layer-return-bg" class="carrot-layer-bg">
         <div id="layer-return-add" class="carrot-layer w-500px  h-500px">
            <div id="addr_wrap" class="addr-wrap h-400px" style="display:none">
               <img src="/resource/farm/img/btn_addr_close.png" id="btnFoldWrap" class="btn-addr-hide"  @click="HidePostcode()" alt="접기 버튼" style="float: right;">
            </div>
         </div>
      </div>
    </div>
    <DaumPostcode
      :on-complete=handleAddress
    />
    
  </div>
</template>

<script>
import DaumPostcode from 'vuejs-daum-postcode'



export default {
  name: 'addressmodal',
      props: ['show'],
  data: () => {
        return {
            addressData:{
                address : ""
            }
        }
    },
  components: {
    DaumPostcode
  },
 
  methods: {
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


      this.addressData.address = fullAddress;
      console.log("주소저장 : " + this.addressData.address)
      this.$emit("child",this.addressData);


    },

  },
  watch: {
      show: function (newVal) {
         if (newVal == true) {
            this.show = true;
            this.ShowPostcode();
         } else {
            this.show = false;
         }
        },
  },
}
</script>