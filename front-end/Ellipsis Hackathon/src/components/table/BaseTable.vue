<script>
export default {
    props: {
        tableName: String,
        tableHeader: Array,
        tableData: Array,
        buttonRef: String,
    },
};
</script>

<template>
    <div class="center">
        <div class="content-section implementation">
            <div class="card">
                <DataTable :value="tableData">
                    <h5>{{ tableName }}</h5>
                    <Column
                        v-for="col of tableHeader"
                        :field="col.field"
                        :header="col.header"
                        :key="col.field"
                    >
                    </Column>
                </DataTable>
            </div>
        </div>
    </div>
</template>