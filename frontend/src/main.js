import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';

import { router } from './router/index.js';
import VueCookies from 'vue-cookies'
import vuetify from './plugins/vuetify';

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(VueCookies)
Vue.use(BootstrapVue)

Vue.prototype.$Axios = axios;
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  vuetify,
  router
}).$mount('#app')