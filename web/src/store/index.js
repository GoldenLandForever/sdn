import { createStore } from 'vuex'
import ModuleTopo from './topo'
import ModuleInternet from './Internet'
import ModuleFlow from './flow'
export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    flow:ModuleFlow,
    internet:ModuleInternet,
    topo:ModuleTopo
  }
})
