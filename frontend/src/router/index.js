import { createRouter, createWebHistory } from 'vue-router'


const routes = [
    {
        path: '/admin1',
        name: 'admin1',
        component: () => import('../views/Admin_multi.vue'),
        props: true
    },
    {
        path: '/',
        name: 'home',
        component: () => import('../views/HomeView.vue'),
        props: true
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router