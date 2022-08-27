import {createRouter, createWebHashHistory} from "vue-router"
import Login from "./pages/shared/Login.vue";
import CreateUpdateClient from "./pages/admin/CreateUpdateClient.vue";

const routes = [
    { path: "/", component: Login },
    { path: "/edit-client", component: CreateUpdateClient },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router