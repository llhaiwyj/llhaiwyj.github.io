import fetch from '@/utils/fetch';

export function money_info() {
  return fetch({
    url: '/get_money_info',
    method: 'get'
  });
}
