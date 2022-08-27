<script>
</script>

<template>
    <div>
        <router-link to="/edit-client">
            <Button label="Login"></Button>
        </router-link>

        <div id="login">
            <h1>Login</h1>
            <div class="form-inputs">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" v-model="input.username" placeholder="Username" />
            </div>
            <div class="form-inputs">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" v-model="input.password" placeholder="Password" />
            </div>
            <button type="button" v-on:click="login()">Login</button>
        </div>

             
    </div>



</template>

<style scoped>
</style>