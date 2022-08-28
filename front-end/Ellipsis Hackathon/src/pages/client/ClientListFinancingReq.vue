<script>
export default {
    data() {
        return {
            finance_requests: [],
            client_id: this.$route.params.id,
        };
    },
    mounted() {
        console.log(this.client_id)
        fetch(`http://127.0.0.1:5001/finance_request/${this.client_id}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        })
            .then(async (res) => {
                const { finance_requests } = await res.json(); // const finance_request = await res.json().finance_request
                this.finance_requests = finance_requests;
                console.log(finance_requests);
            })
            .catch((err) => console.log(err));
    },
    methods: {
        updateFinancing(id) {
            this.$router.push({
                path: `/update-financing-request/${this.client_id}/${id}`,
            });
        },
    },
};
</script>

<template>
    <div>
        <h1>Overview of all Financing Request (Client)</h1>
        <div class="center">
            <div class="content-section implementation">
                <div class="card">
                    <DataTable :value="finance_requests">
                        <Column header="Interest Rate" field="interest_rate" />
                        <Column
                            header="Amount Requested"
                            field="request_amount"
                        />
                        <Column header="Debt Returned" field="paid_amount" />
                        <Column header="Status" field="status" />
                        <Column header="Action">
                            <template #body="{ data }">
                                <Button
                                    :disabled="data.status !== 'Approve'"
                                    label="Update"
                                    @click="updateFinancing(data.id)"
                                />
                            </template>
                        </Column>
                    </DataTable>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>