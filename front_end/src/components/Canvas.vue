<!--
 * User: CHT
 * Date: 2020/5/27
 * Time: 9:52
-->
<template>
  <v-app>
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
          </div>
        </template>
      </super-flow>
      <v-dialog v-model="drawerConf.visible"
                max-width="70%"
                class="scenario-dialog"
      >
        <div v-show="drawerConf.type === drawerType.node">
        <v-card height="40vh">
          <v-text-field
              label="Название сцены"
              color="green darken-2"
              class="pa-5"
              v-model="nodeSetting.name"
          ></v-text-field>
          <v-textarea
              name="input-7-4"
              color="green darken-2"
              label="Здесь можно кратко описать что происходит в этой сцене"
              class="pa-5"
              v-model="nodeSetting.desc"
          ></v-textarea>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn
                color="green"
                text
                @click="settingSubmit()"
            >
              OK
            </v-btn>
          </v-card-actions>
        </v-card>
        </div>

        <div v-show="drawerConf.type === drawerType.link">
          <v-card height="40vh">
            <v-text-field
                label="Название действия"
                color="green darken-2"
                class="pa-5"
                v-model="linkSetting.desc"
            ></v-text-field>
            <v-textarea
                name="input-7-4"
                color="green darken-2"
                label="Здесь можно кратко описать действие"
                class="pa-5"
                v-model="linkSetting.name"
            ></v-textarea>
            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn
                  color="green"
                  text
                  @click="settingSubmit()"
              >
                OK
              </v-btn>
            </v-card-actions>
          </v-card>
        </div>
      </v-dialog>
      <!--    <el-dialog-->
      <!--        :title="drawerConf.title"-->
      <!--        :visible.sync="drawerConf.visible"-->
      <!--        :close-on-click-modal="false"-->
      <!--        width="500px">-->
      <!--      <el-form-->
      <!--          @keyup.native.enter="settingSubmit"-->
      <!--          @submit.native.prevent-->
      <!--          v-show="drawerConf.type === drawerType.node"-->
      <!--          ref="nodeSetting"-->
      <!--          :model="nodeSetting">-->
      <!--        <el-form-item-->
      <!--            label="Node name"-->
      <!--            prop="name">-->
      <!--          <el-input-->
      <!--              v-model="nodeSetting.name"-->
      <!--              placeholder="Please enter the node name"-->
      <!--              maxlength="30">-->
      <!--          </el-input>-->
      <!--        </el-form-item>-->
      <!--        <el-form-item-->
      <!--            label="Node description"-->
      <!--            prop="desc">-->
      <!--          <el-input-->
      <!--              v-model="nodeSetting.desc"-->
      <!--              placeholder="Please enter a node description"-->
      <!--              maxlength="30">-->
      <!--          </el-input>-->
      <!--        </el-form-item>-->
      <!--      </el-form>-->
      <!--      <el-form-->
      <!--          @keyup.native.enter="settingSubmit"-->
      <!--          @submit.native.prevent-->
      <!--          v-show="drawerConf.type === drawerType.link"-->
      <!--          ref="linkSetting"-->
      <!--          :model="linkSetting">-->
      <!--        <el-form-item-->
      <!--            label="Connection description"-->
      <!--            prop="desc">-->
      <!--          <el-input-->
      <!--              v-model="linkSetting.desc"-->
      <!--              placeholder="Please enter a connection description">-->
      <!--          </el-input>-->
      <!--        </el-form-item>-->
      <!--      </el-form>-->
      <!--      <span-->
      <!--          slot="footer"-->
      <!--          class="dialog-footer">-->
      <!--        <el-button-->
      <!--            @click="drawerConf.cancel">-->
      <!--          Cancel-->
      <!--        </el-button>-->
      <!--        <el-button-->
      <!--            type="primary"-->
      <!--            @click="settingSubmit">-->
      <!--          Accept-->
      <!--        </el-button>-->
      <!--      </span>-->
      <!--    </el-dialog>-->

    </div>
  </v-app>
</template>

<script>
const drawerType = {
  node: 0,
  link: 1
}

