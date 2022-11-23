<template>

    <div class="container">
  <div class="row align-items-start">
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(1)" >现有网络拓扑视图</button>
    </div>
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(2)">导入文件生成拓扑</button>
    </div>
    <div class="col">
      <button type="button" class="btn btn-primary" @click="modelchange(3)">建立拓扑</button>
    </div>
    <div class="col-5">
      <div class="myGround">
          <div id="main" style="margin-top: 0%; height: 500px;"></div>
    </div>
    </div>
  </div>
  <div class="row align-items-center">
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(4)">添加主机</button>
    </div>
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(5)">添加链路</button>
    </div>
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(6)">添加交换机</button>
    </div>
    <div class="col-5"></div>
  </div>
  <div class="row align-items-end">
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(7)">删除主机</button>
    </div>
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(8)">删除链路</button>
    </div>
    <div class="col">
      <button type="button" class="btn btn-danger" @click="modelchange(9)">删除交换机</button>
    </div>
    <div class="col-5">
    </div>
  </div>
  
  <div class="row" >
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
            请上传文件
        </div>
        <div class="input-group mb-3">
        <input type="file" class="form-control" id="inputGroupFile02">
        <label class="input-group-text" for="inputGroupFile02">Upload</label>
        </div>
      <button type="button" class="btn btn-success">提交</button>
    </div>
   <!-- 
    以下为model3
   -->
   <div class="OperationBody" v-if="model_change == 3">
        <div class="result">
            这个好难
        </div>
    </div>
    <!-- 
    以下为model4
   -->
    <div class="OperationBody" v-if="model_change == 4">
      <form @submit.prevent="addHost">
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入要添加的主机名</span>
        <input v-model="hostname" type="text" class="form-control" placeholder="例如:h1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入ip</span>
        <input v-model="ipname" type="text" class="form-control" placeholder="例如:192.168.3.9" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入默认连接的交换机</span>
        <input v-model="switchname" type="text" class="form-control" placeholder="例如:S1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <button type="submit" class="btn btn-success">确定</button>
    </form>
    </div>
    <!-- 
      以下为model5
      -->

      <div class="OperationBody" v-if="model_change == 5">
        <form @submit.prevent="addLink">
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入要添加的主机（交换机）名</span>
        <input v-model="link1" type="text" class="form-control" placeholder="例如:h1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入与之连接的要添加的主机（交换机）名</span>
        <input v-model="link2" type="text" class="form-control" placeholder="例如:S2" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <button type="submit" class="btn btn-success">确定</button>
    </form>
    </div>

    <!-- 
      以下为model6
      -->
    
      <div class="OperationBody" v-if="model_change == 6">
        <form @submit.prevent="addSwitch">
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon1">请输入要添加的交换机名</span>
            <input v-model="switchname" type="text" class="form-control" placeholder="例如:S1" aria-label="Username" aria-describedby="basic-addon1">
          </div>
          <button type="submit" class="btn btn-success">确定</button>
        </form>
      </div>

      <!-- 
      以下为model7
      -->

        <div class="OperationBody" v-if="model_change == 7">
          <form @submit.prevent="subhost">
        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">请输入要删除的主机</span>
          <input v-model="hostname" type="text" class="form-control" placeholder="例如:h1" aria-label="Username" aria-describedby="basic-addon1">
        </div>
        <button type="submit" class="btn btn-success">确定</button>
      </form>
      </div>

      <!-- 
      以下为model8
      -->

      <div class="OperationBody" v-if="model_change == 8">
        <form @submit.prevent="rmLink">
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入要删除的主机（交换机）名</span>
        <input v-model="link1" type="text" class="form-control" placeholder="例如:h1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入与之连接的要删除的主机（交换机）名</span>
        <input v-model="link2" type="text" class="form-control" placeholder="例如:S2" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <button type="submit" class="btn btn-success">确定</button>
    </form>
    </div>

      <!-- 
      以下为model9
      -->

        <div class="OperationBody" v-if="model_change == 9">
          <form @submit.prevent="subSwitch">
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon1">请输入要删除的交换机名</span>
            <input v-model="switchname" type="text" class="form-control" placeholder="例如:S1" aria-label="Username" aria-describedby="basic-addon1">
          </div>
          <button type="submit" class="btn btn-success">确定</button>
        </form>
         </div>

  </div>
  

  <div class="row">
    <router-link :to="{name:'login_index'}" class="nav-link logout"> 退出登录</router-link>
  </div>
</div>


