'use strict'

function apiHelper($http) {

  /*
    author: @gaohailang
      way to use the api:
      每个 biz module 有个 endpoint api map

      var apiMap = {
          delBlackList: 'GET /api/app/{app_id}/blacklist/delete',
          fetchStat: 'GET /api/adformat/statement/{id}'
      };

      apiHelper.config(apiMap);

      apiHelper('delBlackList', app_id, config).then(function() {

      });
  */
  /*
      to config api version
  */
  var _maps = {},
    _urlPrfix = '';

  function _buildUrl(toUrl, opt) {
    var params = opt.param;
    if (!params) return toUrl;
    delete opt.param;

    if (_.isObject(params)) {
      _.each(params, function(val, key) {
        toUrl = toUrl.replace(':' + key, val);
      });
    } else {
      _.each(params, function(val) {
        toUrl = toUrl.replace(/:[^/]+/, val);
      });
    }
    return toUrl;
  }

  function helper(endpoint, opt) {
    var apiStr = _maps[endpoint];
    opt = opt || {};
    if (!apiStr) {
      // throw error
    }

    return $http(_.extend({
      method: apiStr.split(' ')[0],
      url: _urlPrfix + _buildUrl(apiStr.split(' ')[1], opt),
    }, opt));
  }

  helper.config = function(maps) {
    _maps = _.extend(_maps, maps);
  };

  return helper;
}

// fake $notice should be created
var $notice = {
  success: function() {},
  error: function() {}
};
// var apiHelperInterceptor = ;

angular.module('photoFlowApp.base.services.api', [])
  .factory('apiHelper', ['$http', apiHelper])
  .factory('apiHelperInterceptor', ['$q',
    function($q) {
      return {
        responseError: function(response) {
          if (response.config.url.indexOf('/api/') > -1) {
            $notice.error('error-' + response.status + ': ' +
              (response.config.url || '') + ', 接口出问题啦!');
          }
          return $q.reject(response);
        },

        response: function(response) {
          // config be closed
          if (response.config.url.indexOf('/api/') > -1) {
            if (response.config.method === 'POST') {
              $notice.success('操作成功！');
            }
          }
          return response;
        }
      };
    }
  ])
  .config(['$httpProvider',
    function($httpProvider) {
      $httpProvider.interceptors.push('apiHelperInterceptor');
    }
  ]);