import fetch from '@/utils/fetch';

//export function getWithdraw(params) {
//return fetch({
//  url: '/withdraw/{withdraw_type}{page}',
//  method: 'get',
//  params: {
//  	withdraw_type: 'all',
//  	page: 1
//  }
//});
//}
export function getWithdraw(params) {
return fetch({
    url: '/withdraw',
    method: 'get',
    params
});
}
export function getAuth(params) {
return fetch({
    url: '/auth_withdraw',
    method: 'post',
});
}