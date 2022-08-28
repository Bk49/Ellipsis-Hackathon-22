import { createApp } from 'vue'
import App from './App.vue'
import Router from "./router"
import PrimeVue from 'primevue/config'

import Button from 'primevue/button'
import Card from 'primevue/card';
import InputText from 'primevue/inputtext'
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Row from 'primevue/row';  
import InputNumber from 'primevue/inputnumber'

import './assets/main.css'
import VueNavigationBar from "vue-navigation-bar";

const app = createApp(App)
app.use(Router)
app.use(PrimeVue)

app.component('Button', Button)
app.component('Card', Card)
app.component('InputText', InputText)
app.component('InputNumber', InputNumber)
app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('ColumnGroup', ColumnGroup)
app.component('Row', Row)


app.mount('#app')

import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"
