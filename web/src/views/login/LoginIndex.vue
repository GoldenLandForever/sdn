<template>
    <div class="container">
     <div class="row justify-content-md-center">
            <div class="col-3">
                <div class="title">福州大学校园网络管理后台</div>
                <form @submit.prevent="login" class="login">
                    <div class="mb-3">
                        <label for="username" class="form-label">用户名</label>
                        <input v-model="username" type="text" class="form-control" id="username" placeholder="请输入用户名">
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">密码</label>
                        <input v-model="password" type="password" class="form-control" id="password" placeholder="请输入密码">
                    </div>
                    <div class="error-message">{{ error_message }}</div>
                    <router-link type="submit" class="nav-link login2" :to="{name:'topo_index'}">立即登录</router-link>
                </form>
            </div>
        </div>
    </div>
</template>
<script>

</script>
<style>
.justify-content-md-center{
    padding-right: 275px;
    margin-top: 200px;
}
.title{
    margin-right: 500px;
    background-color: rgb(189,49,36);
    width: 500px;
    height: 100px;
    color: aliceblue;
    font-family: 楷体;
    font-size: 30px;
    text-align: center;
    line-height: 100px;
}
.login{
    width: 500px;
    height: 300px;
    border-color: rgb(189,49,36);
    border-radius: 5px;
    border-style:solid;
}
.form-control{
    width: 300px;
}
.login2{
    border-radius: 25px;
    margin-top: 50px;
    margin-left: 150px;
    width: 200px;
    height: 50px;
    background-color: rgb(189,49,36);
    text-align: center;
    line-height: 50px;
    color: aliceblue;
    font-family: 楷体;
    font-size: 25px;
}
</style>