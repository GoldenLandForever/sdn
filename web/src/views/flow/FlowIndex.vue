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
        <div v-if="showdata == 0">
          <button v-for="index in $store.state.topo.switchname" :key="index" type="button" class="btn btn-info" @click="showflow(index)">{{index}}</button>
        </div>
        <div v-if="showdata == 1" >
          <div class="indexname">{{indexname}}中有{{cnt}}条流表</div>
          <div style="width: 700px;height: 200px;overflow-x:hidden;">
          <div v-for="(data,index) in datas" :key="data">
            <div v-if="data != null" class="flow_title">第{{index}}条流表</div>
            <div class="flow_content">{{data}}</div>
          </div>            
        </div>
        </div>
        <div class="result">
            当前拓扑共有:{{$store.state.topo.switchname.length}}台交换机
        </div>
      <button type="button" class="btn btn-success" @click="flushflow">刷新</button>
      <button type="button" class="btn btn-success" @click="back">返回</button>
    </div>
    <!-- 
        以下为model3
     -->
     <div class="OperationBody" v-if="model_change == 3">
        <form @submit.prevent="addflow">
        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">switchname</span>
          <input v-model="switchname" type="text" class="form-control" placeholder="例如:s1" aria-label="Username" aria-describedby="basic-addon1">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">priority</span>
          <input v-model="priority" type="text" class="form-control" placeholder="例如:1" aria-label="Username" aria-describedby="basic-addon1">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">match</span>
          <input v-model="match" type="text" class="form-control" placeholder="" aria-label="Username" aria-describedby="basic-addon1">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">actions</span>
          <input v-model="actions" type="text" class="form-control" placeholder="" aria-label="Username" aria-describedby="basic-addon1">
        </div>
        <button type="submit" class="btn btn-success">提交</button>
      </form>
    </div>
     <!-- 
        以下为model4
     -->
     <div class="OperationBody" v-if="model_change == 4">
        <div class="result">
            请上传JSON文件
        </div>
        <div class="input-group mb-3">
        <input type="file" class="form-control" id="inputGroupFile02" @change="getFiles($event)"/>
        <label class="input-group-text" for="inputGroupFile02">Upload</label>
        </div>
      <button class="btn btn-success" @click="fileflow()">提交</button>
    </div>
     <!-- 
        以下为model5
     -->
     <div class="OperationBody" v-if="model_change == 5">
      <div >
          <button v-for="index in $store.state.topo.switchname" :key="index" type="button" class="btn btn-danger btn-delete" @click="deleteflow(index)">{{index}}</button>
        </div>
        <div class="result">
            当前拓扑共有:{{$store.state.topo.switchname.length}}台交换机
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
import $ from 'jquery';
  export default{
    setup() {
      let switchname = ref('');
      let priority = ref();
      let match = ref('');
      let actions = ref('');
      let model_change = ref(1);
      let showdata = ref(0);
      let indexname = ref('');
      let cnt = ref(0);
      let datas = [];
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
      const back = () =>{
        showdata.value = 0;
      }
      const flushflow = () => {
        showdata.value = 0;
      }
      const deleteflow = (index) => {
        $.ajax({
              url: "http://127.0.0.1:5000/delete/flow/" + index,
              type: "POST",
              async: false,
              success: function (data) {
                console.log(data);
              },
              error: function (text) {
                  console.log(text);
                  return;
              }
          });
      }
      const showflow = (index) => {
        for (var key in datas) {
	        datas[key] = null;
        }
        cnt.value = 0;
        $.ajax({
              url: "http://127.0.0.1:5000/get/switch/" + index,
              type: "GET",
              async: false,
              success: function (data) {
                for(let i in data){
                  datas[i - 1] = data[i];
                  cnt.value += 1;
                }

              },
              error: function (text) {
                  console.log(text);
                  return;
              }
          });
        indexname.value = index;
        showdata.value = 1;
      }
      var flow_json2 = {};
      const getFiles = (e) => {
          let reader = new FileReader();
          // var flow_json = {};
          reader.readAsBinaryString(e.target.files[0])
          reader.onload = ev => {
            console.log(typeof(ev.target.result));
            flow_json2 = ev.target.result;
            console.log(typeof(flow_json2));
        }
      }
      const fileflow = () => {
        $.ajax({
              url: "http://127.0.0.1:5000/add/flow",
              type: "POST",
              data: JSON.stringify(flow_json2),
              dataType: "json",
              async: false,
              contentType: "application/json", //必须这样写POST   还要加JSON.stringify()    
              success: function (data) {
                  console.log(data);
              },
              error: function (text) {
                  console.log(text);
              }
          });
      }

      const addflow = () => {
        var flow_json = {
          'switchname':switchname.value,
          'priority':priority.value,
          'match':match.value,
          'actions':actions.value
        }
        $.ajax({
              url: "http://127.0.0.1:5000/add/flow",
              type: "POST",
              data: JSON.stringify(flow_json),
              dataType: "json",
              async: false,
              contentType: "application/json", //必须这样写POST   还要加JSON.stringify()    
              success: function (data) {
                  console.log(data);
              },
              error: function (text) {
                  console.log(text);
              }
          });
        switchname.value = '';
        priority.value = '';
        match.value = '';
        actions.value = '';
      }
      onMounted(() => {
        let myChart1 = echarts.init(document.getElementById("main"));
        myChart1.setOption(option);
  
      })
      const modelchange = (index) =>{
        
        model_change.value = index;
      }
      return{
        switchname,
        match,
        priority,
        actions,
        model_change,
        modelchange,
        addflow,
        showflow,
        showdata,
        datas,
        indexname,
        back,
        cnt,
        deleteflow,
        getFiles,
        fileflow,
        flushflow
      }
    },
    methods: {
      // getFiles(e){
      //     console.info(e.target.files[0]);
      //     let reader = new FileReader();
      //     var flow_json = {};
      //     reader.readAsBinaryString(e.target.files[0])
      //     reader.onload = ev => {
      //       console.log(ev.target.result);
      //       flow_json = ev.target.result;
      //       $.ajax({
      //         url: "http://127.0.0.1:5000/add/flow",
      //         type: "POST",
      //         data: JSON.stringify(flow_json),
      //         dataType: "json",
      //         async: false,
      //         contentType: "application/json", //必须这样写POST   还要加JSON.stringify()    
      //         success: function (data) {
      //             console.log(data);
      //         },
      //         error: function (text) {
      //             console.log(text);
      //         }
      //     });
      //     }

      // }
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
  height: 400px;
  border-radius: 5px;
  border-style:solid;
}
.input-group{
  padding-top: 5px;
}
.btn-info{
    margin: 5px;
    width: 200px;
    height: 50px;
}
.btn-delete{
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
.indexname{
  font-size: 25px;
  font-weight: 400;
  font-family: 楷体;
}
.flow_title{
  font-weight: 600;
  background-color:azure;
}
.flow_content{
  background-color:beige;
}
</style>