/* Join.vue */

<template>
    <div id="mypage">
    <main-header/>
 
    </div>
</template>

<script>
    import axios from 'axios'
    import constants from "../../constants.js"; 
  
  const BACKEND_URL = constants.URL

    export default  {
        data() {
            return {
                user : {
                    id : '',
                    password : ''
                }
            }
        },
        methods : {

        },
        created () {
        }
    }
</script>
