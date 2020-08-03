
var fs =require('fs');
module.exports = {
    runtimeCompiler: true,
    devServer: {
        open: process.platform === 'darwin',
        //host: '192.168.0.10',
        //host: '70.12.247.208', // host 에 따라 변경 해줘야 한다. 
        // host: 'i3a503.p.ssafy.io', // host 에 따라 변경 해줘야 한다. 
        port: 3030, // CHANGE YOUR PORT HERE!
        hotOnly: false,
	    disableHostCheck: true,
        https: true, // SSL 인증을 하기위해 true 로 바꿔준다.
    /* https:{
   	    key: fs.readFileSync('/etc/letsencrypt/archive/i3a503.p.ssafy.io/privkey1.pem'),
            cert: fs.readFileSync('/etc/letsencrypt/archive/i3a503.p.ssafy.io/cert1.pem'),
            ca: fs.readFileSync('/etc/letsencrypt/archive/i3a503.p.ssafy.io/chain1.pem'),
    }*/

    } // 출처 : https://stackoverflow.com/questions/45807049/how-to-run-vue-js-dev-serve-with-https
}
