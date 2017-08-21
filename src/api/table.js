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


