'use strict';

/**
 * @ngdoc function
 * @name photoFlowApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the photoFlowApp
 */
angular.module('photoFlowApp')
  .controller('BlogCtrl', ['$scope', 'apiHelper',
    function($scope, apiHelper) {
      // config apiHelper
      window.prerenderReady = false;
      var prefix = 'http://t.tinkerlab.cn/api';
      var apiMap = {
        // delBlackList: 'GET /api/app/{app_id}/blacklist/delete',
        getBlogList: 'GET ' + prefix + '/blog/list/'
      };
      apiHelper.config(apiMap);

      apiHelper('getBlogList').then(function(data) {
        $scope.blogsList = data.data;
        window.prerenderReady = true;
      });
      $scope.$parent.seo = {
        pageTitle: 'Article List',
        pageDescripton: 'Welcome to my Blog\'s atricle list'
      };

    }
  ]);