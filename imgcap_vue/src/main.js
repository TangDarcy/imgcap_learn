import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementPlus from "element-plus";
import "element-plus/theme-chalk/index.css";
// import axios from 'axios';
// import VueAxios from 'vue-axios';

const app = createApp(App);
// app.prototype.$axios = axios;
// app.prototype.qs = qs;
app.use(store).use(router).use(ElementPlus).mount("#app");
// router.beforeEach((to, from, next) => {
//   // 如果即将进入的路由对象是登录页，则进行跳转，否则验证是否携带accessToken,如果有，则进
//   // 行跳转，没有，则不允许跳转
//   if (to.path === "/") {
//     next();
//   } else {
//     if (sessionStorage.getItem("accessToken")) {
//       next();
//     } else {
//       next("/");
//     }
//   }
// });
