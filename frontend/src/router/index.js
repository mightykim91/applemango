import Vue from 'vue';
import VueRouter from 'vue-router';
import main from '@/views/main.vue';
import login from '@/views/user/login.vue';
import test1 from '@/views/test1.vue';
import insta from '@/views/restaurant/Receive-insta.vue';

import Review from '@/components/review/ReviewList.vue';
import CreateReview from '@/components/review/CreateReview.vue';
import reg from '@/components/restaurant/reg.vue';
import mystore from '@/views/restaurant/mystore.vue';
import detail from '@/views/restaurant/detail.vue';

import comment from '@/views/admin/instagramComment.vue';

Vue.use(VueRouter);


export const router = new VueRouter({
  mode: 'history',
  routes:[
    {
      //  path : url 주소
      path: '/',
      // component: url 주소로 갔을 때 표시될 컴포넌트
      component: main,
    },
    {
        path: '/user/login',
        component: login,
    },
    {
      path: '/instagram/receive',
      name: 'receiveInsta',
      component: insta

  },
    {
      path: '/test1',
      component: test1,
    },
    {
      path: '/rst/reg',
      component: reg,
    },
    {
      path: '/rst/mystore/:ruid?',
      name: 'mystore',
      component: mystore
    },
    {
      path: '/rst/mystore/:ruid',
      name: 'mystore',
      component: mystore,
      props: route => ({
        ruid: String(route.params.ruid)
      })
    },
    {
      path: '/rst/detail/:rid',
      name: 'storeDetail',
      component: detail,
      props: route => ({
        rid: Number(route.params.rid)
      })
    },
    // {
    //   path: '/rst/detail/:rid?',
    //   name:'detail',
    //   component: detail
      
    // },
    //리뷰리스트 출력
    {
      path: '/review',
      name: 'Review',
      component: Review
    },
    //새로운 리뷰 작성(레스토랑별 id 필요)
    {
      path: '/review/:rid',
      name: 'ReviewForm',
      component: CreateReview,
      props: route => ({
        rid: String(route.params.rid)
      })
    },
    {  // 인스타그램 게시물 조회, 댓글, 대댓글 기능
      path: '/instagram/comment',
      name:'comment',
      component: comment,
      
    }
    
  ]
});
