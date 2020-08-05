<template>
  <v-container id="mainmap" style="border-bottom:solid 1px">
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
                      <tr><th id="nearby-restaurant-info" class="text-center">주변 음식점</th></tr>
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
import constants from '../../constants.js'
const MAP_URL = constants.MAP
export default {
    name: 'MapComponent',
    data(){
        return {
            nearByRestaurants: ['음식점1', '음식점2', '음식점3']
        }
    },
     mounted() {
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
    },
    methods: {
        initMap() {
            var container = document.getElementById('map');
            var options = {
              center: new kakao.maps.LatLng(37.501320, 127.039654),
              level: 5
            };

            var map = new kakao.maps.Map(container, options);
            map.setMapTypeId(kakao.maps.MapTypeId);
        }
    }
}
</script>

<style>
#map-component{
    background-color: bisque;
}
</style>