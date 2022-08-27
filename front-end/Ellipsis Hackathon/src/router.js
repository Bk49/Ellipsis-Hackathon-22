import {createRouter, createWebHashHistory} from "vue-router"
import Login from "./pages/shared/Login.vue";
import CreateUpdateClient from "./pages/admin/CreateUpdateClient.vue";

const routes = [
    { path: "/", component: Login },
    { path: "/edit-client", component: CreateUpdateClient },
    { path: "/list-client", component: ListClient },
    { path: "/admin-overview-financing-request", component: AdminListFinancingReq },
    { path: "/view-financing-request", component: ViewFinancingReq },
    { path: "/create-financiang-request", component: CreateUpdateFinancingReq },
    { path: "/client-overview-financing-req", component: ClientListFinancingReq },
    { path: "/view-tools", component: ViewGSTools },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router