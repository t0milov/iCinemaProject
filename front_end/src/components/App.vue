<!--
 * User: CHT
 * Date: 2020/6/28
 * Time: 17:48
-->
<template>
  <v-app>
    <div class="super-flow-base-demo">
      <div class="super-flow-demo1">
        <div class="node-container">
        <span
            class="node-item"
            v-for="item in nodeItemList"
            @mousedown="evt => nodeItemMouseDown(evt, item.value)">
          {{item.label}}
        </span>
        </div>
        <div
            class="flow-container"
            ref="flowContainer">
          <super-flow
              ref="superFlow"
              :graph-menu="graphMenu"
              :node-menu="nodeMenu"
              :link-menu="linkMenu"
              :link-base-style="linkBaseStyle"
              :link-style="linkStyle"
              :link-desc="linkDesc">
            <template v-slot:node="{meta}">
              <div
                  @mouseup="nodeMouseUp"
                  @click="nodeClick"
                  class="flow-node ellipsis">
                {{meta.name}}
              </div>
            </template>
          </super-flow>
        </div>
      </div>
      <v-dialog v-model="drawerConf.visible"
                max-width="70%"
                class="scenario-dialog"
      >
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
      </v-dialog>
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
          console.log('here')
          if (conf.type === drawerType.node) {
            conf.title = 'узел'
            console.log( 'debug',this.$refs,this.$refs.nodeSetting)
            if (this.$refs.nodeSetting) this.$refs.nodeSetting.resetFields()
            this.$set(this.nodeSetting, 'name', info.meta.name)
            this.$set(this.nodeSetting, 'desc', info.meta.desc)
          } else {
            conf.title = 'узел'
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

      dragConf: {
        isDown: false,
        isMove: false,
        offsetTop: 0,
        offsetLeft: 0,
        clientX: 0,
        clientY: 0,
        ele: null,
        info: null
      },
      nodeItemList: [
        {
          label: 'Начало',
          value: {
            width: 120,
            height: 120,
            meta: {
              label: '1',
              name: 'Начало'
            }
          }
        },
        {
          label: 'Сцена',
          value: {
            width: 120,
            height: 120,
            meta: {
              label: '2',
              name: 'Сцена'
            }
          }
        },
        {
          label: 'Комментарий',
          value: {
            width: 120,
            height: 120,
            meta: {
              label: '3',
              name: 'Комментарий'
            }
          }
        },
        {
          label: 'Титры',
          value: {
            width: 120,
            height: 120,
            meta: {
              label: '4',
              name: 'Титры'
            }
          }
        }
      ],

      graphMenu: [
        [
          {
            label: 'Начало',
            disable(graph) {
              return !!graph.nodeList.find(node => node.meta.label === '1')
            },
            selected(graph, coordinate) {
              graph.addNode({
                width: 120,
                height: 120,
                coordinate,
                meta: {
                  label: '1',
                  name: 'Начало'
                }
              })
            }
          },
          {
            label: 'Сцена',
            selected(graph, coordinate) {
              graph.addNode({
                width: 120,
                height: 120,
                coordinate,
                meta: {
                  label: '2',
                  name: 'Сцена'
                }
              })
            }
          },
          {
            label: 'Комментарий',
            selected(graph, coordinate) {
              graph.addNode({
                width: 120,
                height: 120,
                coordinate,
                meta: {
                  label: '3',
                  name: 'Комментарий'
                }
              })
            }
          }
        ],
        [
          {
            label: 'Титры',
            selected(graph, coordinate) {
              graph.addNode({
                width: 120,
                height: 120,
                coordinate,
                meta: {
                  label: '4',
                  name: 'Титры'
                }
              })
            }
          }
        ],
        [
          {
            label: 'Выбрать все',
            selected: graph => {
              graph.selectAll()
            }
          },
          {
            label: 'Сохранить',
            selected: graph => {
              console.log('josn',graph.toJSON())
            }
          }
        ]
      ],
      nodeMenu: [
        [
          {
            label: 'Стереть',
            selected: node => {
              node.remove()
            }
          },
          {
            label: 'Редактировать',
            selected: node => {
              this.drawerConf.open(drawerType.node, node)
            }
          }
        ]
      ],
      linkMenu: [
        [
          {
            label: 'Стереть',
            selected: link => {
              link.remove()
            }
          },
          {
            label: 'Редактировать',
            selected: link => {
              this.drawerConf.open(drawerType.link, link)
            }
          }
        ]
      ],

      linkBaseStyle: {
        color: '#666666',           // line 颜色
        hover: '#FF0000',           // line hover 的颜色
        textColor: '#666666',       // line 描述文字颜色
        textHover: '#FF0000',       // line 描述文字 hover 颜色
        font: '14px Arial',         // line 描述文字 字体设置 参考 canvas font
        dotted: false,              // 是否是虚线
        lineDash: [4, 4],           // 虚线时生效
        background: 'rgba(255,255,255,0.6)'    // 描述文字背景色
      },
      fontList: [
        '14px Arial',
        'italic small-caps bold 12px arial'
      ]
    }
  },
  mounted() {
    document.addEventListener('mousemove', this.docMousemove)
    document.addEventListener('mouseup', this.docMouseup)
  },
  beforeUnmount(){
    document.removeEventListener('mousemove', this.docMousemove)
    document.removeEventListener('mouseup', this.docMouseup)
  },
  methods: {
    flowNodeClick(meta) {
      console.log(this.$refs.superFlow.graph)
    },
    linkStyle(link) {
      return {
        // hover: '#FF00FF'
      }
    },
    linkDesc(link) {
      return link.meta ? link.meta.desc : ''
    },
    settingSubmit() {
      const conf = this.drawerConf
      if (this.drawerConf.type === drawerType.node) {
        if (!conf.info.meta) conf.info.meta = {}
        Object.keys(this.nodeSetting).forEach(key => {
          this.$set(conf.info.meta, key, this.nodeSetting[key])
          // conf.info.meta[key] = this.nodeSetting[key]
        })
        console.log('Changed node name and desc')
      } else {
        if (!conf.info.meta) conf.info.meta = {}
        Object.keys(this.linkSetting).forEach(key => {
          this.$set(conf.info.meta, key, this.linkSetting[key])
          // conf.info.meta[key] = this.linkSetting[key]
        })
      }
      conf.visible = false
    },

    nodeMouseUp(evt) {
      evt.preventDefault()
    },

    nodeClick() {
      console.log(arguments)
    },

    docMousemove({clientX, clientY}) {
      const conf = this.dragConf

      if (conf.isMove) {

        conf.ele.style.top = clientY - conf.offsetTop + 'px'
        conf.ele.style.left = clientX - conf.offsetLeft + 'px'

      } else if (conf.isDown) {

        // 鼠标移动量大于 5 时 移动状态生效
        conf.isMove =
            Math.abs(clientX - conf.clientX) > 5
            || Math.abs(clientY - conf.clientY) > 5

      }
    },

    docMouseup({clientX, clientY}) {
      const conf = this.dragConf
      conf.isDown = false

      if (conf.isMove) {
        const {
          top,
          right,
          bottom,
          left
        } = this.$refs.flowContainer.getBoundingClientRect()

        // 判断鼠标是否进入 flow container
        if (
            clientX > left
            && clientX < right
            && clientY > top
            && clientY < bottom
        ) {

          // 获取拖动元素左上角相对 super flow 区域原点坐标
          const coordinate = this.$refs.superFlow.getMouseCoordinate(
              clientX - conf.offsetLeft,
              clientY - conf.offsetTop
          )

          // 添加节点
          this.$refs.superFlow.addNode({
            coordinate,
            ...conf.info
          })

        }

        conf.isMove = false
      }

      if (conf.ele) {
        conf.ele.remove()
        conf.ele = null
      }
    },

    nodeItemMouseDown(evt, info) {
      const {
        clientX,
        clientY,
        currentTarget
      } = evt

      const {
        top,
        left
      } = evt.currentTarget.getBoundingClientRect()

      const conf = this.dragConf
      const ele = currentTarget.cloneNode(true)

      Object.assign(this.dragConf, {
        offsetLeft: clientX - left,
        offsetTop: clientY - top,
        clientX: clientX,
        clientY: clientY,
        info,
        ele,
        isDown: true
      })

      ele.style.position = 'fixed'
      ele.style.margin = '0'
      ele.style.top = clientY - conf.offsetTop + 'px'
      ele.style.left = clientX - conf.offsetLeft + 'px'

      this.$el.appendChild(this.dragConf.ele)
    }
  }
}
</script>

