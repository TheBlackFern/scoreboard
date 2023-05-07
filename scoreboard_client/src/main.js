import { createApp } from 'vue'
import App from './App.vue'

import axios from 'axios'

createApp(App).mount('#app')
export default ({ Vue }) => {
    Vue.prototype.$axios = axios;
}