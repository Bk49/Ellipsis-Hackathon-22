<script>
// export default {
//         username: '',
//         password: ''
//         data() {
//             return {};
//         }
//     }
</script>

<template>
    <div class="center">
        <img src="../../assets/logo.png" />
        <div id="login" class="center2">
            <span class="p-float-label">
                <InputText id="username" type="text" v-model="value2" placeholder="Username"/>
            </span>

            <span
                >{{ value1 }}
                <InputText
                    name="password"
                    type="password"
                    v-model="password"
                    placeholder="Password"
                />
            </span>

            <div class = "center" style = "top: 120%">
                <router-link to="/edit-client">
                    <Button label="Login"></Button>
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