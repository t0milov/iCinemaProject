import Vue from 'vue'
import App from './components/App'
import SuperFlow from '../packages/index'
import ElementUI from 'element-ui'
import VueRouter from 'vue-router'
import 'element-ui/lib/theme-chalk/index.css'
import vuetify from './plugins/vuetify'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'


Vue.use(SuperFlow)
Vue.use(ElementUI)
Vue.use(VueRouter)

Vue.config.productionTip = false

const routes = [
  { path: '/#', component: App },
  { path: '/graph', component: SuperFlow }
]

const router = new VueRouter({
  routes // сокращённая запись для `routes: routes`
})

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
