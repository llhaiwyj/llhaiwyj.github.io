<template>
	<div class="app-container">
		<div class="block">
			<span class="wrapper">
    <el-button type="success" @click="cs('all')">所有</el-button>
    <el-button type="warning" @click="cs('finish')">完成的</el-button>
    <el-button type="danger" @click="cs('wait_withdraw')">等待提现</el-button>
    <el-button type="info" @click="cs('wait_auth')">等待审核</el-button>
  </span>
		</div>
		<el-table :data="list" v-loading.body="listLoading" element-loading-text="拼命加载中" border fit highlight-current-row>
			<el-table-column align="center" label='ID' width="95">
				<template scope="scope">
					{{scope.$index}}
				</template>
			</el-table-column>
			<el-table-column label="current_state" width="80">
				<template scope="scope">
					{{scope.row.current_state}}
				</template>
			</el-table-column>
			<el-table-column label="current_state_name" width="80" align="center">
				<template scope="scope">
					<span>{{scope.row.current_state_name}}</span>
				</template>
			</el-table-column>
			<el-table-column label="current_state_time" width="120" align="center">
				<template scope="scope">
					{{scope.row.current_state_time}}
				</template>
			</el-table-column>
			<el-table-column label="totals" width="120" align="center">
				<template scope="scope">
					{{scope.row.totals}}
				</template>
			</el-table-column>
			<el-table-column label="trade_no" width="180" align="center">
				<template scope="scope">
					{{scope.row.trade_no}}
				</template>
			</el-table-column>
			<el-table-column label="transfer_channel" width="80" align="center">
				<template scope="scope">
					{{scope.row.transfer_channel}}
				</template>
			</el-table-column>
			<el-table-column label="操作" width="100" align="center">
				<template scope="scope">
					<p @click=clickcourse(scope.$index)>查看</p>
				</template>
			</el-table-column>

		</el-table>
		<br>
		<el-pagination layout="total, prev, pager, next, jumper" @current-change="handleCurrentChange" :page-size=10 :total=totals>
		</el-pagination>
	</div>
</template>

<script>
	import { getWithdraw, getAuth } from '@/api/zn';

	export default {
		data() {
			return {
				list: null,
				totals: 0,
				listLoading: true,
			}
		},
		created() {
			this.fetchData({
				page: 1,
				withdraw_type: 'all'
			});
		},
		methods: {
			handleCurrentChange(val) {
				this.fetchData({
					page: val
				})
			},
			cs: function(index) {
				this.fetchData({
					page: 1,
					withdraw_type: index
				});
			},
			clickcourse: function(e) {
				alert(e)
				getAuth({
					withdraw_id: e
				}).then(a => {
					
				})
			},
			fetchData(params) {
				this.listLoading = true;
				getWithdraw(params).then(response => {
					console.log(response.detail.list)
					this.list = response.detail.list;
					this.totals = response.detail.totals;
					this.listLoading = false;
				})
			}
		}
	};
</script>

<style>
	.block {
		margin-bottom: 20px;
		margin-top: 20px;
	}
	
	.el-table .cell {
		text-align: center;
	}
</style>