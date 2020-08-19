<template>

  <div id="instagramComment">
<p>
AppleMango 페이스북 계정 <br>
id: mmj2566@naver.com <br>
password : ssafy1234!</p>

<button v-on:click="facebookLogin()"><img src="../../assets/facebook.png" border="0" alt="" width="472" height="75"></button>

<p id="status"></p>

<!--
<p>게시물 목록</p>
<select class="style-chooser" v-model="selectedPostid">
 <option v-for="post in postList" v-bind:value="post.id" v-bind:key="post.id"> value는 selectedComment의 값 
    {{post.id}}
  </option>
</select>
 -->
<div v-if="isStatusOn">
<ul id="photoList">
  <li v-for="item in imgList" v-bind:key="item.media_url">
    <img v-show="item.media_url" v-bind:src="item.media_url" width="300" height="300">
    
  </li>
  
</ul>

<p><br>댓글 목록</p>
<select class="custom-select" v-model="selectedComment">
 <option v-for="comment in comments" v-bind:value="comment.id" v-bind:key="comment.id"> <!-- value는 selectedComment의 값 --> 
    {{comment.username}} : {{ comment.text }}
  </option>
</select>
<!-- <span>선택한 댓글의 id : {{ selectedComment }}</span> -->

<p>대댓글 목록</p>
<select class="custom-select" v-model="selectedReply"> 

 <option v-for="comment in replies" v-bind:value="comment.id" v-bind:key="comment.id"> <!-- value는 selectedReplies 값 --> 
    {{ comment.text }}
  </option>
</select>

<textarea class="ta" v-model="message" placeholder="선택한 댓글에 대댓글 달기"></textarea>
<br>
<input type="button" class="big-button" value="댓글 전송" @click="postComment()"/>
<input type="button" class="big-button" value="대댓글 전송" @click="postReplies()"/>
<input type="button" class="big-button" value="댓글 삭제" @click="deleteComment()"/>
<input type="button" class="big-button" value="대댓글 삭제" @click="deleteReplies()"/>
<br>
</div>
  </div>
</template>

<script src="https://use.fontawesome.com/releases/v5.2.0/js/all.js"></script> 
<script src="https://unpkg.com/axios/dist/axios.min.js"></script> 
<script> 

