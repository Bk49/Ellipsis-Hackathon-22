import {createRouter, createWebHashHistory} from "vue-router"
import Login from "./pages/shared/Login.vue";
import CreateUpdateClient from "./pages/admin/CreateUpdateClient.vue";

const routes = [
    { path: "/", component: Login },
    { path: "/edit-client", component: CreateUpdateClient },
    { path: "/list-client", component: ListClient },
    { path: "/edit-client", component: ListFinancingReq },
    { path: "/edit-client", component: ViewFinancingReq },
    { path: "EDIT", component: CreateUpdateFinancingReq },
    { path: "EDIT", component: ListFinancingReq },
    { path: "EDIT", component: ViewGSTools },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router