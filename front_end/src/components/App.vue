<template>
  <div id="app">
   <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
}
</script>

<style scoped>
.header{
  width: 100%;
  height: 120px;
  background-color: #191919;
}

.logo {
  width: 330px;
  height: 70px;
  background-image: url("../assets/logo.png");
}

.screen1 {
  width: 100%;
  height: 800px;
  background: #191919 url("../assets/screen1.png") no-repeat;
  background-size: cover;
}

.screen1text{
  margin-top: 305px;
  margin-left: 305px;
  width: 300px;
  height: 300px;
}

.font1 {
  font-weight: bold;
  font-size: 22px;
  line-height: 26px;
  color: #E32879;
}

.font2 {
  font-style: normal;
  font-weight: 900;
  font-size: 36px;
  line-height: 42px;
  color: #ffffff;
  margin-top: 20px;
}

.font3 {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
  line-height: 26px;
  letter-spacing: 0.02em;
  margin-top: 20px;
  color: #FFFFFF;
}
</style>
