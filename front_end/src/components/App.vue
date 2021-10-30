<!--
 * User: CHT
 * Date: 2020/5/27
 * Time: 9:52
-->
<template>
  <div class="super-flow-base-demo">
    <super-flow
        ref="superFlow"
        :node-list="nodeList"
        :link-list="linkList"
        :origin="origin"
        :graph-menu="graphMenuList"
        :node-menu="nodeMenuList"
        :link-menu="linkMenuList"
        :enter-intercept="enterIntercept"
        :output-intercept="outputIntercept"
        :link-desc="linkDesc">
      <template v-slot:node="{meta}">
        <div :class="`flow-node flow-node-${meta.prop}`">
          <header class="ellipsis">
            {{ meta.name }}
          </header>
          <section>
            {{ meta.desc }}
          </section>
        </div>
      </template>
    </super-flow>
    <v-dialog v-model="this.drawerConf.visible">
      <v-card>
        <v-card-title class="text-h5">
          Use Google's location service?
        </v-card-title>

        <v-card-text>
          Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running.
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
              color="green darken-1"
              text
              @click="dialog = false"
          >
            Disagree
          </v-btn>

          <v-btn
              color="green darken-1"
              text
              @click="dialog = false"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <el-dialog
        :title="drawerConf.title"
        :visible.sync="drawerConf.visible"
        :close-on-click-modal="false"
        width="500px">
      <el-form
          @keyup.native.enter="settingSubmit"
          @submit.native.prevent
          v-show="drawerConf.type === drawerType.node"
          ref="nodeSetting"
          :model="nodeSetting">
        <el-form-item
            label="Node name"
            prop="name">
          <el-input
              v-model="nodeSetting.name"
              placeholder="Please enter the node name"
              maxlength="30">
          </el-input>
        </el-form-item>
        <el-form-item
            label="Node description"
            prop="desc">
          <el-input
              v-model="nodeSetting.desc"
              placeholder="Please enter a node description"
              maxlength="30">
          </el-input>
        </el-form-item>
      </el-form>
      <el-form
          @keyup.native.enter="settingSubmit"
          @submit.native.prevent
          v-show="drawerConf.type === drawerType.link"
          ref="linkSetting"
          :model="linkSetting">
        <el-form-item
            label="Connection description"
            prop="desc">
          <el-input
              v-model="linkSetting.desc"
              placeholder="Please enter a connection description">
          </el-input>
        </el-form-item>
      </el-form>
      <span
          slot="footer"
          class="dialog-footer">
        <el-button
            @click="drawerConf.cancel">
          Cancel
        </el-button>
        <el-button
            type="primary"
            @click="settingSubmit">
          Accept
        </el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
const drawerType = {
  node: 0,
  link: 1
}

