<script>

</script>

<template>
    <div>
        <router-link to="/edit-client">
            <Button label="Login"></Button>
        </router-link>
        <div>
            <h5>Floating Label</h5>
            <span class="p-float-label">
            <InputText id="username" type="text" v-model="value2" />
            <label for="username">Username</label>
            </span>
        </div>
    </div>




</template>

<style scoped>
   
</style>