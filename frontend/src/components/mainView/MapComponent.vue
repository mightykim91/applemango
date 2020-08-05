<template>
  <v-container id="map" style="border-bottom:solid 1px">
      <!--Sample Map Image-->
      <v-row>
          <v-col cols="9" id="map-component">
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
export default {

    name: 'MapComponent',
    data(){
        return {
            nearByRestaurants: ['음식점1', '음식점2', '음식점3']
        }
    }

}
</script>

<style>
#map-component{
    background-color: bisque;
}
</style>