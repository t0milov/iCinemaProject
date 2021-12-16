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
  <div class="action1" id="action1">
    <v-btn @click="clickAction1" :disabled="disableBtn" v-if="showBtn && this.currentLinks[0]">
      {{this.currentLinks[0].meta.desc}}
    </v-btn>
  </div>
  <div class="action2" id="action2">
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
      player1NodeId: '1',
      player2NodeId: null,
      baseBackendPath: 'http://localhost:8000/video',
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
    this.nodes = this.fetchNodes();
    this.links = this.fetchLinks();
    this.setCurrentNode();
    this.setCurrentLinks();
    setInterval(() => {this.checkDuration(), 1000})
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
    fetchNodes() {
      return [
        {
          id: "nodeS3WgFnzCI15X58Qw",
          width: 160,
          height: 80,
          coordinate: [
            -1581,
            -1590
          ],
          meta: {
            prop: "start",
            name: "В помещении"
          }
        },
        {
          id: "nodejvPU5O9KYE3wFByZ",
          width: 160,
          height: 80,
          coordinate: [
            -1323,
            -1590
          ],
          meta: {
            prop: "cc",
            name: "Комната №1"
          }
        },
        {
          id: "nodeIk0EWO3ZENsz76Je",
          width: 160,
          height: 50,
          coordinate: [
            -1095,
            -1451
          ],
          meta: {
            prop: "end",
            name: "Смэрть от испуга"
          }
        },
        {
          id: "nodeefb0cDJpWbzZb5SQ",
          width: 160,
          height: 80,
          coordinate: [
            -1095,
            -1686
          ],
          meta: {
            prop: "cc",
            name: "Утащили сумку"
          }
        },
        {
          id: "nodeSihHPDIVzfgTgnvP",
          width: 160,
          height: 50,
          coordinate: [
            -886,
            -1538
          ],
          meta: {
            prop: "end",
            name: "Смэрть от зомби"
          }
        },
        {
          id: "nodeFqKf8bjHZTS9zniA",
          width: 160,
          height: 80,
          coordinate: [
            -886,
            -1957
          ],
          meta: {
            prop: "cc",
            name: "Новая комната"
          }
        },
        {
          id: "nodeMFLGTfKpblBH4N3e",
          width: 160,
          height: 80,
          coordinate: [
            -605,
            -1957
          ],
          meta: {
            prop: "cc",
            name: "Сцена в дыре"
          }
        },
        {
          id: "nodePgpq8ji0qlOVAPyq",
          width: 160,
          height: 50,
          coordinate: [
            -740,
            -1824
          ],
          meta: {
            prop: "end",
            name: "Смэрть"
          }
        },
        {
          id: "nodefbgwxUy6XoUScmZK",
          width: 160,
          height: 80,
          coordinate: [
            -616,
            -1731
          ],
          meta: {
            prop: "cc",
            name: "Сцена у колыбели"
          }
        },
        {
          id: "nodeBiwjB9izKq8RkLFE",
          width: 160,
          height: 80,
          coordinate: [
            -673,
            -1553
          ],
          meta: {
            prop: "cc",
            name: "Нашел зеркало"
          }
        },
        {
          id: "nodey4FJL3ShWY3Z2wCQ",
          width: 160,
          height: 80,
          coordinate: [
            -412,
            -1553
          ],
          meta: {
            prop: "cc",
            name: "Подсказка"
          }
        },
        {
          id: "nodeYN5yw6knNlgl1eee",
          width: 160,
          height: 80,
          coordinate: [
            -822,
            -1383
          ],
          meta: {
            prop: "cc",
            name: "Осмотреть диван"
          }
        },
        {
          id: "nodeuZ2DF6Mbml2q6O6C",
          width: 160,
          height: 80,
          coordinate: [
            -974,
            -1225
          ],
          meta: {
            prop: "cc",
            name: "Сцена"
          }
        },
        {
          id: "nodedgHiDUusyGgfVAqS",
          width: 160,
          height: 50,
          coordinate: [
            -640,
            -1210
          ],
          meta: {
            prop: "end",
            name: "Спасение мальчика"
          }
        }
      ]
    },
    fetchLinks() {
      return [
        {
          id: "linkZg5ux7UIj8Qiil4D",
          startId: "nodejvPU5O9KYE3wFByZ",
          endId: "nodeIk0EWO3ZENsz76Je",
          startAt: [
            160,
            40
          ],
          endAt: [
            0,
            25
          ],
          meta: {
            desc: "Справа"
          }
        },
        {
          id: "linkATQuGdhB2XOp84rc",
          startId: "nodeS3WgFnzCI15X58Qw",
          endId: "nodejvPU5O9KYE3wFByZ",
          startAt: [
            160,
            40
          ],
          endAt: [
            0,
            40
          ],
          meta: {
            desc: "Дверь №1"
          }
        },
        {
          id: "linkd6NhdbOQ9dI4TfPZ",
          startId: "nodeFqKf8bjHZTS9zniA",
          endId: "nodeMFLGTfKpblBH4N3e",
          startAt: [
            160,
            40
          ],
          endAt: [
            0,
            40
          ],
          meta: {
            desc: "Залесть в дыру"
          }
        },
        {
          id: "linkTBbbc69I0zgh9ZIQ",
          startId: "nodeMFLGTfKpblBH4N3e",
          endId: "nodePgpq8ji0qlOVAPyq",
          startAt: [
            160,
            40
          ],
          endAt: [
            0,
            25
          ],
          meta: {
            desc: "Камин"
          }
        },
        {
          id: "linkdXzwyz3jZbDhtxa2",
          startId: "nodeMFLGTfKpblBH4N3e",
          endId: "nodefbgwxUy6XoUScmZK",
          startAt: [
            160,
            40
          ],
          endAt: [
            80,
            0
          ],
          meta: {
            desc: "Колыбель"
          }
        },
        {
          id: "linkRM5GHgFRqwCsT8wj",
          startId: "nodefbgwxUy6XoUScmZK",
          endId: "nodeBiwjB9izKq8RkLFE",
          startAt: [
            160,
            40
          ],
          endAt: [
            0,
            40
          ],
          meta: {
            desc: "Камин"
          }
        },
        {
          id: "linkQHP8ptwYFqZwiLiE",
          startId: "nodeBiwjB9izKq8RkLFE",
          endId: "nodey4FJL3ShWY3Z2wCQ",
          startAt: [
            160,
            40
          ],
          endAt: [
            0,
            40
          ],
          meta: {
            desc: "Слева"
          }
        },
        {
          id: "link9KoGVVr3xL1EokAw",
          startId: "nodeefb0cDJpWbzZb5SQ",
          endId: "nodeFqKf8bjHZTS9zniA",
          startAt: [
            160,
            40
          ],
          endAt: [
            0,
            40
          ],
          meta: {
            desc: "Открыть дверь"
          }
        },
        {
          id: "linkSBrwKcSh5eEpXYfl",
          startId: "nodejvPU5O9KYE3wFByZ",
          endId: "nodeefb0cDJpWbzZb5SQ",
          startAt: [
            160,
            40
          ],
          endAt: [
            0,
            40
          ],
          meta: {
            desc: "Слева"
          }
        },
        {
          id: "linkb5WSoxNNejJASctO",
          startId: "nodeefb0cDJpWbzZb5SQ",
          endId: "nodeSihHPDIVzfgTgnvP",
          startAt: [
            160,
            40
          ],
          endAt: [
            0,
            25
          ],
          meta: {
            desc: "Обыскать шкаф"
          }
        },
        {
          id: "linkvE1FNSFqFwt0eHYz",
          startId: "nodeuZ2DF6Mbml2q6O6C",
          endId: "nodedgHiDUusyGgfVAqS",
          startAt: [
            160,
            40
          ],
          endAt: [
            0,
            25
          ],
          meta: {
            desc: "Пойти прямо"
          }
        },
        {
          id: "link8fvsDh0kiIM77NH0",
          startId: "nodeYN5yw6knNlgl1eee",
          endId: "nodeuZ2DF6Mbml2q6O6C",
          startAt: [
            160,
            40
          ],
          endAt: [
            0,
            40
          ],
          meta: {
            desc: "Зайти в дверь"
          }
        },
        {
          id: "linkoXJ7aM3NGb724cSy",
          startId: "nodey4FJL3ShWY3Z2wCQ",
          endId: "nodeYN5yw6knNlgl1eee",
          startAt: [
            80,
            80
          ],
          endAt: [
            0,
            40
          ],
          meta: {
            desc: "Диван"
          }
        }
      ]
    },
      setCurrentNode(nodeId) {
        if (!nodeId) {
          this.currentNode = this.findStartNode();
          this.player1NodeId = this.currentNode.id;
        } else {
          this.currentNode = this.findNextNode(nodeId);
        }
        this.setCurrentLinks();
      },
      findStartNode() {
        for (let i=0;i<this.nodes.length;i++) {
          console.log('check node for start', typeof(node));
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
</style>
