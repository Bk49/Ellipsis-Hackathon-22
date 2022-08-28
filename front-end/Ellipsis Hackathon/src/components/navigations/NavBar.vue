<template>
  <div>
    <Menubar :model="items">
      <template #start>
        <img src="../../assets/profinance.jpg" height="70" />
      </template>
      <template>
        <router-link :to="item.to">{{ item.label }} </router-link>
      </template>
      <template #end> </template>
    </Menubar>
  </div>
</template>

<script>
const role = localStorage.getItem("role");

export default {
  data() {
    return {
      items:
        role === "admin"
          ? [
              {
                label: "Financing Request List - Admin",
                icon: "pi pi-fw pi-file",
                to: "/admin-overview-financing-request",
                type: "admin",
              },
              {
                label: "Client List",
                icon: "pi pi-fw pi-pencil",
                to: "/list-client",
                type: "admin",
              },
            ]
          : role === "client"
          ? [
              {
                label: "Financing Request List - Client",
                icon: "pi pi-fw pi-user",
                to: "/client-overview-financing-request",
                type: "client",
              },
              {
                label: "Update Financing Request",
                icon: "pi pi-fw pi-user",
                to: "/create-financing-request",
                type: "client",
              },
            ]
          : [],
    };
  },
};
</script>