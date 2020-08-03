module.exports = {
    runtimeCompiler: true,
    devServer: {
        open: process.platform === 'darwin',
        host: '70.12.247.208', // host 에 따라 변경 해줘야 한다. 
        port: 8080, // CHANGE YOUR PORT HERE!
        https: true, // SSL 인증을 하기위해 true 로 바꿔준다.
        hotOnly: false,
      } // 출처 : https://stackoverflow.com/questions/45807049/how-to-run-vue-js-dev-serve-with-https
}