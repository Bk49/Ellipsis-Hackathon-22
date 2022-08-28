import { createRouter, createWebHashHistory } from "vue-router";
import Login from "./pages/shared/Login.vue";
import CreateUpdateClient from "./pages/admin/CreateUpdateClient.vue";
import ListClient from "./pages/admin/ListClient.vue";
import AdminListFinancingReq from "./pages/admin/AdminListFinancingReq.vue";
import ViewFinancingReq from "./pages/admin/ViewFinancingReq.vue";
import CreateFinancingReq from "./pages/client/CreateFinancingReq.vue";
import ClientListFinancingReq from "./pages/client/ClientListFinancingReq.vue";
import UpdateFinancingReq from "./pages/client/UpdateFinancingReq.vue"
//import ViewGSTools from "./pages/client/ViewGSTools.vue";
import ViewGSTools from "./components/table/BaseTable.vue";

import NavBar from "./components/navigations/NavBar.vue";

const routes = [
    { path: "/", component: Login, name: "Login" },
    {
        path: "/edit-client/:id?",
        component: CreateUpdateClient,
        name: "CreateUpdateClient",
    },
    { path: "/list-client", component: ListClient },
    {
        path: "/admin-overview-financing-request",
        component: AdminListFinancingReq,
        name: "AdminListFinancingReq",
    },
    {
        path: "/view-financing-request/:id?",
        component: ViewFinancingReq,
        name: "ViewFinancingReq",
    },
    {
        path: "/create-financing-request/:user_id?",
        component: CreateFinancingReq,
        name: "CreateFinancingReq",
    },
    {
        path: "/update-financing-request/:financing_company_id/:finance_request_id?",
        component: UpdateFinancingReq,
        name: "UpdateFinancingReq",
    },
    {
        path: "/client-overview-financing-request/:id?",
        component: ClientListFinancingReq,
        name: "ClientListFinancingReq",
    },
    { path: "/view-tools", component: ViewGSTools, name: "ViewGSTools" },
    { path: "/nav-bar", component: NavBar },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
