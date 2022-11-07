<template>
<div class="container">
    <div class="row">
    <div class="OperationHead">操作面板</div>
    <div class="OperationBody">
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入要测试的主机名1</span>
        <input type="text" class="form-control" placeholder="例如:h1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入要测试的主机名2</span>
        <input type="text" class="form-control" placeholder="例如:h1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <button type="button" class="btn btn-primary">pingall</button>
      <button type="button" class="btn btn-success">确定</button>
    </div>
  </div>
  <div class="row"></div>
  <div class="row"></div>
  <div class="row">
    <div class="OperationHead">测试结果</div>
    <div class="OperationBody">
        <div class="result">
            <text class="result1">主机间的连通性:</text>
            <text class="result2">已连通</text>
        </div>
        <div class="result">
            <text class="result1">链路带宽:</text>
            <text class="result2">10Mbps</text>
        </div>
        <div class="result">
            <text class="result1">链路时延:</text>
            <text class="result2">0.168ms</text>
        </div>
        <button type="button" class="btn btn-danger ">流量异常化警告</button>
      <button type="button" class="btn btn-primary othername">数据可视化</button>
    </div>
  </div>
</div>
</template>
<script>
</script>
<style scoped>
div.row{
    padding-top: 100px;
    height: 75px;
    margin-top: 5px;
}
.OperationHead{
  width:715px;
  height: 40px;
  font-weight: 300;
  font-size: 30px;
  color: rgb(252,202,0);
  font-family: 楷体;
  background-color: rgb(254,252,177);
}
.OperationBody{
  background-color: aliceblue;
  border-color: rgb(254,252,177);
  width: 715px;
  height: 200px;
  border-radius: 5px;
  border-style:solid;
}
.input-group{
  padding-top: 15px;
}
.btn-success{
  font-size: 20px;
  margin-left: 50px;
  width: 100px;
  height: 50px;
  font-family: 楷体;
}
.btn-primary{
    margin-left: 400px;
    width: 100px;
    height: 50px;
    
}
.result{
    padding-top: 15px;
    padding-left: 10px;
}
.othername{
    font-size: 20px;
    margin-left: 50px;
    width: 145px;
    height: 50px;
    font-family: 楷体;
}
.btn-danger{
    font-size: 20px;
    font-family: 楷体;
    margin-left: 300px;
    width: 175px;
    height: 50px;
}
.result1{
    font-family: 楷体;
    font-size: 20px;        
}
.result2{
    margin-left: 50px;
    font-family: 楷体;
    font-size: 20px;     
    color: red;

}
</style>