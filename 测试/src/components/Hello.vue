<template>
  <div class="hello">
    <p v-for =(x, index) in datas>{{index+1}}、{{x.acr013}}</p>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      datas: []
    }
  },
  created () {
  	this.$http.jsonp('http://shfp1017.org.cn/shfp/ajaxpagequery/zc/z004/getfpzhongchouList', {'pageSize': '5', 'pageIndex': 1, 'acr012': ''}).then(function (e) {
    	this.datas = e.data.result.pageresult.data
    	console.log(e.data.result.pageresult.data)
    }, function (e) {
      console.log(e)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
