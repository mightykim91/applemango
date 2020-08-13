<template>
<div class="detail">
    <div class="container">   
        <div class = "rstInfo">
        <p><font class="titlefont">{{requestData.rst.rname}} </font> {{requestData.rst.rbranch}} 지점</p><hr>
        <!-- 이미지 값 requestData.rst.rimg값으로 나중에 변경 -->
        
        <div v-if="requestData.rst.rimage" ><v-img id="sigimg" :src="requestData.rst.rimage"></v-img></div>
        <div v-else><v-img src="../../assets/noimage.png"  id="sigimg"></v-img></div>
        <pre><font class="content">
        {{requestData.rst.rdescription}}
        번호 {{requestData.rst.rphone}} 
        주소 {{requestData.rst.raddr}}
        </font></pre>
        </div>
        <br clear="left">
        <div class="menuInfo">
            <!-- 메뉴 등록 모달 창 -->
            <h1 style="text-align: left;">Menu <b-button v-b-modal.regMenu>등록</b-button></h1>
                 
            <b-modal id="regMenu" ref="modal" 
                title="메뉴 등록" @show="resetModal" @hidden="resetModal" @ok="reghandleOk">
                <form ref="form">
                    <b-form-group  
                        label-for="input" invalid-feedback="required">
                        이름<b-form-input v-model="newname"  required></b-form-input>
                        <b-form-checkbox v-model="newissig" requried>메인메뉴 </b-form-checkbox> 
                        가격 <b-form-input v-model="newprice" required></b-form-input>
                        <!-- 이미지 업로드 or 이미지 주소 복사(현재는 이미지 주소) -->
                        이미지 <b-form-input v-model="newimage" required></b-form-input>
                    </b-form-group>
                </form>
            </b-modal>
        <hr>
        <div v-if="requestData.menus">
            <v-container fluid>
            <v-row>
                <v-card flat v-for="(menu,index) in requestData.menus" :key="index">
                    <div v-if="menu.mimage" ><v-img :src="menu.mimage"  id="menuimg"></v-img></div>
                    <div v-else><v-img src="../../assets/noimage.png"  id="menuimg"></v-img></div>
                    <div v-if="menu.missig" ><v-img src="../../assets/star.png" style="width:5%" id = "sigimg"></v-img></div>
                    {{menu.mname}} / {{menu.mprice}}원
                    <b-link v-b-modal = "'modMenu'" @click="sendInfo(menu)">수정</b-link>&nbsp;
                    <b-link v-b-modal = "'delMenu'" @click="sendInfo(menu)">삭제</b-link>

                </v-card>
            </v-row>
        </v-container>
        </div>
        <div v-else>
        등록된 메뉴 정보가 없습니다.
        </div></div>
        <!-- 메뉴 수정하는 모달 창 -->
        <b-modal id="modMenu" title="메뉴 수정" @ok="modhandleSubmit(mid)">
            <form>
                <b-form-group invalid-feedback="required">
                    이름<b-form-input v-model="newname" />
                    <b-form-checkbox v-model="newissig" requried>메인메뉴</b-form-checkbox> 
                    가격 <b-form-input v-model="newprice"  required></b-form-input>
                    <!-- 이미지 업로드 or 이미지 주소 복사(현재는 이미지 주소) -->
                    이미지 <b-form-input v-model="newimage" required></b-form-input>
                    <b-button v-b-modal.modal-multi size="xl">인스타그램 사진 선택</b-button>
                 </b-form-group>
            </form>
        </b-modal>

        <!-- 인스타그램 사진 선택 modal -->
        <b-modal id="modal-multi" size="xl" title="Third Modal" ok-only>
            <p class="my-1">인스타그램 사진 선택</p>

            <v-container fluid>
                <v-row>
                    <v-card flat class="text-xs-center ma-3" v-for="instadata in instadatalist" v-bind:key="instadata.instaid">
                        
                        <v-img :src="instadata.iurl"  max-width="200" max-height="300" ></v-img>
                        <b-button id="select-menu-picture" v-on:click="changePicture(instadata.iurl,instadata.instaid)" >사진 선택</b-button>
                    </v-card>
                </v-row>
            </v-container>
        </b-modal>


        <!-- 메뉴 삭제하기 모달 창-->
        <b-modal id="delMenu" title="메뉴삭제" @ok= delhandleSubmit(mid)><p>{{newname}}을(를) 정말 삭제 하시겠습니까?</p></b-modal>

        <detail-review/>
        <h1 style="text-align: left;">Location</h1><hr>
        <div v-if="requestData.rst.rlat != 0"><div id="map">지도</div></div>
        <div v-else>위치 정보가 없습니다.</div>
    </div>


    
    
