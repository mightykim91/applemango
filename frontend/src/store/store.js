import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

export const store = new Vuex.Store({
         plugins: [
            createPersistedState()
         ],
         state: {
           userInfo: {
             isLoggedin: false,
             isAdmin: false,
             isUser: false,
             isOwner: false,
           },
           userType: '' //유저타입 변수
         },
         mutations: {
             //CHECK USERTYPE
             login(state, userInfo){
                 const userType = userInfo.ukind;
                 if (userType === 0){
                     state.userInfo.isUser = true
                     state.userType = 'User'  
                 }
                 else if (userType === 1){
                     state.userInfo.isOwner = true
                     state.userType = 'Owner';
                 }
                 else if (userType === 3){
                     state.userInfo.isConsultant = true;
                     state.userType = 'Consultant';
                 }
                 else if(userType === 4){
                     state.userInfo.isOwner = true;
                     state.userType = 'Admin';
                 }
             },
             //로그아웃시 유저 타입 초기화 
             logout(state){
                 state.userType = ''
             }
         },
         getters: {
             getUserType: state => {
                 return state.userType;
             }
         }
       });