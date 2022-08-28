<script>
export default {
    data() {
        return {
            financing_company_id: this.$route.params.financing_company_id,
            finance_request_id: this.$route.params.finance_request_id,
        };
    },
    methods: {
        async sendRequest() {
            try {
                const requestOptions = {
                    method: "PUT",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        paid_amount: parseFloat(this.paid_amount),
                        finance_request_id: parseFloat(this.finance_request_id),
                        status:"Approve"
                    }),
                };
                let response = await fetch(
                    `http://127.0.0.1:5001/finance_request/${this.financing_company_id}`,
                    requestOptions
                );
                const data = await response.json();
                this.$router.push(`/client-overview-financing-request/${this.financing_company_id}`)
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
            <InputText
                id="paid_amount"
                v-model="paid_amount"
                type="number"
                placeholder="Amount Paid"
            />
            <div>
                <Button v-on:click="sendRequest()">Submit</Button>
            </div>
        </form>
    </div>
</template>

<style>
</style>