// import Facebook from './Facebook.js'
import axios from 'axios';
import facebookimg from '../../assets/facebook.png'
export default {
  
  name: 'App',
  components: { 
   
  },
  created() {
    if(!window.FB) this.Init();
  },

  methods : {
    Init(){
        window.fbAsyncInit = function() {
          FB.init({
            appId      : '3385672468159203',
            cookie     : true,                     // Enable cookies to allow the server to access the session.
            xfbml      : true,                     // Parse social plugins on this webpage.
            version    : 'v7.0'           // Use this Graph API version for this call.
          });
          window.FB.AppEvents.logPageView(); 
        };
        (function(d, s, id) {
          var js, fjs = d.getElementsByTagName(s)[0];
          if (d.getElementById(id)) return;
          js = d.createElement(s); js.id = id;
          js.src = "//connect.facebook.net/ko_KR/sdk.js#xfbml=1&version=v2.9&appId=3385672468159203";
          fjs.parentNode.insertBefore(js, fjs);
         
        }(document, 'script', 'facebook-jssdk'));
        
      }, //end of Init() 
        facebookLogin(){
          //처음 로그인 
          window.FB.login(  // 참고:  https://developers.facebook.com/docs/reference/javascript/FB.login/v7.0 + 출처: https://parkjihwan.tistory.com/9
            response =>{
              if (response.status === 'connected') {
                
                const accessToken =response.authResponse.accessToken;
                
                window.FB.api('/me',{ fields : 'id,name,email,picture'} ,res => {
                    console.log('Successful login for: ' + res.name);
                    console.log('accessToken: ' + accessToken);
                    // console.log('id: ' + res.id);
                   
                  if(!res) LoginFailure();
                  var req_body={
                    facebookAccessToken: accessToken, // 로그인 하면 주는 accesstoken은 facebook내의 다른 api 요청 시 쓰임 , 
                    id: res.id,                         //클라이언트에서는 쿠키로 알아서 해결, 서버에서는 accessToken을 저장했다가 요청할때 같이 보내줘야 한다.
                    email: res.email,
                    name: res.name,
                    profileIMG: res.picture,
                    source: 'f',
                  };
                  // document.getElementById('status').innerHTML ='Thanks for logging in, ' + req_body.name + '!<br>'; // + 'Your accesstoken is '+req_body.facebookAccessToken; 
                  
                  this.accesstoken=accessToken; //accesstoken 저장 
                  
                  // social_login(req_body);
                });
            }else{
              LoginFailure();
            }

            }, //response
          { scope: 'public_profile , email,instagram_basic,ads_management,pages_show_list, instagram_manage_comments,pages_read_engagement,business_management'}, // 허락받을 데이터를 정한다. public_profile과 email 로 (이름,id, 프로필사진과 이메일에 대한 동의를 구한다.) business_managementsms 는 IG media기능
            
         
          ); 
          //  "https://graph.facebook.com/ v7.0/ me / accounts? access_token = EAAwHQEzKWuMBAMZCVrXHoO8Mnu843dtfZAGh3izOrZBp647KSBKXZAy1FGLR1aIqBvCxaDCTQZA75KvyJwmq3xElYUt1PRHWC6BmIseXe0ofZBk44ygHvIQwJtjRZAKZBymtSNBTvlXbghMmnyNwULlZAGY79ikQDX8rgYQO8H2JCUz7yBQgpRGLRMdeNsnf4PqdrZBWGosyBRjQZDZD"
          
         
      }, //login
       
      GetAccountsId(){ //accesstoken 를 가지고 pageid 를 가져온다.
        axios
          .get(`https://graph.facebook.com/v7.0/me/accounts?access_token=`+ this.accesstoken)
          //
          .then(({data}) => {
            this.pageid=data.data[0].id;
            this.user=data.data[0];
            console.dir('pageid는 '+ this.pageid+ ' 입니다.');
         
          });
          
      },
      GetUserId(){ //pageid 를 가지고 Userid를 가져온다.
        axios
          .get(`https://graph.facebook.com/v7.0/`+ this.pageid + `?fields=instagram_business_account&access_token=`+ this.accesstoken)
          .then(({ data }) => {
            console.dir(data);
            this.igUserid= data.instagram_business_account.id;
            console.dir("IG userid는 "+ this.igUserid+"입니다.");
            
          });
      },
      GetMediaId(){ //Userid를 가지고 MediaId를 가져온다.
        axios
          .get(`https://graph.facebook.com/v7.0/`+ this.igUserid + `/media?access_token=`+ this.accesstoken)
          .then(({ data }) => {
            
            this.postList = data.data;
            console.dir("게시물 목록:");
            console.dir(this.postList);
            this.selectedPostid = this.postList[0].id;
          });
      },
      GetPostNum(){// MediaId를 가지고 게시물 리스트(Post들의 각 MediaId)를 가져온다
        const fields=['caption',
                    'children{media_type,media_url,thumbnail_url}',
                    'id',
                    'media_type',
                    'media_url',
                    'permalink',
                    'thumbnail_url',
                    'timestamp'].join(',')
        axios
          .get(`https://graph.facebook.com/v7.0/`+ this.selectedPostid + `?fields=${fields}&access_token=`+ this.accesstoken)
          //.get(`https://graph.facebook.com/v7.0/`+ this.postList[0].id + `?fields=id,media_type,media_url,owner,timestamp&access_token=`+ this.accesstoken) //첫번째 게시물의 데이터만 가져온다.
          .then(({ data }) => {
            console.dir("선택된 게시물 데이터");
          if(data.media_type=="IMAGE"){ //image 가 1개면 하나만 등록 
              this.imgList=data;
          }else{ //여러개면 여러개 등록
              this.imgList=data.children.data;
          }
            
     //       console.dir(this.imgList);
            
          });
      },
     GetComment(){ //게시글의 댓글을 가져옵니다. 
        const fields=['username', // 유저 이름 
                      'id',
                      'text',
                      'replies',
                      'user ',
                      'like_count',
                      'timestamp'].join(',')
        axios
            .get(`https://graph.facebook.com/v7.0/`+ this.selectedPostid + `/comments?fields=${fields}&access_token=`+ this.accesstoken)
            .then(({ data }) => {
              console.dir("댓글 리스트입니다.");
              console.dir(data);
              this.comments= data.data; // 0 번째 댓글을 타겟으로 합니다. 
            });
      },
      GetReplies(){ //댓글의 대댓글을 가져옵니다. 
        axios
            .get(`https://graph.facebook.com/v7.0/`+ this.selectedComment + `/replies?access_token=`+ this.accesstoken)
            .then(({ data }) => {
              console.dir("대댓글 리스트입니다.");
              console.dir(data);
              this.replies= data.data; // 타겟으로 합니다. 
            });
      },
      postReplies(){ // 댓글id(comment.id) 를 가지고 게시글의 댓글(comments.id)에 대댓글을 답니다.
        axios
         .post(`https://graph.facebook.com/v7.0/`+ this.selectedComment + `/replies?access_token=`+ this.accesstoken,{message: this.message })
          .then(({ data }) => {
            console.dir("대댓글 :'"+ this.message+ " '을 적었습니다.");
            console.dir(data); // 대댓글 id 
            this.GetReplies();
          });
      },
     
      postComment(){ // 게시글 id(media id) 를 가지고 게시글에 댓글을 답니다.
        axios
         .post(`https://graph.facebook.com/v7.0/`+ this.selectedPostid + `/comments?access_token=`+ this.accesstoken,{message: this.message })
          .then(({ data }) => {
            console.dir("댓글 :'"+ this.message+ " '을 적었습니다.");
            console.dir(data); // 대댓글 id 
             this.GetComment(); // 댓글이 추가되었으니 댓글 목록을 업데이트 합니다.  
          });
      },
      deleteComment(){ // 댓글id(comment.id) 를 가지고 삭제합니다.
        axios
            .delete(`https://graph.facebook.com/v7.0/`+ this.selectedComment + `?access_token=`+ this.accesstoken)
            .then(({ data }) => {
              console.dir("댓글이 삭제되었습니다.");
              this.GetComment(); // 댓글이 삭제되었으니 댓글 목록을 업데이트 합니다.  
            })
            .catch(error =>{
              alert("삭제할 댓글이 없습니다.");
            });
      },
      deleteReplies(){//대댓글 id를 가지고 삭제합니다.
        axios
            .delete(`https://graph.facebook.com/v7.0/`+ this.selectedReply + `?access_token=`+ this.accesstoken)
            .then(({ data }) => {
              console.dir("대댓글이 삭제되었습니다.");
              this.GetReplies(); // 대댓글이 삭제되었으니 대댓글 목록을 업데이트 합니다.  
            })
            .catch(error =>{
              alert("삭제할 대댓글이 없습니다.");
            });
      },
    
  },
  data: () => {
      return {
        postList:{},
        imgList:{}, //받아온 imgList
        accesstoken: 'EAAwHQEzKWuMBAM1Q8hPdQxM2ZBU4xiVZAqXCRy2ZCpDQTmMkUny4LupkHAZCHjOPp3pDenmIoDlPnGBlBtNstIC6b03kpd3eJRnph4ZAAokNDsKtrZCpwcbAVPyieOoVVue0hdBKqIanOaZCFuDifcXKzgMpgRoPh70OVMZB2cve4uvqSgbaKYpXtRWlWJN5P1OCyiphZBUC7OQZDZD',
        pageid:'',
        selectedPostid:'', //선택된 게시물의 id 
        igUserid:'', // IG User Id
        message:' 누구 님 축하드립니다. 올리신 피드가 메뉴사진으로 선정되었습니다. 10%쿠폰 발행해드렸습니다. AppleMango 웹에서 확인해주세요.', // 게시글 댓글리스트 
        comments:{}, // 게시글의 댓글 정보
        replies:{}, //댓글의 대댓글 정보
        selectedComment: '', // toggle 로 선택된 댓글 
        selectedReply:'', // toggle 로 선택된 대댓글 
        isStatusOn: false,
    }
  },
  // pageid(계정페이지id)-> Userid(사용자계정id) -> mediaid(게시물id) ->commentid(댓글id)
   watch: {
    /* trigger:function(){ //페이스북 로그인해서 accesstoken 이 바뀌면 
      this.facebookLogin(); // Accountid를 가져오는 함수 실행 
    },*/
    accesstoken:function(){ //페이스북 로그인해서 accesstoken 이 바뀌면 
      this.GetAccountsId(); // Accountid를 가져오는 함수 실행 
      this.isStatusOn=!this.isStatusOn;
    },
    pageid:function(){ //Accountid를 수행해서 pageid가 바뀌면 
       this.GetUserId(); // IG Userid를 가져오는 함수 실행 
    },
    igUserid:function(){ //GetUserId를 수행해서 igUserid가 바뀌면 
       this.GetMediaId(); // Post(게시물)들의 MediaId List를 가져오는 함수 실행 
    },
    selectedPostid:function(){ //GetMediaId를 수행해서 postList가 바뀌고 selectedPostid가 바뀌면
      this.GetPostNum(); // Post(게시물)들의 MediaId List중 0번 인덱스 게시물을 가져오는 함수 실행 
      this.GetComment(); //게시물의 댓글을 가져오는 함수 실행 
    },
    
   // selectedPostid:function(){ // GetPostNum을 수행해서 imgList 가 바뀌면 
   //   this.postComment(); //게시물의 댓글을 보내는 함수 실행 
   // },
    selectedComment:function(){ // GetComment를 수행해서 selectedComment 가 바뀌면 
      this.GetReplies(); // 선택된 댓글의 대댓글을 조회하는 함수 실행 
    },
  },
}
</script>

<style>
#instagramComment {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; 
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  
}
  .style-chooser .vs__search::placeholder,
  .style-chooser .vs__dropdown-toggle,
  .style-chooser .vs__dropdown-menu {
    background: #dfe5fb;
    color: #394066;
    text-transform: lowercase;
    font-variant: small-caps;
  }

  .style-chooser .vs__clear,
  .style-chooser .vs__open-indicator {
    fill: #394066;
  }
.big-button{
  margin : 10px;
  background-color: #FFCB3C;
  padding: 10px;
  border-radius: 12px;
  color: black;
  font-weight:300;
  font-size:15px;
}
.ta{
  width:500px;
  height: 100px;
  resize:none;
  border: solid 2px orange;
  
}
ul li {list-style-type:none; display: inline; margin-left:20px;}


</style>
