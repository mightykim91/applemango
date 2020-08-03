const Facebook ={
    Init(){
        window.fbAsyncInit = function() {
          FB.init({
            appId      : '3385672468159203',
            cookie     : true,                     // Enable cookies to allow the server to access the session.
            xfbml      : true,                     // Parse social plugins on this webpage.
            version    : 'v7.0'           // Use this Graph API version for this call.
          });
          window.FB.AppEvents.logPageView(); //박진환 사이트에서 카피 https://parkjihwan.tistory.com/9
        };
        (function(d, s, id) {
          var js, fjs = d.getElementsByTagName(s)[0];
          if (d.getElementById(id)) return;
          js = d.createElement(s); js.id = id;
          js.src = "//connect.facebook.net/ko_KR/sdk.js#xfbml=1&version=v2.9&appId=3385672468159203";
          fjs.parentNode.insertBefore(js, fjs);
        }(document, 'script', 'facebook-jssdk'));
      },
      Login(){

          //처음 로그인 
          window.FB.login(  // 참고:  https://developers.facebook.com/docs/reference/javascript/FB.login/v7.0 + 출처: https://parkjihwan.tistory.com/9
            response =>{
              if (response.status === 'connected') {
                
                const accessToken =response.authResponse.accessToken;
                
                window.FB.api('/me',{ fields : 'id,name,email,picture'} ,res => {
                    console.log('Successful login for: ' + res.name);
                    console.log('accessToken: ' + accessToken);
                    console.log('id: ' + res.id);
                     document.getElementById('status').innerHTML ='Thanks for logging in, ' + res.name + '!';
                  if(!res) LoginFailure();
                  const req_body={
                    facebookAccessToken: accessToken, // 로그인 하면 주는 accesstoken은 facebook내의 다른 api 요청 시 쓰임 , 
                    id: res.id,                         //클라이언트에서는 쿠키로 알아서 해결, 서버에서는 accessToken을 저장했다가 요청할때 같이 보내줘야 한다.
                    email:res.email,
                    name: res.name,
                    profileIMG: res.picture,
                    source: 'f',
                  };
                  
                // social_login(req_body);
                });
            }else{
              LoginFailure();
            }

            }, //response
          { scope: 'public_profile , email'}, // 허락받을 데이터를 정한다. public_profile과 email 로 (이름,id, 프로필사진과 이메일에 대한 동의를 구한다.)
            
          ); 
          
      
      }, //login
      Logout(){
        window.FB.getLoginStatus(response => {
          window.FB.logout(async res => {
            if(!res) return LogoutFailure();
            social_logout();
          });
        });
      }, //logout
}; //FaceBook 

export default Facebook;