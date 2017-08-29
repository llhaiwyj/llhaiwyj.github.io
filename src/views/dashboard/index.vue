<template>
  <div class="dashboard-container">
    <div class='dashboard-text'><p class="guanli">管理员:</p><p class="ming">{{name}}</p></div>
    <div class='dashboard-text'><p class="qx">权限:</p><p v-for='role in roles' :key='role' class="quanxian">{{role}}</p></div>
    <div class='dashboard-text'><p class="liuru">资金流入(充值):</p><p class="qian"> <b>{{money_in}}</b> 元</p></div>
    <div id="main" style="width:400px;height:300px;"></div>
    <div class='dashboard-text'><p class="liuchu">资金流出(提现):</p> <p class="lqian"><b>{{money_out}}</b> 元</p></div>
    <div id="dier" style="width:400px;height:300px;"></div>
  </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import { money_info } from '@/api/money_info';
     var echarts = require('echarts/lib/echarts');
// 引入柱状图
     require('echarts/lib/chart/bar');
// 引入提示框和标题组件
     require('echarts/lib/component/tooltip');
     require('echarts/lib/component/title');


    export default {
      name: 'dashboard',
      data() {
        return {
          money_in : null,
          money_out : null
        }
      },
      computed: {
        ...mapGetters([
          'name',
          'roles'
        ])
      },
      created() {
        money_info().then(response => {
          console.log(response)
          this.money_in = response.detail.in;
          this.money_out = response.detail.out;
        })
      },
      mounted(){
            var myChart = echarts.init(document.getElementById('main'));
            var myChartOption={
            	title: { text: '' },
                tooltip: {},
                xAxis: {
                    data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
                },
                yAxis: {},
                series: [{
                    name: '销量',
                    type: 'bar',
                    data: [5, 10, 26, 40, 25, 16]
                }]}
            myChart.setOption(myChartOption,true);
            
            
            
            var myCharts = echarts.init(document.getElementById('dier'));
             var myChartOptions={
            	title: { text: '' },
                tooltip: {},
                xAxis: {
                    data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
                },
                yAxis: {},
                series: [{
                    name: '销量',
                    type: 'bar',
                    data: [5, 10, 26, 40, 25, 16]
                }]}
            myCharts.setOption(myChartOptions,true);
        },
     


      
    }
    
    
     
        
</script>

<style>
#main{
	float:left;
}
#dier{
	float:left;
}
.dashboard-container{
	width:600px;
	height:auto;
}	
.dashboard-text{
	width:600px;
	height:50px;
	margin-left:20px;
	margin-top:20px;
	float:left;
}
b{
	font-weight: 200;
	color:red;
}
.guanli{
	width:200px;
	height:50px;
	font-size:20px;
	float:left;
	line-height: 50px;
}
.ming{
	width:300px;
	height:50px;
	font-size:20px;
	float:left;
	line-height: 50px;
}
.qx{
	width:200px;
	height:50px;
	font-size:20px;
	float:left;
	line-height: 50px;
	
}
.quanxian{
	width:300px;
	height:50px;
	font-size:20px;
	float:left;
	line-height: 50px;
	
}
.liuru{
	width:203px;
	height:50px;
	font-size:20px;
	float:left;
	line-height: 50px;

	
}
.qian{
	width:54px;
	height:50px;
	font-size:20px;
	float:left;
	line-height: 50px;
	
}
.liuchu{
	width:203px;
	height:50px;
	font-size:20px;
	float:left;
  line-height: 50px;
 /* margin-top:150px;*/
}
.lqian{
	width:54px;
	height:50px;
	font-size:20px;
	float:left;
	line-height: 50px;
	/*margin-top:150px;*/
}
</style>
