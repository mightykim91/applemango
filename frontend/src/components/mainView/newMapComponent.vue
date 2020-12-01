<template>
<div>
  <div id="map">
  </div>
</div>
</template>

<script>
export default {
    data(){
        return {
            map: '',
            marker: '',
            userLat: '',
            userLng: '',
        }
    },
    created() {
        if (window.kakao && window.kakao.maps) {
                this.initMap();
        } else {
            const script = document.createElement('script');
            /* global kakao */
            script.type = 'text/javascript';
            script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${process.env.VUE_APP_KAKAO_MAP_API_KEY}&autoload=false`;
            document.head.appendChild(script);
            script.onload = () => kakao.maps.load(this.initMap);   
        }
    },
    methods: {
        initMap: function() {
            if(navigator.geolocation){
                console.log('geolocation is allowed')
                navigator.geolocation.getCurrentPosition(position => {
                    var lat = position.coords.latitude
                    var lon = position.coords.longitude
                    this.$store.commit('getLocation', [lat, lon])
                    this.userLat = lat;
                    this.userLng = lon;
                    var mapContainer = document.querySelector('#map');
                    var options = { //지도를 생성할 때 필요한 기본 옵션
                            center: new kakao.maps.LatLng(lat, lon), //지도의 중심좌표.
                            level: 3 //지도의 레벨(확대, 축소 정도)
                            };
                    this.map = new kakao.maps.Map(mapContainer, options);
                    this.marker = new kakao.maps.Marker({
                        position: this.map.getCenter()
                    });
                    this.marker.setMap(this.map);
                })
          }//end of if(navigator.geolocation)
          else{
            console.log('geolocation is not allowed')
          }//end of else(navigator.geolocation)
        },//end of initMap
    }//end of methods
}
</script>

<style scoped>

#map {
    border-radius: 30px;
    width: 800px;
    height: 500px;
}

</style>