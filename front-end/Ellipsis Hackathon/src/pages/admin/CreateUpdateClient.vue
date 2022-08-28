<script >
export default {
    data() {
        return {
            id: this.$route.params.id,
        };
    },

    methods: {
        async submitForm() {
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
                    "http://127.0.0.1:5001/user",
                    requestOptions
                ).then((res) => res.json());

                if (response.status_code === 200) {
                    alert("Submission Successful!");
                    this.$router.push("/list-client");
                } else {
                    alert("Unable to submit form, there are missing values");
                }
            } catch (error) {
                alert("Submit form request error!");
            }
        },
    },
};
</script>

<template>
    <div>
        <Card>
            <template #title> {{ paramNo ? "Edit" : "Add" }} Client </template>
            <template #content>
                <div class="grid p-fluid">
                    <div class="col-12 md:col-4">
                        <div class="p-inputgroup">
                            <InputText
                                placeholder="Client Username"
                                name="username"
                                type="number"
                                v-model="username"
                            />
                        </div>
                    </div>
                    <div class="col-12 md:col-4">
                        <div class="p-inputgroup">
                            <InputText
                                placeholder="Password"
                                name="password"
                                type="text"
                                v-model="password"
                            />
                        </div>
                    </div>
                </div>
            </template>
            <template #footer>
                <Button label="Submit" @click="submitForm()" />
            </template>
        </Card>
    </div>
</template>

<style scoped>
</style>