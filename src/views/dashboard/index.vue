<template>
  <div class="dashboard-container">
    <div class='dashboard-text'>管理员:{{name}}</div>
    <div class='dashboard-text'>权限:  <span v-for='role in roles' :key='role'>{{role}}</span></div>
    <div class='dashboard-text'>资金流入(充值): {{money_in}} 元</div>
    <div class='dashboard-text'>资金流出(提现): {{money_out}} 元</div>
  </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import { money_info } from '@/api/money_info';
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
      }
    }
</script>

<style rel="stylesheet/scss" lang="scss">
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
