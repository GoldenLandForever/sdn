<template>
  <NavBar/>
  <router-view></router-view>
</template>

<script> 
import NavBar from './components/NavBar.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap/dist/js/bootstrap"  
import "bootstrap/dist/css/bootstrap.css"
// import $ from 'jquery'
export default{
    components:{
      NavBar
    },
    setup() {
    }
  }
</script>
<style scoped>
</style>
