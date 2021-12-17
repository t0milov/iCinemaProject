<template>
  <div>
  <div :class="{'hidden': !isPlayer1Active}" :key="player1NodeId">
    <video controls autoplay id="player1">
      <source :src="this.baseBackendPath+'/'+player1NodeId" type="video/mp4">
    </video>
  </div>
  <div :class="{'hidden': isPlayer1Active}" :key="player2NodeId">
    <video controls autoplay id="player2">
      <source :src="this.baseBackendPath+'/'+player2NodeId" type="video/mp4">
    </video>
  </div>
  <div class="action1 btn1" id="action1">
    <v-btn @click="clickAction1" :disabled="disableBtn" v-if="showBtn && this.currentLinks[0]">
      {{this.currentLinks[0].meta.desc}}
    </v-btn>
  </div>
  <div class="action2 btn2" id="action2">
    <v-btn @click="clickAction2" :disabled="disableBtn" v-if="showBtn && this.currentLinks[1]">
      {{this.currentLinks[1].meta.desc}}
    </v-btn>
  </div>
  </div>
</template>

<script>
export default {
  name: "Player",
  data() {
    return {
      player1NodeId: null,
      player2NodeId: null,
      baseBackendPath: '/video',
      isPlayer1Active: true,
      currentNode: {},
      currentLinks: [],
      disableBtn: false,
      first: true,
      nodes: [],
      links: [],
      showBtn: false,
    }
  },
  created() {
    console.log('init')
    this.fecthData().then((res) =>{
      console.log('fectch data', res);
      this.nodes = res.data.project.nodeList;
      this.links = res.data.project.linkList;
      this.setCurrentNode();
      this.setCurrentLinks();
      setInterval(() => {this.checkDuration(), 1000});
    });
  },
  methods: {
    clickAction1() {
      this.disableBtn = true;
      this.setCurrentNode(this.getAction1NodeId());
      this.fecthNextVideo();
      this.flipActivePlayer();
    },
    clickAction2() {
      this.disableBtn = true;
      this.setCurrentNode(this.getAction2NodeId());
      this.fecthNextVideo();
      this.flipActivePlayer();
    },
    fecthNextVideo() {
      if (this.isPlayer1Active) {
        this.player2NodeId = this.currentNode.id
      } else {
        this.player1NodeId = this.currentNode.id
      }
    },
    getAction1NodeId() {
      return this.currentLinks[0].endId;
    },
    getAction2NodeId() {
      return this.currentLinks[1].endId;
    },
    flipActivePlayer() {
      setTimeout(() => {
        if (this.isPlayer1Active) this.stop(1);
        if (!this.isPlayer1Active) this.stop(2);
        this.isPlayer1Active = !this.isPlayer1Active; this.disableBtn = false;
        }, 1000);
    },
    fecthData() {
      return axios.get('/api/auth/getjson/'+this.$route.params.projectName)
    },
      setCurrentNode(nodeId) {
      console.log('Setting current node', nodeId)
        if (!nodeId) {
          this.currentNode = this.findStartNode();
          console.log('this.currentNode', this.currentNode)
          this.player1NodeId = this.currentNode.id;
        } else {
          this.currentNode = this.findNextNode(nodeId);
        }
        this.setCurrentLinks();
      },
      findStartNode() {
        console.log('check nodes for start', this.nodes);
        for (let i=0;i<this.nodes.length;i++) {
          if (!!this.nodes[i].meta.prop && this.nodes[i].meta.prop == 'start'){
            return this.nodes[i];
          }
        }
      },
      findNextNode(nextNodeId) {
        for (let i=0;i<this.nodes.length;i++) {
          console.log('check next node', this.nodes[i]);
          if (!!this.nodes[i] && this.nodes[i].id == nextNodeId) {
            return this.nodes[i];
          }
        }
      },
      setCurrentLinks() {
        let links = [];
        for (let i=0;i<this.links.length;i++) {
           if (!!this.links[i] && this.links[i].startId == this.currentNode.id) {
             links.push(this.links[i])
           }
        }
        this.currentLinks = links
        console.log('setted currentLinks', links)
      },
      stop(number) {
        if(number == 1) {
          document.getElementById('player1').pause()
        } else {
          document.getElementById('player2').pause()
        }
      },
      play(number) {
        if(number == 1) {
          document.getElementById('player1').play()
        } else {
          document.getElementById('player2').play()
        }
      },
      checkDuration() {
          let p = this.isPlayer1Active ? document.getElementById('player1') : document.getElementById('player2');
          if (p.duration - p.currentTime < 10) {
            this.showBtn = true;
          } else {
            this.showBtn = false;
        }
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

.btn1{
  position: absolute;
  bottom: 40px;
  left: 40px;
}

.btn2{
  position: absolute;
  bottom: 40px;
  right: 40px;
}
</style>
