<script>
</script>


<script>
import BaseTable from "../../components/table/BaseTable.vue";
export default {
  //   props: {

  //   },
  data() {
    return {
      finance_requests: [],
      tableHeader: [
        { header: "Interest Rate", field: "interest_rate" },
        { header: "Amount Requested", field: "request_amount" },
        { header: "Debt Collection/Returned", field: "paid_amount" },
        { header: "Status of Loan", field: "status" },
      ],
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
  components: {
    BaseTable,
  },
};
</script>

<template>
  <div>
    <h1>Overview of all Financing Request (Client)</h1>
    <BaseTable
      tableName="Financing Requests (Admin)"
      :tableHeader="tableHeader"
      :tableData="finance_requests"
    />
  </div>
</template>

<style scoped>
</style>