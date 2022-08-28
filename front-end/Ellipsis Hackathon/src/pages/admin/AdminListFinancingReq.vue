<script>
export default {
    data() {
        return {
            finance_requests: [],
        };
    },
    mounted() {
        fetch("http://127.0.0.1:5001/finance_request_list", {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        })
            .then(async (res) => {
                const { finance_requests } = await res.json(); // const finance_request = await res.json().finance_request
                this.finance_requests = finance_requests;
            })
            .catch((err) => console.log(err));
    },
    methods: {
        async changeStatus(isApprove, financing_company_id, id) {
            fetch(
                `http://127.0.0.1:5001/finance_request/${financing_company_id}`,
                {
                    method: "PUT",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        status: isApprove ? "Approve" : "Reject",
                        paid_amount: 0,
                        finance_request_id: id,
                    }),
                }
            ).then(async (res) => {
                await res.json();
                alert("Success");
                this.$router.go(this.$router.currentRoute);
            });
        },
    },
};
</script>

<template>
    <div>
        <h1>Overview of all Financing Request (Admin)</h1>
        <div class="center">
            <div class="content-section implementation">
                <div :key="componentKey" class="card">
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
                                    class="p-button-success"
                                    label="Approve"
                                    @click="
                                        changeStatus(
                                            true,
                                            data.financing_company_id,
                                            data.id
                                        )
                                    "
                                />
                                <Button
                                    class="p-button-danger"
                                    label="Reject"
                                    @click="
                                        changeStatus(
                                            false,
                                            data.financing_company_id,
                                            data.id
                                        )
                                    "
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