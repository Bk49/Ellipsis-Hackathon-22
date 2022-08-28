<template>
  <div>
	<nav>
	<router-link :to="{name: name}"></router-link>
    <Menubar :model="items">
      <template #start>
        <img
          alt="logo"
          src="https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png"
          height="40"
          class="mr-2"
        />
      </template>
    </Menubar>
	</nav>
  </div>
</template>

<script>
export default {
			data() {
				return {
					items: [
						{
							name: "Financing Request List - Admin",
							label:'Financing Request List - Admin',
							path: "/admin-overview-financing-request",
						},
						{
							name: "Client List",
							label:'Client List',
							path: "/list-client",
						},
						{
							name: "Financing Request List - Client",
							label:'Financing Request List - Client',
							path: "/client-overview-financing-request",
				        },
                        {
							name: "Update Financing Request",
							label:'Update Financing Request',
							path: "/view-financing-request",
				        },
                    ]
			    }
		    }
        }
</script>