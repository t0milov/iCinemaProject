import Vue from 'vue'
import App from './components/App'
import SuperFlow from '../packages/index'
import ElementUI from 'element-ui'
import Vuetify from ;
import 'element-ui/lib/theme-chalk/index.css'


Vue.use(SuperFlow)
Vue.use(ElementUI)
Vue.use(Vuetify)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
