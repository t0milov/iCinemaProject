<template>
  <v-content style="font-family: Roboto">
    <div class="header">
      <div class="logo"></div>
    </div>
    <v-row :justify="'center'">
      <div class="screen1">
        <div class="screen1text">
          <div class="font1">Интерактивное кино</div>
          <div class="font2">Interactive Movie</div>
          <div class="font3">Your Choose. Your Style. Your Story.</div>
          <v-btn style="margin-top: 20px; justify-content: center">Создать свой фильм</v-btn>
        </div>
      </div>
    </v-row>
  </v-content>

</template>

<script>
export default {
  name: "App"
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
  width: 1920px;
  height: 800px;
  background-image: url("../assets/screen1.png");
  background-color: #191919;
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
