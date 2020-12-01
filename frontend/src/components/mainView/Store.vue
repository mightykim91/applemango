<template>
  <div class="store-container">
      <div class="store-info">
          <div class="store-photo">{{ content }}</div>
          <div class="store-detail">
              <div class="description">
                  <h4>홍콩반점</h4>
                  <p style="color: #ff5856">영업시간: 09:00 ~ 23:00</p>
                  <p>주소: 서울특별시 강남구 역삼동</p>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
export default {
    props: {
        content: Number
    }
}
</script>

<style scoped>

@font-face {
    font-family: 'BinggraeMelona';
    src: url('../../assets/fonts/BinggraeMelona.ttf') format('truetype');
}

@font-face {
    font-family: 'BinggraeMelona-Bold';
    src: url('../../assets/fonts/BinggraeMelona-Bold.ttf') format('truetype');
}

.store-container {
    border-radius: 30px;
    background-color: #ffaa2b;
    opacity: 100%;
}

.store-container:hover {
    opacity: 80%;
    transition-duration: 0.3s;
}

.store-info {
    display: flex;
    height: 100%;
    justify-content: center;
}

.store-photo {
    background-color: black;
    width: 40%;
    height: 90%;
    margin-right: 10px;
    margin-left: 10px;
    margin-top: auto;
    margin-bottom: auto;
    border-radius: 30px;
}

.store-detail {
    background-color: white;
    width: 60%;
    height: 90%;
    margin-top: auto;
    margin-bottom: auto;
    margin-right: 10px;
    border-radius: 30px;
}

.description {
    width: 80%;
    height: 80%;
    text-align: left;
    margin-left: 10%;
    margin-right: 10%;
    margin-top: 9%;
}

.description p {
    font-family: 'BinggraeMelona';
    margin-bottom: 0;
}

.description h4 {
    font-family: 'BinggraeMelona-Bold';
    margin-bottom: 2px;
}
</style>