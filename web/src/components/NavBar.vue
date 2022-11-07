<template>
    <nav class="navbar fixed-top">
    <div class="container-fluid">
      <button class="btn btn-light" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasNavbarLabel">福州大学校园网络管理后台</h5>
          <button type="button " class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <div class="user-photo">
             <img src="https://img-blog.csdnimg.cn/5b13c6b34fa349f79aa9abca0fea691d.jpeg" alt="">          
          </div>
          <div class="user-username">
            admin
          </div>
          <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
            <li class="nav-item" data-bs-dismiss="offcanvas">
              <router-link  class="nav-link" :to="{name:'topo_index'}">拓扑管理</router-link> 
            </li>
            <li class="nav-item" data-bs-dismiss="offcanvas">
                <router-link  class="nav-link" :to="{name:'flow_index'}" >流规则管理</router-link> 
            </li>
            <li class="nav-item" data-bs-dismiss="offcanvas">
                <router-link  class="nav-link" :to="{name:'internet_index'}" >网络管理</router-link> 
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
  .offcanvas{
    background-color:rgb(189,49,36);
  }
  div.user-photo > img{
      margin: 0 120px;
      border-radius: 50%;
      width: 15vh;
  }
  .offcanvas-title{
      margin-left: 25px;
      text-align: center;
      font-size: 24px;
      font-weight: 600;
      color: aliceblue;
      padding-top: 2vh;
      font-family: 楷体;
  }
  div.user-username{
      text-align: center;
      font-size: 24px;
      font-weight: 600;
      color: aliceblue;
      padding-top: 2vh;
  }
  .nav-link{
      text-align: center;
      font-size: 24px;
      font-weight: 600;
      color: aliceblue;
      padding-top: 2vh;
      font-family: 楷体;
      border-color: aliceblue;
    border-width: 5px;
  }
  .nav-item{
    margin: 5px;
    border-style:inset;
    border-color: aliceblue;
    border-width: 3px;
  }
  </style>