export default {
  data() {
    return {
      drawerType,
      drawerConf: {
        title: '',
        visible: false,
        type: null,
        info: null,
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

      nodeActions:
        {
          createNewNode(node ,graph) {
            console.log('Вызвался лог')
            graph.addNode({
              width: 80,
              height: 50,
              coordinate: [100, 100],
              meta: {
                name: 'Название'
              }
            })
          }
        },

      graphMenuList: [
        [
          {
            label: 'Добавить начало',
            disable(graph) {
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
            label: 'Добавить сцену',
            disable: false,
            selected: (graph, coordinate) => {
              graph.addNode({
                width: 160,
                height: 80,
                coordinate: coordinate,
                meta: {
                  prop: 'cc',
                  name: 'Сцена'
                }
              })
            }
          },
          {
            label: 'Добавить конец',
            selected: (graph, coordinate) => {
              graph.addNode({
                width: 160,
                height: 50,
                coordinate: coordinate,
                meta: {
                  prop: 'end',
                  name: 'Концовка'
                }
              })
            }
          }
        ],
        [
          {
            label: 'Сохранить',
            selected: (graph, coordinate) => {
              console.log(JSON.stringify(graph.toJSON(), null, 2))
            }
          },
          {
            label: 'Выделить все',
            selected: (graph, coordinate) => {
              graph.selectAll()
            }
          }
        ]
      ],
      nodeMenuList: [
        [
          {
            label: 'Удалить',
            disable: false,
            hidden(node) {
              return node.meta.prop === 'start'
            },
            selected(node, coordinate) {
              node.remove()
            }
          }
        ],
        [
          {
            label: 'Изменить',
            selected: (node, coordinate) => {
              this.drawerConf.open(drawerType.node, node)
            }
          }
        ]
      ],
      linkMenuList: [
        [
          {
            label: 'Удалить действие',
            disable: false,
            selected: (link, coordinate) => {
              link.remove()
            }
          }
        ],
        [
          {
            label: 'Изменить действие',
            disable: false,
            selected: (link, coordinate) => {
              this.drawerConf.open(drawerType.link, link)
            }
          }
        ]
      ]
    }
  },
  created() {
    const nodeList = [
      {
        'id': 'nodeS3WgFnzCI15X58Qw',
        'width': 160,
        'height': 80,
        'coordinate': [-1200, -1600],
        'meta': {
          'prop': 'start',
          'name': 'Начало'
        }
      }
    ]
    const linkList = []

    setTimeout(() => {
      this.nodeList = nodeList
      this.linkList = linkList
    }, 100)
  },
  mounted() {
    this.$nextTick(() => {
      this.$el.scrollBy({
        left: (this.$el.scrollWidth - this.$el.clientWidth) / 2,
        top: (this.$el.scrollHeight - this.$el.clientHeight) / 2
      })
    })
  },
  methods: {
    enterIntercept(formNode, toNode, graph) {
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
    outputIntercept(node, graph) {
      return !(node.meta.prop === 'end')
    },
    linkDesc(link) {
      return link.meta ? link.meta.desc : ''
    },
    settingSubmit() {
      const conf = this.drawerConf
      if (this.drawerConf.type === drawerType.node) {
        if (!conf.info.meta) conf.info.meta = {}
        Object.keys(this.nodeSetting).forEach(key => {
          //что за ебаная conf.info.meta
          this.$set(conf.info.meta, key, this.nodeSetting[key])
        })
        //нужно для element ui
        // this.$refs.nodeSetting.resetFields()
      } else {
        if (!conf.info.meta) conf.info.meta = {}
        Object.keys(this.linkSetting).forEach(key => {
          this.$set(conf.info.meta, key, this.linkSetting[key])
        })
        // this.$refs.linkSetting.resetFields()
      }
      conf.visible = false
      console.log(conf)
    }
  }
}
</script>

<style lang="less">
//<!--костыль для того чтобы открывался dialog-->
.v-dialog__container {
  display: unset !important;
}

.plus{
  @node-width: 160px;
  font-size: 36px;
  margin-left: @node-width + 10px;
}

.scenario-dialog {
  height: 80%;
}

.ellipsis {
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  word-wrap: break-word;
}

.disable-box-shadow {
  box-shadow: none !important;
}


.super-flow-base-demo {
  width: 100%;
  height: 100%;
  margin: 0 auto;
  background-color: #f5f5f5;
  overflow: scroll;

  .super-flow {
    width: 100%;
    height: 100%;
  }

  .super-flow__node {
    .flow-node {
      > header {
        font-size: 14px;
        height: 32px;
        line-height: 32px;
        padding: 0 12px;
        color: #ffffff;
      }

      > section {
        text-align: center;
        line-height: 20px;
        overflow: hidden;
        padding: 6px 12px;
        word-break: break-all;
      }

      &.flow-node-start {
        > header {
          background-color: #55abfc;
        }
      }

      &.flow-node-condition {
        > header {
          background-color: #BC1D16;
        }
      }

      &.flow-node-approval {
        > header {
          background-color: rgba(188, 181, 58, 0.76);
        }
      }

      &.flow-node-cc {
        > header {
          background-color: #30b95c;
        }
      }

      &.flow-node-end {
        > header {
          height: 50px;
          line-height: 50px;
          background-color: rgb(0, 0, 0);
        }
      }
    }
  }
}
</style>
