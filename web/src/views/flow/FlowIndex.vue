<template>
    <div class="container">
  <div class="row align-items-start">
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(1)">查看当前拓扑图</button>
    </div>
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(2)">查看拓扑中的交换机与流表</button>
    </div>
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(3)">添加流表项</button>
    </div>
    <div class="col-5">
      <div class="myGround">
          <div  id="main" style="margin-top: 0%; height: 500px;"></div>
        </div>
    </div>
  </div>
  <div class="row align-items-center">
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(4)">以文件形式提交流表项</button>
    </div>
    <div class="col">
      <button type="button" class="btn btn-danger"  @click="modelchange(5)">删除指定交换机的所有流表</button>
    </div>
    <div class="col">
      <button type="button" class="btncantsee">你看不见我看不见我</button>
    </div>
    
    <div class="col-5"></div>
  </div>
  <div class="row">
    <div class="OperationHead">操作面板</div>
    <!-- 
        以下为model1
     -->
     <div class="OperationBody" v-if="model_change == 1">
        <div class="result">
            请选择上方操作
        </div>
    </div>
    <!-- 
        以下为model2
     -->
    <div class="OperationBody" v-if="model_change == 2">
        <div class="result">
            dpid
        </div>
        <div>
            <button type="button" class="btn btn-info">dpid1</button>
        </div>
        <div>
            <button type="button" class="btn btn-info">dpid2</button>
        </div>
        <div class="result">
            当前拓扑共有:2台交换机
        </div>
      <button type="button" class="btn btn-success">刷新</button>
      <button type="button" class="btn btn-success">返回</button>
    </div>
    <!-- 
        以下为model3
     -->
     <div class="OperationBody" v-if="model_change == 3">
        <div class="result">
            dpid
        </div>
        <div class="input-group input-group-lg">
          <input type="text" placeholder="请以json形式输入流表..." class="form-control text_input" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
        </div>
      <button type="button" class="btn btn-success">提交</button>
    </div>
     <!-- 
        以下为model4
     -->
     <div class="OperationBody" v-if="model_change == 4">
        <div class="result">
            请上传JSON文件
        </div>
        <div class="input-group mb-3">
        <input type="file" class="form-control" id="inputGroupFile02">
        <label class="input-group-text" for="inputGroupFile02">Upload</label>
        </div>
      <button type="button" class="btn btn-success">提交</button>
    </div>
     <!-- 
        以下为model5
     -->
     <div class="OperationBody" v-if="model_change == 5">
        <div class="result">
            dpid
        </div>
        <div>
            <button type="button" class="btn btn-info">dpid1</button>
        </div>
        <div>
            <button type="button" class="btn btn-info">dpid2</button>
        </div>
        <div class="result">
            当前拓扑共有:2台交换机
        </div>
      <button type="button" class="btn btn-success">刷新</button>
      <button type="button" class="btn btn-success">返回</button>
    </div>
  </div>
</div>
</template>
<script>
import { onMounted } from "vue";
import * as echarts from 'echarts';
import store from "@/store";
import { ref } from 'vue';
  export default{
    setup() {
      let model_change = ref(1);
      let option = {
        series: [
          {
            type: 'graph',
            layout: 'force',
            animation: false,
            roam: true,
            label: {
              show: true
            },
            data: store.state.topo.data,
            force: {
              // initLayout: 'circular'
              // gravity: 0
              repulsion: 100,
              edgeLength: 100
            },
            edges: store.state.topo.edges
          }
        ]
      };
      onMounted(() => {
        let myChart1 = echarts.init(document.getElementById("main"));
        myChart1.setOption(option);
  
      })
      const modelchange = (index) =>{
        model_change.value = index;
        console.log(model_change.value);
      }
      return{
        model_change,
        modelchange,
      }
    }
  }
</script>
<style scoped>
div.row{
    padding-top: 100px;
    height: 75px;
    margin-top: 5px;
}
.btn{
  font-weight: 400;
  font-size: 20px;
  font-family: 楷体;
  width: 190px;
  height: 75px;
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
  height: 300px;
  border-radius: 5px;
  border-style:solid;
}
.input-group{
  padding-top: 25px;
}
.btn-info{
    margin: 5px;
    width: 200px;
    height: 50px;
}
.btn-success{
  margin: 5px;
  width: 100px;
  height: 50px;
}
.result{
    margin: 5px;
    font-size: 20px;
    font-weight: 200;
    font-family: 楷体;
}
.btncantsee{
    visibility: hidden !important;
}
div.myGround {
    border-radius: 2%;
    width: 500px;
    height: 500px;
    background-color:aliceblue;
}
.text_input{
  height: 150px;
  width: 400px; 
}
</style>