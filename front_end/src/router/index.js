import VueRouter from 'vue-router'
import Canvas from "@/components/Canvas";
import Player from "@/components/Player";
import App from "@/components/App";

export default new VueRouter({
    routes: [
        { path: '/', name:'home',  component: App },
        { path: '/canvas', name:'canvas',  component: Canvas },
        { path: '/player/:projectName', name:'player', component: Player }
    ]
})

