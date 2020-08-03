import Vue from 'vue'
import Router from 'vue-router'

import constants from '../lib/constants'

// 유저
import Login from '../page/user/Login.vue'
import Join from '../page/user/Join.vue'
import Info from '../page/user/Info.vue'
import Read from '../page/user/Read.vue'
import Update from '../page/user/Update.vue'
import Delete from '../page/user/Delete.vue'
// 포스트
import List from '../page/post/List.vue'
 
Vue.use(Router) 
 
export default new Router({
  routes: [   
    // 로그인/가입
    { 
      path: '/user/login',
      name: constants.URL_TYPE.USER.LOGIN,
      component: Login
    },
    { 
      path: '/user/info',
      name: 'info',
      component: Info
    },
    {
      path: '/user/join',
      name: constants.URL_TYPE.USER.JOIN,
      component: Join
    },
    {
      path: '/user/read',
      name: 'read',
      component: Read
    },
    {
      path: '/user/update',
      name: 'update',
      component: Update
    },
    {
      path: '/user/delete',
      name: 'delete',
      component: Delete
    },
    
    // 포스트
    { 
      path: '/',
      name: constants.URL_TYPE.POST.MAIN,
      component: List,
    },
  ]
})
