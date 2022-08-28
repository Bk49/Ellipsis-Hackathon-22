<script>
export default {
    data() {
        return {
            user_id: this.$route.params.user_id,
            // finance_request_id: this.$route.params.finance_request_id,
        };
    },
    methods: {
        async sendRequest() {
            try {
                const requestOptions = {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        request_amount: parseFloat(this.request_amount),
                        interest_rate: parseFloat(this.interest_rate),
                    }),
                };
                let response = await fetch(
                    `http://127.0.0.1:5001/finance_request/${this.user_id}`,
                    requestOptions
                );
                const data = await response.json();

                console.log(data.message);
            } catch (error) {
                console.log(error);
            }
        },
    },
};
</script>

<template>
    <div>
        <form>
            <div>
                <InputText
                    id="request_amount"
                    v-model="request_amount"
                    type="number"
                    placeholder="Request Amount"
                />
            </div>
            <InputText
                id="interest_rate"
                v-model="interest_rate"
                type="number"
                placeholder="Interest Rate"
            />
            <div>
                <Button v-on:click="sendRequest()">Submit</Button>
            </div>
        </form>
    </div>
</template>

<style>
</style>