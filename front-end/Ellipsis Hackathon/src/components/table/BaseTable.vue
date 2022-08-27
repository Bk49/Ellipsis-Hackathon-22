// Take in 2 props (Table header : string array, Table data : Object array)
// const strAryExp = ["hello", "world"];
// const products = [{ 
//     property1: "value of prop1",
//     property2: "value2",
//     property3: "value3"
//  }];
<script>
export default {
  data() {
    return {
      finance_requests: [],
    };
  },
  mounted() {
    fetch("http://127.0.0.1:5001/finance_request/2", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then(async (res) => {
        const { finance_requests } = await res.json(); // const finance_request = await res.json().finance_request
        this.finance_requests = finance_requests;
      })
      .catch((err) => console.log(err));
  },
};
</script>



<script setup>
const table = [
  { header: "Interest Rate", field: "interest_rate" },
  { header: "Amount Requested", field: "request_amount" },

  { header: "Debt Collection/Returned", field: "paid_amount" },
  { header: "Status of Loan", field: "status" },
];
</script>



<template>
  <div class="center">
    <div class="content-section introduction">
      <div class="feature-intro">
        <h1>DataTable</h1>
        <p>DataTable displays data in tabular format.</p>
      </div>
      <AppDemoActions />
    </div>

    <div class="content-section implementation">
      <div class="card">
        <DataTable :value="finance_requests">
          <h5>Your Mum</h5>
          <Column
            v-for="col of table"
            :field="col.field"
            :header="col.header"
            :key="col.field"
          >
          </Column>
        </DataTable>
      </div>
    </div>

    <DataTableDoc />
  </div>
</template>

<style lang="scss" scoped>
::v-deep(.p-paginator) {
  .p-paginator-current {
    margin-left: auto;
  }
}
::v-deep(.p-progressbar) {
  height: 0.5rem;
  background-color: #d8dadc;
  .p-progressbar-value {
    background-color: #607d8b;
  }
}
::v-deep(.p-datepicker) {
  min-width: 25rem;
  td {
    font-weight: 400;
  }
}
::v-deep(.p-datatable.p-datatable-customers) {
  .p-datatable-header {
    padding: 1rem;
    text-align: left;
    font-size: 1.5rem;
  }
  .p-paginator {
    padding: 1rem;
  }
  .p-datatable-thead > tr > th {
    text-align: left;
  }
  .p-datatable-tbody > tr > td {
    cursor: auto;
  }
  .p-dropdown-label:not(.p-placeholder) {
    text-transform: uppercase;
  }
}
</style>