<template>
  <v-container id="main" style="border-bottom:solid 1px">
      <!--Sample Map Image-->
    
    <!-- 지도 API 
    <dmap/> -->
      <v-row>
          <v-col cols="9" id="map">
              지도
          </v-col>
          <v-col cols="3">
              <v-simple-table>
                  <thead>
                      <tr><th id="nearby-restaurant-info" class="text-center">  주변 음식점</th></tr>
                  </thead>
                  <tbody>
                      <tr v-for="rest in nearByRestaurants" v-bind:key="rest.id">
                          <td>{{ rest }}</td>
                      </tr>
                  </tbody>
              </v-simple-table>
          </v-col>
      </v-row> 
      
  </v-container>
  
</template>

<script>
import axios from 'axios';
import constants from '../../constants.js';
import {router} from '../../router/index.js';

const BACKEND_URL = constants.URL
const MAP_URL = constants.MAP
export default {
    name: 'MapComponent',
    
    data(){
        return {
            nearByRestaurants: ['음식점1', '음식점2', '음식점3'],
            addr : '서울특별시 강남구 역삼동 테헤란로 212',
            uid : this.$parent.uid,
            userInfo : [],
            rlist:[],
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
        initMap() {
            var container = document.getElementById('map');
            var options = {
              center: new kakao.maps.LatLng(37.501320, 127.039654),
              level: 5
            };
            var map = new kakao.maps.Map(container, options);
            //map.setMapTypeId(kakao.maps.MapTypeId);

            var geocoder = new kakao.maps.services.Geocoder();
            
            geocoder.addressSearch(this.addr, (result, status) => {
                // 정상적으로 검색이 완료됐으면 
                if (status == kakao.maps.services.Status.OK) {
                    var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
                    // 결과값으로 받은 위치를 마커로 표시합니다
                    var marker = new kakao.maps.Marker({
                        map: map,
                        position: coords
                    });
                    // 인포윈도우로 장소에 대한 설명을 표시합니다
                    var infowindow = new kakao.maps.InfoWindow({
                        content: '<div style="width:150px;text-align:center;padding:6px 0;">내 주소</div>'
                    });
                    infowindow.open(map, marker);
                    // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
                    map.setCenter(coords);
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
                        var marker = new kakao.maps.Marker({
                            map: map,
                            position: coords
                        });
                        // 인포윈도우로 장소에 대한 설명을 표시합니다
                        var infowindow = new kakao.maps.InfoWindow({
                            content: '<div style="width:150px;text-align:center;padding:6px 0;">'+ this.rlist[i].rname +'</div>'
                        });
                        infowindow.open(map, marker);  
                        kakao.maps.event.addListener(marker, 'click', function() {
                            // 해당 매장으로 이동
                            router.push({ name: 'storeDetail', params: { rid: this.rlist[i].rid }});
                            //<router-link :to="{ name: "storeDetail", params: { rid: 1 }}"> 홍콩반점0410<br>강남역점 </router-link>
                        });
                        //infowindow.open(map, marker);
                        // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
                        map.setCenter(coords);
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
    }
}
</script>

<style>
#map-component{
    background-color: bisque;
}
</style>