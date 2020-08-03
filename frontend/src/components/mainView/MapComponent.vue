<template>
  <v-container id="map" style="border-bottom:solid 1px">
      <!--Sample Map Image-->
      <v-row>
          <v-col cols="9">
            <img src="https://lh3.googleusercontent.com/proxy/13xKKMVriIztYzWu3CoUX6Z4-MeF0NYRqSPwHnuRKZpXZrRP_W0gNKCOTYj1tqP94iAWWkadIPAZn2fruAYgCJZzLvNvPDRFtqTtmQ2KBW5yYB9QwGIu5KqQ_2JXxSftvnkMlDvYozU2L6BHmJJ9Z9zeNJy70VCjCfgC2K0m7cIrQorTUBYJZPdw2QBF_fCRcn6jeGtsB-5aci-yTGhigcXzcNqN2K8n0CfDMEKKTblkz6GgdVgyhy5puWa4xkzkOLMwkIConmKkK7QwJE5-YOlgYycY_lMCqZxPOCOp3FH9-yp1w7izferri96uQO3SxIWAf0Q">
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

</style>