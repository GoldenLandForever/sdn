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
      <div class="row">
        <div class="col-8">
          <button id="but2" class="btn btn-primary xuuxxi" @click="addSwitch">添加交换机</button>
          <div class="alert alert-primary" role="alert" style="margin-left: 20px">
            {{linkInfo}}
          </div>
          <button id="but3" class="btn btn-primary xuuxxi" @click="addLink">确定</button>
        </div>
      </div>
      <div class="row">
          <div id="main" style=" height: 600px;"></div>
        </div>
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
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入要添加的主机名</span>
        <input type="text" class="form-control" placeholder="例如:h1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入ip</span>
        <input type="text" class="form-control" placeholder="例如:192.168.3.9" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入默认连接的交换机</span>
        <input type="text" class="form-control" placeholder="例如:S1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <button type="button" class="btn btn-success">确定</button>
    </div>

    <!-- 
      以下为model5
      -->
      <div class="OperationBody" v-if="model_change == 5">
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入要添加的主机（交换机）名</span>
        <input type="text" class="form-control" placeholder="例如:h1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入与之连接的要添加的主机（交换机）名</span>
        <input type="text" class="form-control" placeholder="例如:S2" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <button type="button" class="btn btn-success">确定</button>
    </div>
    <!-- 
      以下为model6
      -->
      <div class="OperationBody" v-if="model_change == 6">
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入要添加的交换机名</span>
        <input type="text" class="form-control" placeholder="例如:S1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <button type="button" class="btn btn-success">确定</button>
    </div>
      <!-- 
      以下为model7
      -->
      <div class="OperationBody" v-if="model_change == 7">
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入要删除的主机</span>
        <input type="text" class="form-control" placeholder="例如:h1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <button type="button" class="btn btn-success">确定</button>
    </div>
      <!-- 
      以下为model8
      -->
      <div class="OperationBody" v-if="model_change == 8">
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入要删除的主机（交换机）名</span>
        <input type="text" class="form-control" placeholder="例如:h1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入与之连接的要删除的主机（交换机）名</span>
        <input type="text" class="form-control" placeholder="例如:S2" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <button type="button" class="btn btn-success">确定</button>
    </div>
      <!-- 
      以下为model9
      -->
      <div class="OperationBody" v-if="model_change == 9">
      <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">请输入要删除的交换机名</span>
        <input type="text" class="form-control" placeholder="例如:S1" aria-label="Username" aria-describedby="basic-addon1">
      </div>
      <button type="button" class="btn btn-success">确定</button>
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
  export default{
    setup() {
      let model_change = ref(1);
      const modelchange = (index) =>{
        if(index == 4) addHost();
        if(index == 5)
        model_change.value = index;
        console.log(model_change.value);
      }
      const idMap = {};
      let mapCnt = 0;
      let curHost = 0;
      let curSwitch = 0;
  
      let myChart;
  
      const data = [];
      const edges = [];
      let allOption = new Array();
  
      let link1, link2;
      let linkInfo = ref('links ' + link1 + ' & ' + link2);
  
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
            data: data,
            force: {
              // initLayout: 'circular'
              // gravity: 0
              repulsion: 100,
              edgeLength: 100
            },
            edges: edges
          }
        ]
      };
  
      onMounted(() => {
        let myChart1 = echarts.init(document.getElementById("main"));
        myChart1.setOption(option);
  
        myChart = myChart1;
  
        myChart.on('click', function (param) {
          if (param.dataType === 'node') {
            if (link1 === null) link1 = param.data.name;
            else if (link2 === null) link2 = param.data.name;
            else link1 = link2 = null;
  
            linkInfo.value = 'links ' + link1 + ' & ' + link2;
          }
        })
      })
  
      const chk = () => {
        console.log(allOption);
      }
  
      const addHost = () => {
        idMap['h' + curHost] = mapCnt++;
        allOption.push('h' + curHost);
  
        data.push({
          id: data.length + '',
          symbolSize: 40,
          draggable: true,
          name: 'h' + curHost++
        });
  
        myChart.setOption({
          series: [
            {
              roam: true,
              data: data,
              edges: edges
            }
          ]
        });
      }
  
      const addSwitch = () => {
        idMap['s' + curSwitch] = mapCnt++;
        allOption.push('s' + curSwitch);
  
        data.push({
          id: data.length + '',
          symbolSize: 40,
          draggable: true,
          name: 's' + curSwitch++
        });
  
        myChart.setOption({
          series: [
            {
              roam: true,
              data: data,
              edges: edges
            }
          ]
        });
      }
  
      const addLink = () => {
        let pos1 = idMap[link1];
        let pos2 = idMap[link2];
  
        if (pos1 != null && pos2 != null && pos1 != pos2) {
          edges.push({
            source: pos1,
            target: pos2
          });
  
          link1 = link2 = null;
        }
  
        myChart.setOption({
          series: [
            {
              roam: true,
              data: data,
              edges: edges
            }
          ]
        });
      }
  
      return {
        addHost,
        addSwitch,
        addLink,
        chk,
        allOption,
        linkInfo,
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
  .xuuxxi {
    font-weight: 400;
    font-size: 15px;
    font-family: 楷体;
    width: 100px;
    height: 50px;
  }
</style>