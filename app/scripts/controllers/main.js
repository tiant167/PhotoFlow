'use strict';

angular.module('photoFlowApp')
  .controller('MainCtrl', ['$scope', 'apiHelper',
    function($scope, apiHelper) {
      window.prerenderReady = false;
      var prefix = '/api';
      var apiMap = {
        getWebsiteConf: 'GET ' + prefix + '/website/conf/'
      };
      apiHelper.config(apiMap);

      apiHelper('getWebsiteConf').then(function(data) {
        $scope.websiteConfig = data.data;
      });
      $scope.seo = {
        pageTitle: '',
        pageDescription: ''
      };
    }
  ]);