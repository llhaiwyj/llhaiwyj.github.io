<template>
  <div class="app-container">
    <el-table :data="list" v-loading.body="listLoading" element-loading-text="拼命加载中" border fit highlight-current-row>
      <el-table-column align="center" label='ID' width="95">
        <template scope="scope">
         {{scope.$index}} 
        </template>
      </el-table-column>
      <el-table-column label="
      	性别" width="80">
        <template scope="scope">
          {{scope.row.gender}}
        </template>
      </el-table-column>
      <el-table-column label="地区" width="80" align="center">
        <template scope="scope">
          <span>{{scope.row.region}}</span>
        </template>
      </el-table-column>
      <el-table-column label="泡泡号" width="120" align="center">
        <template scope="scope">
          {{scope.row.pp_number}}
        </template>
      </el-table-column>
      <el-table-column label="identify" width="120" align="center">
        <template scope="scope">
          {{scope.row.identify}}
        </template>
      </el-table-column>
      <el-table-column label="绑定手机号" width="180" align="center">
        <template scope="scope">
          {{scope.row.phone}}
        </template>
      </el-table-column>
      <el-table-column label="昵称" width="80" align="center">
        <template scope="scope">
          <el-button type="text" @click=handlerClickBank(scope.row.identify)>{{scope.row.nick_name}} </el-button>
        </template>
      </el-table-column>
      <el-table-column label="头像" width="220" align="center">
        <template scope="scope" id="example" >
          <img :src="scope.row.head_image" style="width:100px;height:100px;" />
        </template>
      </el-table-column>
      <!--<el-table-column align="center" prop="created_at" label="Display_time" width="200">
        <template scope="scope">
          <i class="el-icon-time"></i>
          <span>{{scope.row.display_time}}</span>
        </template>
      </el-table-column>-->
    </el-table>
    <br>
    <el-pagination
      layout="total, prev, pager, next, jumper"
      @current-change="handleCurrentChange"
      :page-size=10
      :total=totals>
    </el-pagination>
  </div>
</template>

<script>
  import { getUserBack } from '@/api/table';
  
  
  export default {
    data() {
    	 aboutData:[]
      return {
        list: null,
        listLoading: true,
        totals: 0, 
      }
    },
    created() {
      this.fetchData({
        page:1
      });
      this.getRoute()
    },
    methods: {
      handleCurrentChange (val) {
        this.fetchData({
          page: val
        })
      },
      handlerClickBank (index)  {
      	alert(index)
      	getUserBack({
          identify: index
      	});
    	this.$alert( '您的余额', {})
      },
      fetchData(params) {
        this.listLoading = true;
        getUserList(params).then(response => {
          this.list = response.detail.list;
          this.totals = response.detail.totals;
          this.listLoading = false;
        })
      },

   },
  };
</script>