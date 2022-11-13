<template>
    
  </template>
  
  <script >
  
  
  export default {
    setup() {
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
        linkInfo
      }
    }
  }
  </script>
  
  <style scoped>
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