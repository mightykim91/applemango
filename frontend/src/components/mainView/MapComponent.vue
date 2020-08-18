<template>
   
  <v-container id="main" style="border-bottom:solid 1px">
      <!--Sample Map Image-->
    
    <!-- 지도 API 
    <dmap/> -->
     
      <v-row>
          <v-col>
        <select  class="custom-select" v-model="showingPosition">
           <option v-for="position in positionList" v-bind:key="position"> <!-- value는 selectedComment의 값 --> 
            {{position}}
        </option>

        </select>
          </v-col>
          <v-col cols="12" id="map">
              지도
          </v-col>
          
      </v-row> 
     
  </v-container>
  
</template>

<script>
import axios from 'axios';
import constants from '../../constants.js';
import {router} from '../../router/index.js';

import forkimage from '../../assets/fork.png'

const BACKEND_URL = constants.URL
const MAP_URL = constants.MAP
export default {
    name: 'MapComponent',
    
    data(){
        return {
            addr : '서울특별시 강남구 역삼동 테헤란로 212',
            uid : this.$parent.uid,
            userInfo : [],
            rlist:[],
            positionList:["내 위치","역삼역"],
            showingPosition:'역삼역',
            map:'',
            lat:'',
            lng:'',
        }
    },

     mounted() {
         this.getAllRestaurants();
         console.log(this.uid)
        axios.get(BACKEND_URL + 'user/info', {params: {'uid':this.uid}})
        .then(response => {
            this.userInfo = response.data
            this.addr = this.userInfo.uaddr
        })

    },
    methods: {
        //지도
        getAllRestaurants(){ // 모든 레스토랑 정보를 받아온다. mount 때 실행하여 watch를 이용해 rlist가바뀌면 initmap에 적용한다.
            axios
            .get(BACKEND_URL+'rst/all')
            .then(({ data }) =>{
                this.rlist =data;
                
            })
        },//end of getAllRestaurants
        moveToPage(i){
            router.push({ name: 'storeDetail', params: { rid: i }});
        },
        initMap() {
            var container = document.getElementById('map');
            this.lat =this.$store.getters.getLocation.latitude;
            this.lng =this.$store.getters.getLocation.longitude;
           
            var options = {
            //  center: new kakao.maps.LatLng(this.lat, this.lng),
              center: new kakao.maps.LatLng(37.499813584420224, 127.0347184269031),
              level: 4
            };
            this.map = new kakao.maps.Map(container, options);
            var map =this.map;
            // var map = new kakao.maps.Map(container, options);
            //map.setMapTypeId(kakao.maps.MapTypeId);

            var geocoder = new kakao.maps.services.Geocoder();
        
            geocoder.addressSearch(this.addr, (result, status) => {
                // 정상적으로 검색이 완료됐으면 
                if (status == kakao.maps.services.Status.OK) {
                    var coords = new kakao.maps.LatLng(this.lat,this.lng);
                    
                   // var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
                    // 결과값으로 받은 위치를 마커로 표시합니다
                    var marker = new kakao.maps.Marker({
                        map: map,
                        position: coords
                    });
                    // 인포윈도우로 장소에 대한 설명을 표시합니다
                    var infowindow = new kakao.maps.InfoWindow({
                        content: '<div style="width:150px;text-align:center;padding:5px 0;">내 주소</div>'
                    });
                    infowindow.open(map, marker);

                    // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
                    // 역삼역을 중심으로 초기값을 설정합니다.
                    map.setCenter(new kakao.maps.LatLng(37.499813584420224, 127.0347184269031));
                }
            });
           // "강남구 테헤란로4길 27",1,"홍콩반점0410"
           for(let i=0; i< this.rlist.length ;i++){
          // .forEach(element => {
                
                geocoder.addressSearch(this.rlist[i].raddr, (result, status) => {
                    // 정상적으로 검색이 완료됐으면 
                    if (status == kakao.maps.services.Status.OK) {
                        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
                        // 결과값으로 받은 위치를 마커로 표시합니다
                        var rid =this.rlist[i].rid;
                        //var imageSrc = "../../assets/mangoFork.png", // 마커이미지의 주소입니다    
                        var imageSrc = forkimage,
                        imageSize = new kakao.maps.Size(32, 32), // 마커이미지의 크기입니다
                        imageOption = {offset: new kakao.maps.Point(15, 0)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.
                        
                        var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);

                        var marker = new kakao.maps.Marker({
                            map: map,
                            position: coords,
                            image: markerImage //마커 이미지 설정
                        });
                        // 인포윈도우로 장소에 대한 설명을 표시합니다
                        //width:150px;text-align:center;padding:3px 0;
                        var infowindow = new kakao.maps.InfoWindow({
                            content: '<div style="font-size:1em;padding:5px;width:150px;">'+ this.rlist[i].rname +'</div>',
                            removable : true // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다

                        });
                        infowindow.open(map, marker);  
                        // <v-img src="../../assets/mangoFork.png"  id="sigimg"></v-img>
                        kakao.maps.event.addListener(marker, 'click',function(){
                            // 해당 매장으로 이동
                            router.push({ name: 'storeDetail', params: { rid: rid}})
                            //router.push({ name: 'storeDetail', params: { rid: '1' }});
                        });
                        kakao.maps.event.addListener(marker, 'mouseover', function() {
                        // 마커에 마우스오버 이벤트가 발생하면 인포윈도우를 마커위에 표시합니다
                            infowindow.open(map, marker);
                        });
                        //infowindow.open(map, marker);
                        // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
                        
                        // 현재 내 위치 기반 위치로 이동시킵니다
                        
                        // 
                        // 마지막 index 음식점 기준 위치로 이동시킵니다
                       
                    }
                });// end of geocoder.addressSearch
             // });// end of foreach
            }// end of for
            
        },//end of initMap
        kakaoMapAPIReady(){
            if (window.kakao && window.kakao.maps) {
                this.initMap();
            } else {
                const script = document.createElement('script');
                /* global kakao */
                script.onload = () => kakao.maps.load(this.initMap);
                //script.src = 'http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=a367e1fe90bc271522126e07ddfc6338'
                script.src = MAP_URL;
                document.head.appendChild(script);
                
            }
        },//end of kakaoMapAPIReady
        
      
        
    }, // methods
    watch:{
        rlist:function(){ //페이스북 로그인해서 accesstoken 이 바뀌면 
            console.dir(this.rlist);
            this.kakaoMapAPIReady();// Accountid를 가져오는 함수 실행 
        },
        showingPosition:function(){
            console.dir(this.showingPosition);
            if(this.showingPosition=="내 위치"){
                console.dir(this.lat+""+this.lng);
                this.map.setCenter(new kakao.maps.LatLng(this.lat,this.lng));
            }else if(this.showingPosition=="역삼역"){
                this.map.setCenter(new kakao.maps.LatLng(37.499813584420224, 127.0347184269031));
            }
        },
    }
}
</script>

<style>
#map-component{
    background-color: bisque;
}

</style>