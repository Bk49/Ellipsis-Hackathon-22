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
    </Menubar>
  </div>
</template>

<script>
export default {
			data() {
				return {
					items: [
						{
							label:'Financing Request List - Admin',
							icon:'pi pi-fw pi-file',
						},
						{
							label:'Client List',
							icon:'pi pi-fw pi-pencil',
						},
						{
							label:'Financing Request List - Client',
							icon:'pi pi-fw pi-user',
				        },
                        {
							label:'Update Financing Request',
							icon:'pi pi-fw pi-user',
				        },
                        {
							label:'GS Tools',
							icon:'pi pi-fw pi-user',
				        }
                    ]
			    }
		    }
        }
</script>