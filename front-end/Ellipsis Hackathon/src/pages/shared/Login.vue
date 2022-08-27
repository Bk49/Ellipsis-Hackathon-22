<script>
</script>

<template>
    <div>
        <router-link to="/edit-client">
            <Button label="Login"></Button>
        </router-link>

        <div id="login">
            <span class="p-float-label">
                <InputText id="username" type="text" v-model="value2" />
                <label for="username">Username</label>
            </span>

            <InputText type="password" v-model="value1" />
            <span :style="{marginLeft: '.5em'}">{{value1}}</span>
        </div>

             
    </div>



</template>

<style scoped>
</style>