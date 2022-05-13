import { createRouter, createWebHistory } from "vue-router";
import ElementLogin from "@/components/ElementLogin.vue";
import ElementRegister from "@/components/ElementRegister.vue";
import ElementHome from "@/components/ElementHome.vue";

const routes = [
  {
    path: "/",
    name: "EleLogin",
    component: ElementLogin,
  },
  {
    path: "/register",
    name: "EleRegister",
    component: ElementRegister,
  },
  {
    path: "/home",
    name: "EleHome",
    component: ElementHome,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
