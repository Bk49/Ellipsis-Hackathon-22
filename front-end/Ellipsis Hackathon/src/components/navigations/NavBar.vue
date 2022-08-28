<template>
  <div>
    <Menubar :model="items">
    <template #item="{item}">
        <router-link :to="item.to" custom v-slot="{href, route, navigate, isActive, isExactActive}">
            <a :href="href" @click="navigate" :class="{'active-link': isActive, 'active-link-exact': isExactActive}">{{route.fullPath}}
				item.labels
			</a>
        </router-link>
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
          name: "Financing Request List - Admin",
          label: "Financing Request List - Admin",
          to: "/admin-overview-financing-request",
        },
        {
          name: "Client List",
          label: "Client List",
          to: "/list-client",
        },
        {
          name: "Financing Request List - Client",
          label: "Financing Request List - Client",
          to: "/client-overview-financing-request",
        },
        {
          name: "Update Financing Request",
          label: "Update Financing Request",
          to: "/view-financing-request",
        },
      ],
    };
  },
};
</script>