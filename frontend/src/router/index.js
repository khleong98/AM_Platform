import { createRouter, createWebHistory } from 'vue-router';
import UserReferral from '../views/userReferral.vue';
import UserDetail from '../views/userDetail.vue';

const routes = [
  // Your existing routes...
  {
    path: '/referral',
    name: 'UserReferral',
    component: UserReferral,
  },
  {
    path: '/detail',
    name: 'UserDetail',
    component: UserDetail,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
