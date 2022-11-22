<template>
<div class="container">
  <div class="row align-items-start">
      <div class="col-7">
        <div class="OperationHead">操作面板</div>
        <form @submit.prevent="ping">
        <div class="OperationBody">
          <div class="result">
            <img src="@/assets/host.png" class="hostpic"/>
            <img src="@/assets/jiantou.png " class="jiantou"/>
            <img v-if="$store.state.internet.text1 == 0" src="@/assets/x.png" class="x"/>
            <img src="@/assets/host.png" class="hostpic"/>
        </div>
        <div class="result">
            <text class="result1">链路带宽:</text>
            <text class="result2">{{$store.state.internet.text2}}</text>
        </div>
        <div class="result">
            <text class="result1">链路时延:</text>
            <text class="result2">{{$store.state.internet.text3}}</text>
        </div>
          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon1">请输入要测试的主机名1</span>
            <input v-model="hostname1" type="text" class="form-control" placeholder="例如:h1" aria-label="Username" aria-describedby="basic-addon1">
          </div>

          <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon1">请输入要测试的主机名2</span>
            <input v-model="hostname2" type="text" class="form-control" placeholder="例如:h3" aria-label="Username" aria-describedby="basic-addon1">
          </div>
          <button type="submit" class="btn btn-success">进行测量</button>
        </div>
      </form>
      </div>
      <div class="col-5">
        <div class="myGround">
          <div id="main" style=" height: 500px;"></div>
        </div>
      </div>
    </div>
  <div class="row"></div>
  <div class="row"></div>
</div>
</template>
<script>
import { onMounted } from "vue";
import * as echarts from 'echarts';
import store from "@/store";
import { ref } from 'vue';
import $ from 'jquery'; 
  export default{
    setup(){
      let hostname1 = ref('');
      let hostname2 = ref('');
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
      const ping = () => {
        var flag = 0;
        for (let index = 0; index < store.state.topo.hostname.length; index++) {
          const element = store.state.topo.hostname[index];
          if(element == hostname1.value) flag ++;
          if(element == hostname2.value) flag ++;
        }
        if (flag != 2){
          return;
        }
        var  hostname_json = {
          'node1':hostname1.value,
          'node2':hostname2.value,
        }
        console.log(store.state.internet.text1);
        $.ajax({
            url: "http://127.0.0.1:5000/net/linkStatues",
            type: "POST",
            data: JSON.stringify(hostname_json),
            dataType: "json",
            async: false,
            contentType: "application/json", //必须这样写POST   还要加JSON.stringify()    
            success: function (data) {
                console.log(data);
                store.state.internet.text1 =  data.linkStatus;
                store.state.internet.text2 =  data.bandwidth;
                store.state.internet.text3 =  data.RTT;
            },
            error: function (text) {
                console.log(text);
                return;
            }
        });
        console.log(store.state.internet.text1);
        hostname1.value = '';
        hostname2.value = '';
      }
      onMounted(() => {
        let myChart1 = echarts.init(document.getElementById("main"));
        myChart1.setOption(option);
      })
      return{
        hostname1,
        hostname2,
        option,
        onMounted,
        ping,
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
  height: 600px;
  border-radius: 5px;
  border-style:solid;
}
.input-group{
  padding-top: 15px;
}
.btn-success{
  font-size: 20px;
  margin-left: 500px;
  width: 120px;
  height: 50px;
  font-family: 楷体;
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
div.myGround {
    border-radius: 2%;
    width: 500px;
    height: 500px;
    background-color:aliceblue;
  }

.input-group{
  margin: 5px;
  width: 400px;
}
.jiantou{
  width: 250px;
  height: 150px;
  margin: 0 50px;
}
.x{
  position: absolute;
  width: 12vh;
  top: 185px;
  left: 450px;
}
</style>