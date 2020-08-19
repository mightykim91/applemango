/* Join.vue */

<template>
    <div id="mypage">
    <main-header/>
    <div>
    <br><br>
  
        
        <!--크롤링 데이터 리스트 컨테이너-->

        <h1 style="text-align: left;">Location</h1><hr>

        <!--div id="map">지도</div-->
        <!--div v-if="requestData.rst.rlat != 0"><div id="map">지도</div></div>
        <div v-else>위치 정보가 없습니다.</div-->
 

        <v-card
            max-width="1100"
    
            class="mx-auto"
        >
            <v-toolbar
            color="orange"
            dark
            >

            <v-toolbar-title>내 즐겨찾기 목록</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn icon>
                <v-icon>mdi-magnify</v-icon>
            </v-btn>

            <v-btn icon>
                <v-icon>mdi-checkbox-marked-circle</v-icon>
            </v-btn>
            </v-toolbar>
            
            <v-list two-line>
                <template  v-for="favors in favorlist">
                    <v-list-item :key="favors.fid" v-bind:to= "{ name: 'storeDetail', params: { rid: favors.frid }}">
                        
                        <v-list-item-content>
                        <v-list-item-title v-text="favors.restaurant.rname"></v-list-item-title> 
                        <v-list-item-subtitle v-text="favors.restaurant.rbranch"></v-list-item-subtitle>
                        <v-list-item-subtitle v-text="favors.restaurant.raddr"></v-list-item-subtitle>
                        </v-list-item-content>

                         <v-list-item-action>
                            <v-list-item-action-text v-text="favors.restaurant.rphone"></v-list-item-action-text>
  
                            <v-icon
                            color="yellow"
                            >
                            fas fa-star
                            </v-icon>
                        </v-list-item-action>
                    </v-list-item>
                </template>
            </v-list>

        </v-card>

        
    </div>

    <my-review/>

    </div>
</template>


<script>
    import axios from 'axios'
    import constants from "../../constants.js"; 
    import forkimage from '../../assets/fork.png'
    import ReviewForMypage from '@/components/review/ReviewListForMypage.vue';
    const BACKEND_URL = constants.URL
    const MAP_URL = constants.MAP
    export default  {
        components: {
            'my-review' : ReviewForMypage
        },
        data() {
            return {
                user : {
                    id : '',
                    password : ''
                },
                favorlist : []
            }

        },
        methods : {
             //지도
            initMap() {
                var container = document.getElementById('map');
                var options = {
                center: new kakao.maps.LatLng(37.501320, 127.039654),
                level: 5
                };
                var map = new kakao.maps.Map(container, options);
                //map.setMapTypeId(kakao.maps.MapTypeId);

                var geocoder = new kakao.maps.services.Geocoder();
                var imageSrc = forkimage,
                    imageSize = new kakao.maps.Size(32, 32), // 마커이미지의 크기입니다
                    imageOption = {offset: new kakao.maps.Point(15, 0)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.
                        
                var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);
                geocoder.addressSearch(this.addr, (result, status) => {
                    // 정상적으로 검색이 완료됐으면 
                    if (status == kakao.maps.services.Status.OK) {
                        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
                        // 결과값으로 받은 위치를 마커로 표시합니다
                        var marker = new kakao.maps.Marker({
                            map: map,
                            position: coords,
                            image: markerImage //마커 이미지 설정
                        });
                        // 인포윈도우로 장소에 대한 설명을 표시합니다
                        var infowindow = new kakao.maps.InfoWindow({
                            content: '<div style="width:150px;text-align:center;padding:6px 0;">'+this.name+'</div>'
                        });
                        infowindow.open(map, marker);
                        // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
                        map.setCenter(coords);
                    }
                });
            },//end of initMap

        },

        mounted(){
            
            axios.get(`${BACKEND_URL}user/favors/list/${this.$cookies.get('auth-token')}`)
            .then(response => {
                this.favorlist = response.data;

                this.initMap();
                console.log(response);
            })

            axios.get(`${BACKEND_URL}user/favors/detail/${this.data.favorlist.rid}`)
            .then(response => {
                this.favorlist = response.data;
                this.initMap();
                console.log(response);
            })

            if (window.kakao && window.kakao.maps) {
                this.initMap();
            } else {
                const script = document.createElement('script');
                /* global kakao */
                script.onload = () => kakao.maps.load(this.initMap());
                //script.src = 'http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=a367e1fe90bc271522126e07ddfc6338'
                script.src = MAP_URL
                document.head.appendChild(script);
            }
        },
        created () {
            if (this.$cookies.get('auth-token')){
                //request userinfo
            }
            else {
                this.$router.push({ name: 'Login'})
            }
        }
    }
</script>
