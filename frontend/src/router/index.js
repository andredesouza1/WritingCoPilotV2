import { createRouter, createWebHistory } from "vue-router";

import Home from "../views/Home.vue";
import CreateArticle from "../views/CreateArticle.vue";
import ViewArticle from "../views/ViewArticle.vue";
import TestView from "../views/TestView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/create-article",
    name: "CreateArticle",
    component: CreateArticle,
  },
  {
    path: "/view-article/",
    name: "ViewArticle",
    component: ViewArticle,
  },
  {
    path: "/test-view",
    name: "TestView",
    component: TestView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
