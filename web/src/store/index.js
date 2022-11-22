import { createStore } from 'vuex'
import ModuleTopo from './topo'
import ModuleInternet from './Internet'
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
    internet:ModuleInternet,
    topo:ModuleTopo
  }
})
