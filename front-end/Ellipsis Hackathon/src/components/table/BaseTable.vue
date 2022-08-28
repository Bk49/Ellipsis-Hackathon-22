<script>
export default {
  props: {
    tableName: String,
    tableHeader: Array,
    tableData: Array,
  }
}
</script>

<template>
  <div class="center">
    <div class="content-section introduction">
      <div class="feature-intro">
        <h1>DataTable</h1>
        <p>DataTable displays data in tabular format.</p>
      </div>
    </div>

    <div class="content-section implementation">
      <div class="card">
        <DataTable :value="tableData">
          <h5>{{tableName}}</h5>
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