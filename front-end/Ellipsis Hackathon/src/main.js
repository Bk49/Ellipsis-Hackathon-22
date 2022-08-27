import { createApp } from 'vue'
import App from './App.vue'
import Router from "./router"
import PrimeVue from 'primevue/config'

import Button from 'primevue/button'
import Card from 'primevue/card';
import InputText from 'primevue/inputtext'

import './assets/main.css'

const app = createApp(App)
app.use(Router)
app.use(PrimeVue)

app.component('Button', Button)
app.component('PVCard', Card)
app.component('InputText', InputText)

app.mount('#app')

import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"