</template>
<script>
import { onMounted } from "vue";
import * as echarts from 'echarts';
import { ref } from 'vue';
import store from "@/store";
import $ from 'jquery'; 

  export default{
    setup() {
      let model_change = ref(1);
      const modelchange = (index) =>{
        model_change.value = index;
        if(model_change.value == 3){
          getTopo();
        }
      }
      let hostname = ref('');
      let ipname = ref('');
      let switchname = ref('');
      
      let myChart;
  
      let allOption = new Array();
  
      let link1 = ref(''), link2 = ref('');
  
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
  
        myChart = myChart1;

      })
  
      var chk = 0;
      const getTopo = () => {

        chk = 1;
        store.state.topo.idMap = {};
        store.state.topo.mapCnt = 0;
        store.state.topo.hostname = [];
        store.state.topo.switchname = [];
        store.state.topo.edges = [];
        store.state.topo.data = [];
        $.ajax({
            url: "http://127.0.0.1:5000/topo/default-topo",
            type: "GET",
            dataType: "json",
            async: false,
            contentType: "application/json", //必须这样写POST   还要加JSON.stringify()    
            success: function (data) {
                console.log(data.param);
            },
            error: function (text) {
                console.log(text);
                return;
            }
        });
        for (let index = 1; index <= 5; index++) {
            hostname.value = 'h' + index;
            addHost();
        }
        hostname.value = '';
        for (let index = 1; index <= 3; index++) {
            switchname.value = 's' + index;
            addSwitch();
        }
        switchname.value = '';
        link1.value = 'h2';
        link2.value = 's2';
        addLink();
        link1.value = 'h3';
        link2.value = 's2';
        addLink();
        link1.value = 's1';
        link2.value = 's2';
        addLink();
        link1.value = 's1';
        link2.value = 'h1';
        addLink();
        link1.value = 's1';
        link2.value = 's3';
        addLink();
        link2.value = 's3';
        link1.value = 'h5';
        addLink();
        link2.value = 's3';
        link1.value = 'h4';
        addLink();

        chk = 0;
      }

      const addHost = () => {
        for (let index = 0; index < store.state.topo.hostname.length; index++) {
          const element = store.state.topo.hostname[index];
          if(element == hostname.value) return
        }
        var  hostname_json = {
          'name':hostname.value,
          'ip_address':ipname.value,
          'switch':switchname.value
        }
        if(chk != 1){
          $.ajax({
              url: "http://127.0.0.1:5000/topo/addhost",
              type: "POST",
              data: JSON.stringify(hostname_json),
              dataType: "json",
              async: false,
              contentType: "application/json", //必须这样写POST   还要加JSON.stringify()    
              success: function (data) {
                  console.log(data.param);
              },
              error: function (text) {
                  console.log(text);
                  return;
              }
          });
        }
        store.state.topo.hostname.push(hostname.value);
        store.state.topo.idMap[hostname.value] = store.state.topo.mapCnt++;
        allOption.push(hostname.value);
        
        store.state.topo.data.push({
          id: store.state.topo.mapCnt + '',
          symbolSize: 40,
          draggable: true,
          name: hostname.value,
          symbol: 'image://' + require('../../assets/2.png'),
          label: {
            position: 'bottom',
            formatter: '{b}'
          },
        });

        myChart.setOption({
          series: [
            {
              roam: true,
              data: store.state.topo.data,
              edges: store.state.topo.edges
            }
          ]
        });
        if(switchname.value != ''){
          link1.value = switchname.value;
          link2.value = hostname.value;
          addLink();
          switchname.value = '';
        }
        ipname.value = '';
        hostname.value = '';
      }
      
      const subhost = () => {
          $.ajax({
              url: "http://127.0.0.1:5000/topo/deletehost/" + hostname.value,
              type: "GET",
              dataType: "json",
              async: false,
              contentType: "application/json", //必须这样写POST   还要加JSON.stringify()    
              success: function (data) {
                  console.log(data.param);
              },
              error: function (text) {
                  console.log(text);
                  return;
              }
          });
        for (let index = 0; index < store.state.topo.mapCnt; index++) {
          if(store.state.topo.data[index].name == hostname.value){
            store.state.topo.data[index].symbolSize = 0;
            store.state.topo.data[index].name = '';
          }
        }
        for (let index = 0; index < store.state.topo.hostname.length; index++) {
          const element = store.state.topo.hostname[index];
          if(element == hostname.value){
            store.state.topo.hostname[index] = '';
          }
        }
        let newEdges = [];
        for (var i in store.state.topo.edges) {
          if(store.state.topo.edges[i]["source"] == store.state.topo.idMap[hostname.value]  ||  store.state.topo.edges[i]["target"] == store.state.topo.idMap[hostname.value]) continue;

          newEdges.push(store.state.topo.edges[i]);
        }
        store.state.topo.edges = newEdges;
        myChart.setOption({
          series: [
            {
              roam: true,
              data: store.state.topo.data,
              edges: store.state.topo.edges
            }
          ]
        });
        
        hostname.value = '';
      }

      const addSwitch = () => {
        for (let index = 0; index < store.state.topo.switchname.length; index++) {
          const element = store.state.topo.switchname[index];
          if(element == switchname.value) return
        }
        if(chk != 1){
        $.ajax({
              url: "http://127.0.0.1:5000/topo/addswitch/" + switchname.value,
              type: "GET",
              dataType: "json",
              async: false,
              contentType: "application/json", //必须这样写POST   还要加JSON.stringify()    
              success: function (data) {
                  console.log(data.param);
              },
              error: function (text) {
                  console.log(text);
                  return;
              }
          });
        }
        store.state.topo.switchname.push(switchname.value);
        store.state.topo.idMap[switchname.value] = store.state.topo.mapCnt++;
        allOption.push(switchname.value);
  
        store.state.topo.data.push({
          id: store.state.topo.mapCnt + '',
          symbolSize: 40,
          draggable: true,
          name: switchname.value,
          symbol: 'image://' + require('../../assets/1.png'),
          label: {
            position: 'bottom',
            formatter: '{b}'
          },
        });


        myChart.setOption({
          series: [
            {
              roam: true,
              data: store.state.topo.data,
              edges: store.state.topo.edges
            }
          ]
        });

        switchname.value = '';
      }
      
      const subSwitch = () => {
        $.ajax({
              url: "http://127.0.0.1:5000/topo/deleteswitch/" + switchname.value,
              type: "GET",
              dataType: "json",
              async: false,
              contentType: "application/json", //必须这样写POST   还要加JSON.stringify()    
              success: function (data) {
                  console.log(data.param);
              },
              error: function (text) {
                  console.log(text);
                  return;
              }
          });
        for (let index = 0; index < store.state.topo.mapCnt; index++) {
          if(store.state.topo.data[index].name == switchname.value){
            store.state.topo.data[index].symbolSize = 0;
            store.state.topo.data[index].name = '';
          }
        }

        for (let index = 0; index < store.state.topo.switchname.length; index++) {
          const element = store.state.topo.switchname[index];
          if(element == switchname.value){
            store.state.topo.switchname[index] = '';
          }
        }
        let newEdges = [];
        for (var i in store.state.topo.edges) {
          if(store.state.topo.edges[i]["source"] == store.state.topo.idMap[switchname.value]  ||  store.state.topo.edges[i]["target"] == store.state.topo.idMap[switchname.value]) continue;
          newEdges.push(store.state.topo.edges[i]);
        }
        store.state.topo.edges = newEdges;
        myChart.setOption({
          series: [
            {
              roam: true,
              data: store.state.topo.data,
              edges: store.state.topo.edges
            }
          ]
        });
        
        switchname.value = '';
      }

      const addLink = () => {
        var  Link_json = {
          'node1': link1.value,
          'node2': link2.value,
        }
        if(chk != 1){
          $.ajax({
              url: "http://127.0.0.1:5000/topo/addlink",
              type: "POST",
              data: JSON.stringify(Link_json),
              dataType: "json",
              async: false,
              contentType: "application/json", //必须这样写POST   还要加JSON.stringify()    
              success: function (data) {
                  console.log(data.param);
              },
              error: function (text) {
                  console.log(text);
                  return;
              }
          });
        }
        let pos1 = store.state.topo.idMap[link1.value];
        let pos2 = store.state.topo.idMap[link2.value];
        if (pos1 != null && pos2 != null && pos1 != pos2) {
          store.state.topo.edges.push({
            source: pos1,
            target: pos2
          });
  
          link1.value = link2.value = null;
        }

        myChart.setOption({
          series: [
            {
              roam: true,
              data: store.state.topo.data,
              edges: store.state.topo.edges
            }
          ]
        });
      }

      const rmLink = () => {
        var  Link_json = {
          'node1': link1.value,
          'node2': link2.value,
        }
        if(chk != 1){
          $.ajax({
              url: "http://127.0.0.1:5000/topo/deletelink",
              type: "POST",
              data: JSON.stringify(Link_json),
              dataType: "json",
              async: false,
              contentType: "application/json", //必须这样写POST   还要加JSON.stringify()    
              success: function (data) {
                  console.log(data.param);
              },
              error: function (text) {
                  console.log(text);
                  return;
              }
          });
        }
      let pos1 = store.state.topo.idMap[link1.value];
      let pos2 = store.state.topo.idMap[link2.value];

      let newEdges = [];

      for (var i in store.state.topo.edges) {
        if((store.state.topo.edges[i]["source"] == pos1 && store.state.topo.edges[i]["target"] == pos2) || (store.state.topo.edges[i]["source"] == pos2 && store.state.topo.edges[i]["target"] == pos1)) continue;

        newEdges.push(store.state.topo.edges[i]);
      }

      store.state.topo.edges = newEdges;

      link1.value = '';
      link2.value = '';
      myChart.setOption({
        series: [
          {
            roam: true,
            data: store.state.topo.data,
            edges: store.state.topo.edges
          }
        ]
      });
    }
      return {
        ipname,
        hostname,
        link1,
        link2,
        switchname,
        getTopo,
        subhost,
        addHost,
        addSwitch,
        addLink,
        rmLink,
        subSwitch,
        allOption,
        model_change,
        modelchange,
      }
    }
}

</script>
<style scoped>
.logout{
  margin-top: 200px;
  margin-left: 1250px;
  width: 180px;
  height: 55px;
  background-color: rgb(189,49,36);
  font-family: 楷体;
  font-size: 35px;
  text-align: center;
  color: aliceblue;
}
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
.btn-success{
  margin-left: 580px;
  width: 100px;
  height: 50px;
}
div.myGround {
    border-radius: 2%;
    width: 500px;
    height: 500px;
    background-color:aliceblue;
}
</style>