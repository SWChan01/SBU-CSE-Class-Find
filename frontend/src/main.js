import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Home from './components/Home'
import Schedule from './components/Schedule'

Vue.config.productionTip = false
Vue.use(VueRouter);

const router = new VueRouter({
  routes: [
    {path: '/', component: Home},
    {path: '/schedule' , component:Schedule}
  ],
  mode:'history'
}); 









new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