<style lang="less">

.ellipsis {
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  word-wrap: break-word;
}

.link-base-style-form {
  .el-form-item {
    margin-bottom : 12px;
  }

  padding-bottom : 20px;
  border-bottom  : 1px solid #DCDCDC;
}

.super-flow-demo1 {
  margin-top       : 20px;
  width            : 100%;
  height           : 800px;
  background-color : rgba(189, 153, 185, 0.6);
  @list-width      : 200px;


  > .node-container {
    width            : @list-width;
    float            : left;
    height           : 100%;
    text-align       : center;
    background-color : rgba(143, 94, 138, 0.6);
  }

  > .flow-container {
    width    : calc(100% - @list-width);
    float    : left;
    height   : 100%;
    overflow : hidden;
  }

  .super-flow__node {
    .flow-node {
      box-sizing  : border-box;
      width       : 100%;
      height      : 100%;
      line-height : 40px;
      padding     : 0 6px;
      font-size   : 20px;
    }
  }
}

.node-item {
  @node-item-height : 30px;

  font-size         : 16px;
  display           : inline-block;
  height            : @node-item-height;
  width             : 120px;
  margin-top        : 20px;
  background-color  : #FFFFFF;
  line-height       : @node-item-height;
  box-shadow        : 1px 1px 4px rgba(0, 0, 0, 0.3);
  cursor            : pointer;
  user-select       : none;
  text-align        : center;
  z-index           : 6;

  &:hover {
    box-shadow : 1px 1px 8px rgba(0, 0, 0, 0.4);
  }
}

</style>
