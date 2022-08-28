<template>
  <div>
    <Menubar :model="items">
      <template #start>
        <img
          alt="logo"
          src="https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png"
          height="40"
          class="mr-2"
        />
      </template>
	  <template>
		<router-link :to="item.to" custom v-slot="{href, route, navigate, isActive, isExactActive}">
            <a :href="href" @click="navigate" :class="{'active-link': isActive, 'active-link-exact': isExactActive}">{{item.label}}</a>
        </router-link>
	  </template>
	  <template #end>
	  <p>YOZA DA BEST</p>
	  </template>
    </Menubar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          label: "Financing Request List - Admin",
          icon: "pi pi-fw pi-file",
		  to: "/admin-overview-financing-request",
        },
        {
          label: "Client List",
          icon: "pi pi-fw pi-pencil",
		  to: "/list-client",
        },
        {
          label: "Financing Request List - Client",
          icon: "pi pi-fw pi-user",
		  to: "/client-overview-financing-request",
        },
        {
          label: "Update Financing Request",
          icon: "pi pi-fw pi-user",
		  to: "/create-financing-request",
        },
      ],
    };
  },
};
</script>