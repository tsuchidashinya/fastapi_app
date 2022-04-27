import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/propTest',
    name: 'proptest',
    props: {
      // 複数ある場合はそれぞれに設定。"component:"の場合はprops:trueとか
      default: true,
      slot1: true
    },
    components:{
      default: () =>
        import(/* webpackChunkName: "propTest" */ '../views/PageComponent1.vue')
      // slot1: () =>
      //   import(/* webpackChunkName: "propTest" */ './views/PageComponent2.vue')
    }
  },
  {
    path: "/propTest2",
    name: 'proptest2',
    props: true,
    components: () => import('../views/PageComponent2.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
