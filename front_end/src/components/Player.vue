<template>
  <div>
  <div :class="{'hidden': !isPlayer1Active}" :key="player1NodeId">
    <video muted="muted" autoplay>
      <source :src="this.baseBackendPath+'/'+player1NodeId" type="video/mp4">
    </video>
  </div>
  <div :class="{'hidden': isPlayer1Active}" :key="player2NodeId">
    <video controls muted="muted">
      <source :src="this.baseBackendPath+'/'+player2NodeId" type="video/mp4">
    </video>
  </div>
<!--  <div :class="{'hidden': !isPlayer3Active}" :key="player3NodeId">-->
<!--    <video controls muted="muted">-->
<!--      <source :src="this.baseBackendPath+'/'+player3NodeId" type="video/mp4">-->
<!--    </video>-->
<!--  </div>-->
  <div class="action1" id="action1">
    <v-btn @click="clickAction1">
      Действие 1
    </v-btn>
  </div>
  <div class="action2" id="action2">
    <v-btn @click="clickAction2">
      Действие 2
    </v-btn>
  </div>
  </div>
</template>

<script>
export default {
  name: "Player",
  data() {
    return {
      player1NodeId: '1',
      player2NodeId: null,
      // player3NodeId: '3',
      baseBackendPath: 'http://localhost:8000/video',
      isPlayer1Active: true,
      // isPlayer2Active: false,
      // isPlayer3Active: false,
      currentNodeId: '1'
    }
  },
  created() {

  },
  methods: {
    clickAction1() {
      this.fecthNextVideo(this.getAction1NodeId());
      this.flipActivePlayer();
    },
    clickAction2() {
      this.fecthNextVideo(this.getAction2NodeId());
      his.flipActivePlayer();
    },
    fecthNextVideo(nextNodeId) {
      if (this.isPlayer1Active) {
        this.player2NodeId = nextNodeId
      } else {
        this.player1NodeId = nextNodeId
      }
    },
    getAction1NodeId() {
      return '2';
    },
    getAction2NodeId() {
      return '3';
    },
    flipActivePlayer() {
      setTimeout(() => {this.isPlayer1Active = !this.isPlayer1Active}, 2000);
    }
  }
}
</script>

<style scoped>
video{
  height: 100%;
  width: 100%;
}

.hidden {
  display: none;
}
</style>