</div>
</template>

<script>
import axios from 'axios';
import Review from '@/components/review/ReviewList.vue';
import constants from '../../constants.js'
import forkimage from '../../assets/fork.png'
//local
const BACKEND_URL = constants.URL
const MAP_URL = constants.MAP
//AWS


export default {
    name:'Detail',
    props: {
        rid: Number
    },
    components: {
        'detail-review' : Review
    },
    data: () => {
        return {
            requestData: {
                rst: [],
                menus: []
            },
            mid:'',
            newissig:false,
            newname:'',
            newprice:'',
            newimage:'',
            menuid:'',
            name:'멀캠',
            addr:'서울특별시 강남구 역삼동 테헤란로 212',

            instagramName:'@myunggi_moon',
            message:'님 축하드립니다. 올리신 피드가 메뉴사진으로 선정되었습니다. 10%쿠폰 발행해드렸습니다. AppleMango 웹에서 확인해주세요.',
            accesstoken: 'EAAwHQEzKWuMBAM1Q8hPdQxM2ZBU4xiVZAqXCRy2ZCpDQTmMkUny4LupkHAZCHjOPp3pDenmIoDlPnGBlBtNstIC6b03kpd3eJRnph4ZAAokNDsKtrZCpwcbAVPyieOoVVue0hdBKqIanOaZCFuDifcXKzgMpgRoPh70OVMZB2cve4uvqSgbaKYpXtRWlWJN5P1OCyiphZBUC7OQZDZD',
            pageid:'',
            igUserid:'',
            selectedPostid:'',
            
            instadatalist : {
                iid : '',
                rname : '',
                rbranch : '',
                instaid : '',
                iurl : '',
                likes : '',
                idate : ''

            },
            instaflag:'', //수정버튼을 누르면 인스타의 현재 사진을 저장한다.
        }
    },
    created() {
        if(!window.FB) this.facebookInit();
    },
    mounted() {
        axios.get(BACKEND_URL + 'rst/detail', {params: {'rid':this.rid}})
        .then(response => {
            console.log(response.data)
            this.requestData.rst = response.data

            this.addr = this.requestData.rst.raddr
            this.name = this.requestData.rst.rname

            this.initMap();

        })

        axios.get(BACKEND_URL + 'menu/list', {params: {'mrid':this.rid}})
        .then(response => {
            console.log("menu list:" + response.data)
            this.requestData.menus = response.data
        })

        if (window.kakao && window.kakao.maps) {
            this.initMap();
        } else {
            const script = document.createElement('script');
            /* global kakao */
            script.onload = () => kakao.maps.load(this.initMap());
            //script.src = 'http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=a367e1fe90bc271522126e07ddfc6338'
            script.src = MAP_URL
            document.head.appendChild(script);
        }


        //기훈추가
        axios.get(BACKEND_URL + 'instagram/select/' + this.rid) // select/{irid} 레스토랑 정보 인자로 받아와서 넣어주면 댐!
            .then(response => {
                this.instadatalist = response.data;
                console.log(response);
            })
    },
    methods: {
        //메뉴등록처리
        resetModal() {
            this.newissig = false,
            this.newname = '',
            this.newprice = '',
            this.newimage = ''
        },
        reghandleOk(bvModalEvt) {
        bvModalEvt.preventDefault()
        this.reghandleSubmit()
        console.log("Ok Sign")
        },
        reghandleSubmit: function() {
            axios.post(BACKEND_URL + 'menu/reg' , { 
                'mrid':this.rid, 
                'missig': this.newissig, 
                'mname':this.newname,
                'mprice':this.newprice, 
                'mimage':this.newimage
                }).then(response => {
                console.log(response.data)
                this.$nextTick(() => {
                    this.$bvModal.hide('regMenu')
                        })
                })
        },

        //메뉴수정처리
        modhandleSubmit: function(mid) {
            console.log("mod 도달")
            axios
            .post(BACKEND_URL + 'menu/mod?mid='+ mid , { 'mrid':this.rid, 'missig': this.newissig, 
                'mname':this.newname,'mprice':this.newprice, 'mimage':this.newimage})
            .then(response => {
                console.log(response.data)
                this.$nextTick(() => {
                    this.$bvModal.hide('modMenu')
                })
                if(this.instaflag != this.newimage){
                     this.facebookLogin(); //사진이 바뀌었으면 댓글을 보낸다.
                }     

                //메뉴사진 초기화
                axios.get(BACKEND_URL + 'menu/list', {params: {'mrid':this.rid}})
                .then(response => {
                    console.log("menu list:" + response.data)
                    this.requestData.menus = response.data
                })
            })
        },
        sendInfo(menu) {
            this.mid = menu.mid,
            this.newname = menu.mname,
            this.newprice = menu.mprice,
            this.newissig = menu.missig,
            this.newimage = menu.mimage
            this.instaflag =menu.mimage; //수정하기전에 이미지를 저장한다.
            console.log("sendInfo확인"+this.newname)
        },

        //메뉴삭제처리
        delhandleSubmit: function(mid) {
            console.log("삭제할 메뉴 번호:"+mid);
            axios.get(BACKEND_URL + 'menu/del?mid=' + mid).then(response => {
                console.log(response.data)
                this.$nextTick(() => {
                    this.$bvModal.hide('delMenu')
                    })
                })
        },

        //지도
        initMap() {
            var container = document.getElementById('map');
            var options = {
              center: new kakao.maps.LatLng(37.501320, 127.039654),
              level: 5
            };
            var map = new kakao.maps.Map(container, options);
            //map.setMapTypeId(kakao.maps.MapTypeId);

            var geocoder = new kakao.maps.services.Geocoder();
            var imageSrc = forkimage,
                imageSize = new kakao.maps.Size(32, 32), // 마커이미지의 크기입니다
                imageOption = {offset: new kakao.maps.Point(15, 0)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.
                    
            var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);
            geocoder.addressSearch(this.addr, (result, status) => {
                // 정상적으로 검색이 완료됐으면 
                if (status == kakao.maps.services.Status.OK) {
                    var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
                    // 결과값으로 받은 위치를 마커로 표시합니다
                    var marker = new kakao.maps.Marker({
                        map: map,
                        position: coords,
                         image: markerImage //마커 이미지 설정
                    });
                    // 인포윈도우로 장소에 대한 설명을 표시합니다
                    var infowindow = new kakao.maps.InfoWindow({
                        content: '<div style="width:150px;text-align:center;padding:6px 0;">'+this.name+'</div>'
                    });
                    infowindow.open(map, marker);
                    // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
                    map.setCenter(coords);
                }
            });
        },//end of initMap
        
        //send comment using instagram Graph API
        facebookInit(){
            window.fbAsyncInit = function() {
            window.FB.init({
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
            
        }, //end of facebookInit() 
        facebookLogin(){
          //처음 로그인 
          window.FB.login(  // 참고:  https://developers.facebook.com/docs/reference/javascript/FB.login/v7.0 + 출처: https://parkjihwan.tistory.com/9
            response =>{
              if (response.status === 'connected') {
                
                const accessToken =response.authResponse.accessToken;
                
                window.FB.api('/me',{ fields : 'id,name,email,picture'} ,res => {
                    console.log('Successful login for: ' + res.name);
                    console.log('accessToken: ' + accessToken);
                  this.accesstoken=accessToken; //accesstoken 저장 

                });
            }
                console.dir("페이스북 로그인 완료");
            }, //response
          { scope: 'public_profile , email,instagram_basic,ads_management,pages_show_list, instagram_manage_comments,pages_read_engagement,business_management'}, // 허락받을 데이터를 정한다. public_profile과 email 로 (이름,id, 프로필사진과 이메일에 대한 동의를 구한다.) business_managementsms 는 IG media기능
            
          ); 
    
        }, //end of facebookLogin
        GetAccountsId(){ //accesstoken 를 가지고 pageid 를 가져온다.
            axios
            .get(`https://graph.facebook.com/v7.0/me/accounts?access_token=`+ this.accesstoken)
            //
            .then(({data}) => {
                this.pageid=data.data[0].id;
               
                console.dir('pageid는 '+ this.pageid+ ' 입니다.');
            
            });
          
        },//end of GetAccountsId
         GetUserId(){ //pageid 를 가지고 Userid를 가져온다.
            axios
            .get(`https://graph.facebook.com/v7.0/`+ this.pageid + `?fields=instagram_business_account&access_token=`+ this.accesstoken)
            .then(({ data }) => {
                console.dir(data);
                this.igUserid= data.instagram_business_account.id;
                console.dir("IG userid는 "+ this.igUserid+"입니다.");
                
            });
        },//end of GetUserId
        GetMediaId(){ //Userid를 가지고 MediaId를 가져온다.
            axios
            .get(`https://graph.facebook.com/v7.0/`+ this.igUserid + `/media?access_token=`+ this.accesstoken)
            .then(({ data }) => {
                
                this.selectedPostid = data.data[0].id;
                
            });
        },//end of GetMediaId
        postComment(){ // 게시글 id(media id) 를 가지고 게시글에 댓글을 답니다.
            const msg = this.instagramName + this.message;
            axios
            .post(`https://graph.facebook.com/v7.0/`+ this.selectedPostid + `/comments?access_token=`+ this.accesstoken,{message: msg })
            .then(({ data }) => {
                console.dir("댓글 :'"+ msg + " '을 적었습니다.");
                console.dir(data);
                alert("변경사항이 반영되어 "+this.instagramName +"님께 인스타그램에 댓글을 달았습니다.");
            });
        },//end of postComment

        //모달에서 메뉴 사진 선택 url 변경
        changePicture: function(url,instaid){
            this.newimage = url;
            console.dir("!!!!!!!!!!!!판도라의 상자!!!!!!!! 인스타 사진의 주인:"+ instaid)// this.instagramName=instaid; // 판도라의 상자 실제 주인에게 메시지가 갈 수 있음 
            //alert(url + " " + instaid)

            //선택 모달 창 종료
            this.$bvModal.hide('modal-multi')
            
            //    this.imageData.mimage = url;
            //    this.imageData.mid = mid;
            //    axios.post(`${BACKEND_URL}instagram/update`,this.imageData)
            //     .then(response => {
            //         console.log(this.imageData)
            //         console.log(response.data)
            //         this.comments.unshift(response.data) //새로운댓글 배열에 추가후 배열의 처음으로 이동.
                    
                    
            //   }) 
        } // end of changePictures
      },//end of methods
   
    watch: {
     accesstoken:function(){ //페이스북 로그인해서 accesstoken 이 바뀌면 
      this.GetAccountsId(); // Accountid를 가져오는 함수 실행 
    },
    pageid:function(){ //Accountid를 수행해서 pageid가 바뀌면 
       this.GetUserId(); // IG Userid를 가져오는 함수 실행 
    },
    igUserid:function(){ //GetUserId를 수행해서 igUserid가 바뀌면 
       this.GetMediaId(); // Post(게시물)들의 MediaId List를 가져오는 함수 실행 
    },
    selectedPostid:function(){ // GetPostNum을 수행해서 imgList 가 바뀌면 
      this.postComment(); //게시물의 댓글을 보내는 함수 실행 
    },
  }, //end of watch
}//end of export default
</script>

<style>
* {
    margin: 0;
    padding: 0px;
}
.rstInfo {
    width: 100%;
    height: 240px;
    text-align:left;
    margin : 5px;
    padding: 5px;
}
.menuInfo {
    text-align: left;
    margin : 20px;
    padding: 5px;
}
.titlefont {font-size: 50px;}
.content {font-size: 25px;}
#sigimg {float:left}
#menuimg {width: 240px; height:200px;}
#map {width: 100%; height:480px;}
</style>
