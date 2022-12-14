import { createRouter, createWebHistory } from 'vue-router' 
import TOPO from '../views/topo/TopoIndex'
import FLOW from '../views/flow/FlowIndex'
import INTERNET from '../views/internet/InternetIndex'
import Login from '../views/login/LoginIndex'
const routes = [
  {
    path: "/",
    name: "home",
    redirect: "/topo",
  },
  {
    path:"/topo",
    component:TOPO,
    name:"topo_index",
  },
  {
    path:"/flow",
    component:FLOW,
    name:"flow_index",
  },
  {
    path:"/internet",
    component:INTERNET,
    name:"internet_index",
  },
  {
    path:"/login",
    component:Login,
    name:"login_index",
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
