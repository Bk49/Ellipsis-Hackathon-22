<script>
export default {
        methods: {
            async authenticate() {
                try {
                    const requestOptions = {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ username: this.username, password: this.password })
                    };
                    let response = await fetch("http://127.0.0.1:5001/authenticate", requestOptions);
                    const data = await response.json()
                    console.log(data.role);

                } catch (error) {
                    console.log(error);
                }
            }
        }
    }
</script>

<template>
    <div class = "center">
        <img src="../../assets/logo.png" />
        <div id="login" class = "center2">
            <span class="p-float-label">
                <InputText id="username" type="text" v-model="username" placeholder="Username"/>
            </span>

            <span>{{ value1 }}
                <InputText name = "password" type="password" v-model="password" placeholder="Password"/>
            </span>

            <div class = "center" style = "top: 120%">
                <router-link to="/edit-client">
                    <Button label="Login" v-on:click="authenticate()"></Button>
                </router-link>
            </div>
        </div>
    </div>
</template>

<style scoped>
.center {
position: absolute;
left: 50%;
top: 50%;
transform: translate(-50%, -50%);
padding: 10px;
}

.center2 {
position: absolute;
left: 50%;
top: 100%;
transform: translate(-50%, -50%);
padding: 10px;
}
</style>