export default {
  data () {
    return {
      drawerType,
      drawerConf: {
        title: '',
        visible: true,
        type: null,
        info: null,
        dialog: false,
        open: (type, info) => {
          const conf = this.drawerConf
          conf.visible = true
          conf.type = type
          conf.info = info
          if (conf.type === drawerType.node) {
            conf.title = 'Node'
            if (this.$refs.nodeSetting) this.$refs.nodeSetting.resetFields()
            this.$set(this.nodeSetting, 'name', info.meta.name)
            this.$set(this.nodeSetting, 'desc', info.meta.desc)
          } else {
            conf.title = 'Connect'
            if (this.$refs.linkSetting) this.$refs.linkSetting.resetFields()
            this.$set(this.linkSetting, 'desc', info.meta ? info.meta.desc : '')
          }
        },
        cancel: () => {
          this.drawerConf.visible = false
          if (this.drawerConf.type === drawerType.node) {
            this.$refs.nodeSetting.clearValidate()
          } else {
            this.$refs.linkSetting.clearValidate()
          }
        }
      },
      linkSetting: {
        desc: ''
      },
      nodeSetting: {
        name: '',
        desc: ''
      },

      origin: [2000, 2000],
      nodeList: [],
      linkList: [],

      graphMenuList: [
        [
          {
            label: 'label1',
            disable (graph) {
              return !!graph.nodeList.find(node => node.meta.prop === 'start')
            },
            selected: (graph, coordinate) => {
              const start = graph.nodeList.find(node => node.meta.prop === 'start')
              if (!start) {
                graph.addNode({
                  width: 100,
                  height: 80,
                  coordinate: coordinate,
                  meta: {
                    prop: 'start',
                    name: 'start'
                  }
                })
              }
            }
          },
          {
            label: 'label2',
            disable: false,
            selected: (graph, coordinate) => {
              graph.addNode({
                width: 160,
                height: 80,
                coordinate: coordinate,
                meta: {
                  prop: 'condition',
                  name: 'condition'
                }
              })
            }
          },
          {
            label: 'label3',
            disable: false,
            selected: (graph, coordinate) => {
              graph.addNode({
                width: 160,
                height: 80,
                coordinate: coordinate,
                meta: {
                  prop: 'approval',
                  name: 'approval'
                }
              })
            }
          },
          {
            label: 'label3',
            disable: false,
            selected: (graph, coordinate) => {
              graph.addNode({
                width: 160,
                height: 80,
                coordinate: coordinate,
                meta: {
                  prop: 'cc',
                  name: 'cc'
                }
              })
            }
          },
          {
            label: 'label4',
            disable (graph) {
              return !!graph.nodeList.find(point => point.meta.prop === 'end')
            },
            selected: (graph, coordinate) => {
              graph.addNode({
                width: 80,
                height: 50,
                coordinate: coordinate,
                meta: {
                  prop: 'end',
                  name: 'end'
                }
              })
            }
          }
        ],
        [
          {
            label: 'label6',
            selected: (graph, coordinate) => {
              console.log(JSON.stringify(graph.toJSON(), null, 2))
            }
          },
          {
            label: 'label7',
            selected: (graph, coordinate) => {
              graph.selectAll()
            }
          }
        ]
      ],
      nodeMenuList: [
        [
          {
            label: 'Delete',
            disable: false,
            hidden (node) {
              return node.meta.prop === 'start'
            },
            selected (node, coordinate) {
              node.remove()
            }
          }
        ],
        [
          {
            label: 'Configure',
            selected: (node, coordinate) => {
              this.drawerConf.open(drawerType.node, node)
            }
          }
        ]
      ],
      linkMenuList: [
        [
          {
            label: 'remove1',
            disable: false,
            selected: (link, coordinate) => {
              link.remove()
            }
          }
        ],
        [
          {
            label: 'configure1',
            disable: false,
            selected: (link, coordinate) => {
              this.drawerConf.open(drawerType.link, link)
            }
          }
        ]
      ]
    }
  },
  created () {
    const nodeList = [
      {
        'id': 'nodeS3WgFnzCI15X58Qw',
        'width': 100,
        'height': 80,
        'coordinate': [-644, -148],
        'meta': {
          'prop': 'start',
          'name': 'name1'
        }
      },
      {
        'id': 'nodefHsy9uJObPtdHZv1',
        'width': 160,
        'height': 80,
        'coordinate': [-200, -148],
        'meta': {
          'prop': 'approval',
          'name': 'name2',
          'desc': '111111'
        }
      },
      {
        'id': 'nodeni9QOqT3mI7hsMau',
        'width': 160,
        'height': 80,
        'coordinate': [-442, -275],
        'meta': {
          'prop': 'condition',
          'name': 'name3'
        }
      },
      {
        'id': 'nodeZBK0ZPpgMe1exezE',
        'width': 160,
        'height': 80,
        'coordinate': [-200, -275],
        'meta': {
          'prop': 'approval',
          'name': 'name4'
        }
      },
      {
        'id': 'nodeqkK9zjcDz53xKRlK',
        'width': 160,
        'height': 80,
        'coordinate': [34, -209],
        'meta': {
          'prop': 'cc',
          'name': 'name5'
        }
      },
      {
        'id': 'nodeDhVU6w2KbEnJCjZs',
        'width': 80,
        'height': 50,
        'coordinate': [286, -133],
        'meta': {
          'prop': 'end',
          'name': 'name6'
        }
      },
      {
        'id': 'nodesyxisLH1hJDdPsxx',
        'width': 160,
        'height': 80,
        'coordinate': [34, -75],
        'meta': {
          'prop': 'cc',
          'name': 'name7'
        }
      },
      {
        'id': 'node0aiA9VuhjkiAdZCs',
        'width': 160,
        'height': 80,
        'coordinate': [-200, -2],
        'meta': {
          'prop': 'approval',
          'name': 'name8'
        }
      },
      {
        'id': 'nodeG3WeFnzCI15X58Qw',
        'width': 160,
        'height': 80,
        'coordinate': [-442, -2],
        'meta': {
          'prop': 'condition',
          'name': 'name9'
        }
      },
      {
        'id': 'node7WXbwOR6kSFD53Hf',
        'width': 160,
        'height': 80,
        'coordinate': [-442, -148],
        'meta': {
          'prop': 'condition',
          'name': 'name10'
        }
      }
    ]
    const linkList = [
      {
        'id': 'linkcs9ZhumWeTHrtUy8',
        'startId': 'nodeS3WgFnzCI15X58Qw',
        'endId': 'nodeni9QOqT3mI7hsMau',
        'startAt': [100, 40],
        'endAt': [0, 40],
        'meta': null
      },
      {
        'id': 'linkBDld5rDBw4C6kiva',
        'startId': 'nodefHsy9uJObPtdHZv1',
        'endId': 'nodeqkK9zjcDz53xKRlK',
        'startAt': [160, 40],
        'endAt': [0, 40],
        'meta': null
      },
      {
        'id': 'linkA0ZZxRlDI9AOonuq',
        'startId': 'node7WXbwOR6kSFD53Hf',
        'endId': 'nodefHsy9uJObPtdHZv1',
        'startAt': [160, 40],
        'endAt': [0, 40],
        'meta': null
      },
      {
        'id': 'linkhCKTpRAf89gcujGS',
        'startId': 'nodeni9QOqT3mI7hsMau',
        'endId': 'nodeZBK0ZPpgMe1exezE',
        'startAt': [160, 40],
        'endAt': [0, 40],
        'meta': null
      },
      {
        'id': 'link2o7VZ7DRaSFKtB0g',
        'startId': 'nodeqkK9zjcDz53xKRlK',
        'endId': 'nodeDhVU6w2KbEnJCjZs',
        'startAt': [160, 40],
        'endAt': [0, 25],
        'meta': null
      },
      {
        'id': 'linkII013ovDctUDuPLu',
        'startId': 'nodeS3WgFnzCI15X58Qw',
        'endId': 'nodeG3WeFnzCI15X58Qw',
        'startAt': [100, 40],
        'endAt': [0, 40],
        'meta': null
      },
      {
        'id': 'link6MOmsq1EqzlWcG1n',
        'startId': 'nodeZBK0ZPpgMe1exezE',
        'endId': 'nodeqkK9zjcDz53xKRlK',
        'startAt': [160, 40],
        'endAt': [0, 40],
        'meta': null
      },
      {
        'id': 'link52SczSXHmuyKDzRU',
        'startId': 'nodesyxisLH1hJDdPsxx',
        'endId': 'nodeDhVU6w2KbEnJCjZs',
        'startAt': [160, 40],
        'endAt': [0, 25],
        'meta': null
      },
      {
        'id': 'link2hBQDTuIG4ZFYyE0',
        'startId': 'node0aiA9VuhjkiAdZCs',
        'endId': 'nodesyxisLH1hJDdPsxx',
        'startAt': [160, 40],
        'endAt': [0, 40],
        'meta': null
      },
      {
        'id': 'linkrwdW87FmOma5rPVo',
        'startId': 'nodeG3WeFnzCI15X58Qw',
        'endId': 'node0aiA9VuhjkiAdZCs',
        'startAt': [160, 40],
        'endAt': [0, 40],
        'meta': null
      },
      {
        'id': 'linknL75dQV0AWZA85sq',
        'startId': 'nodeS3WgFnzCI15X58Qw',
        'endId': 'node7WXbwOR6kSFD53Hf',
        'startAt': [100, 40],
        'endAt': [0, 40],
        'meta': null
      }
    ]

    setTimeout(() => {
      this.nodeList = nodeList
      this.linkList = linkList
    }, 100)
  },
  mounted () {
    this.$nextTick(() => {
      this.$el.scrollBy({
        left: (this.$el.scrollWidth - this.$el.clientWidth) / 2,
        top: (this.$el.scrollHeight - this.$el.clientHeight) / 2
      })
    })
  },
  methods: {
    enterIntercept (formNode, toNode, graph) {
      const formType = formNode.meta.prop
      switch (toNode.meta.prop) {
        case 'start':
          return false
        case 'approval':
          return [
            'start',
            'approval',
            'condition',
            'cc'
          ].includes(formType)
        case 'condition':
          return [
            'start',
            'approval',
            'condition',
            'cc'
          ].includes(formType)
        case 'end':
          return [
            'approval',
            'cc'
          ].includes(formType)
        default:
          return true
      }
    },
    outputIntercept (node, graph) {
      return !(node.meta.prop === 'end')
    },
    linkDesc (link) {
      return link.meta ? link.meta.desc : ''
    },
    settingSubmit () {
      const conf = this.drawerConf
      if (this.drawerConf.type === drawerType.node) {
        if (!conf.info.meta) conf.info.meta = {}
        Object.keys(this.nodeSetting).forEach(key => {
          this.$set(conf.info.meta, key, this.nodeSetting[key])
        })
        this.$refs.nodeSetting.resetFields()
      } else {
        if (!conf.info.meta) conf.info.meta = {}
        Object.keys(this.linkSetting).forEach(key => {
          this.$set(conf.info.meta, key, this.linkSetting[key])
        })
        this.$refs.linkSetting.resetFields()
      }
      conf.visible = false
    }
  }
}
</script>

