<script>
export default {
    methods: {
        async authenticate() {
            try {
                const requestOptions = {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        username: this.username,
                        password: this.password,
                    }),
                };
                const response = await fetch(
                    "http://127.0.0.1:5001/authenticate",
                    requestOptions
                ).then((res) => res.json());

                if (response.role) {
                    localStorage.setItem("role", response.role)
                    this.$router.push(
                        `${
                            response.role === "admin"
                                ? "/admin-overview-financing-request"
                                : `/client-overview-financing-request/${response.id}`
                        }`
                    );
                } else {
                    alert("The user details are not valid");
                }
            } catch (error) {
                alert("Invalid request!");
            }
        },
    },
};
</script>

<template>
    <div class="center">
        <img src="../../assets/logo.png" />
        <div id="login" class="center2">
            <span class="p-float-label">
                <InputText
                    id="username"
                    type="text"
                    v-model="username"
                    placeholder="Username"
                />
            </span>

            <span>
                <InputText
                    name="password"
                    type="password"
                    v-model="password"
                    placeholder="Password"
                />
            </span>

            <div class="center" style="top: 120%">
                <Button @click="authenticate()" label="Login"></Button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.center {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, 0%);
    padding: 10px;
}

.center2 {
    position: absolute;
    left: 50%;
    top: 100%;
    transform: translate(-50%, 0%);
    padding: 10px;
}
</style>