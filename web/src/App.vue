<template>
  <nav class="navbar fixed-top">
  <div class="container-fluid">
    <button class="btn btn-light" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
      <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="offcanvasNavbarLabel">管理后台</h5>
        <button type="button " class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="offcanvas-body">
        <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">拓扑管理</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">流规则管理</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link" href="#" >
              网络管理
            </a>
          </li>
        </ul>
      </div>
    </div>
    <a class="navbar-brand" href="#">福州大学校园网络管理后台</a>
  </div>
</nav>
</template>
<script>
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap/dist/js/bootstrap"  
export default{
  name:"App",
  setup:() =>{

  }
}
</script>
<style scoped>
.navbar-brand{
  color: aliceblue;
  font-weight: 500;
  font-family: 楷体;
}
.navbar{
  background-color:rgb(189,49,36);
}
</style>