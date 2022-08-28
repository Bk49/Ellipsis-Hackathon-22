<script>
export default {
    data() {
        return {
            users: [],
        };
    },
    mounted() {
        fetch("http://127.0.0.1:5001/user", {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        })
            .then(async (res) => {
                const { users } = await res.json(); // const finance_request = await res.json().finance_request
                this.users = users;
                console.log(users)
            })
            .catch((err) => console.log(err));
    },
    methods: {
        linkToUpdate(id) {
            return this.$router.push(`/edit-client/${id}`);
        },
        async deleteUser(id) {
            try {
                const requestOptions = {
                    method: "DELETE",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ id: id }),
                };
                const res = await fetch(
                    "http://127.0.0.1:5001/user",
                    requestOptions
                ).then((res) => res.json());
                if (res) alert("Successfully deleted user");
                this.$router.link("/list-client");
            } catch (err) {
                alert("Unable to perform delete!");
            }
        },
    },
};
</script>

<template>
    <div>
        <h1>Overview of all Financing Request (Admin)</h1>
        <div class="center">
            <div class="content-section implementation">
                <div class="card">
                    <DataTable :value="users">
                        <Column header="Client Name" field="username" />
                        <Column header="Action">
                            <template #body="{ data }">
                                <Button
                                    label="Edit"
                                    @click="linkToUpdate(data.id)"
                                />
                                <Button
                                    class="p-button-danger"
                                    label="Delete"
                                    @click="deleteUser(data.id)"
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