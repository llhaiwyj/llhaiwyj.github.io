import fetch from '@/utils/fetch';

export function getList(params) {
  return fetch({
    url: '/table/list',
    method: 'get',
    params
  });
}

export function getUserList(params) {
  return fetch({
    url: '/user',
    method: 'get',
    params
  })
}

export function getUserBack(params) {
	return fetch({
	    url: '/get_user_bank',
	    method: 'get',
	    params
	})
}