<style lang="less">
.ellipsis {
  white-space   : nowrap;
  text-overflow : ellipsis;
  overflow      : hidden;
  word-wrap     : break-word;
}

.super-flow-base-demo {
  width            : 100%;
  height           : 800px;
  margin           : 0 auto;
  background-color : #f5f5f5;
  overflow         : scroll;

  .super-flow {
    width  : 4000px;
    height : 4000px;
  }

  .super-flow__node {
    .flow-node {
      > header {
        font-size   : 14px;
        height      : 32px;
        line-height : 32px;
        padding     : 0 12px;
        color       : #ffffff;
      }

      > section {
        text-align  : center;
        line-height : 20px;
        overflow    : hidden;
        padding     : 6px 12px;
        word-break  : break-all;
      }

      &.flow-node-start {
        > header {
          background-color : #55abfc;
        }
      }

      &.flow-node-condition {
        > header {
          background-color : #BC1D16;
        }
      }

      &.flow-node-approval {
        > header {
          background-color : rgba(188, 181, 58, 0.76);
        }
      }

      &.flow-node-cc {
        > header {
          background-color : #30b95c;
        }
      }

      &.flow-node-end {
        > header {
          height           : 50px;
          line-height      : 50px;
          background-color : rgb(0, 0, 0);
        }
      }
    }
  }
}
</style>
