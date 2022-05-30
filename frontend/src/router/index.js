import { createRouter, createWebHistory } from 'vue-router'


const routes = [
    {
        path: '/admin1',
        name: 'admin1',
        component: () => import('../views/Admin_multi.vue'),
        props: true
    },
    {
        path: '/home',
        name: 'home',
        component: () => import('../views/HomeView.vue'),
        props: true
    },
    {
        path: '/register',
        name: 'register1',
        component: () => import('../views/Register_multi.vue'),
        props: true
    },
    {
        path: '/',
        name: '/first_window',
        component: () => import('../views/first_window.vue')
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router