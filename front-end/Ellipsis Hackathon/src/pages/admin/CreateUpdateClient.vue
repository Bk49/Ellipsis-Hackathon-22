<script >
export default {
    props: {
        paramNo: Number,
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
                    query: {
                        financing_company_id: paramNo,
                    },
                };
                const response = await fetch(
                    "http://127.0.0.1:5001/finance_request/",
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
                                placeholder="Request Amount"
                                name="request_amount"
                                type="number"
                                v-model="request_amount"
                            />
                        </div>
                    </div>
                    <div class="col-12 md:col-4">
                        <div class="p-inputgroup">
                            <InputText
                                placeholder="Interest Rate"
                                name="interest_rate"
                                type="text"
                                v-model="interest_rate"
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