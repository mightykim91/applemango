import Vue from 'vue';
import VueRouter from 'vue-router';
import MainView from '@/views/MainView.vue';
import login from '@/views/user/login.vue';
import Join from '@/views/user/Join.vue';
import insta from '@/views/restaurant/Receive-insta.vue';
import Review from '@/components/review/ReviewList.vue';
import CreateReview from '@/components/review/CreateReview.vue';
import ReviewEditForm from '@/components/review/ReviewEditForm.vue';
import reg from '@/components/restaurant/reg.vue';
import mystore from '@/views/restaurant/mystore.vue';
import detail from '@/views/restaurant/detail.vue';
import AdminPage from '@/views/admin/AdminPage.vue'; //김연수 추가
import SearchResult from '@/views/search/SearchResult.vue';

import comment from '@/views/admin/instagramComment.vue';

import mypage from '@/views/user/myPage.vue';
import addressmodal from '@/components/user/AddressForm.vue'

Vue.use(VueRouter);


export const router = new VueRouter({
  mode: 'history',
  routes:[
    {
      //  path : url 주소
      path: '/',
      // component: url 주소로 갔을 때 표시될 컴포넌트
      name: 'Home',
      component: MainView,
    },
    {
        path: '/user/login',
        name: 'Login',
        component: login,
    },
    {
      path: '/user/signup',
      name: 'SignUp',
      component: Join
    },
    {
      path: '/instagram/receive',
      name: 'receiveInsta',
      component: insta
    },
    //레스토랑 등록 페이지
    {
      path: '/rst/reg/:ruid',
      component: reg,
      name: 'reg',
      props: route => ({
        ruid: String(route.params.ruid)
      })
    },
    //레스토랑 My Store (사업장 관리) 페이지
    {
      path: '/rst/mystore/:ruid',
      name: 'mystore',
      component: mystore,
      props: route => ({
        ruid: String(route.params.ruid)
      })
    },
    //레스토랑 detail 페이지
    {
      path: '/rst/detail/:rid',
      name: 'storeDetail',
      component: detail,
      props: route => ({
        rid: Number(route.params.rid)
      })
    },
  
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
    {
      path: '/review/edit/:rid',
      name: 'ReviewEditForm',
      component: ReviewEditForm,
      props: route => ({
        rid: Number(route.params.rid)
      })
    },
    {  // 인스타그램 게시물 조회, 댓글, 대댓글 기능
      path: '/instagram/comment',
      name:'comment',
      component: comment,
      
    },
    {  // 마이페이지 메인
      path: '/mypage',
      name:'mypage',
      component: mypage,
      
    },
    {
      path: '/addressmodal',
      name: 'addressmodal',
      component: addressmodal
    },
    //관리자 페이지
    //김연수 추가
    {
      path: '/admin',
      name: 'AdminPage',
      component: AdminPage
    },
    {
      path: '/search/result/:keyword',
      name: 'SearchResult',
      component: SearchResult,
    }

    
  ]
});