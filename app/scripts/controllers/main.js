'use strict';

/**
 * @ngdoc function
 * @name photoFlowApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the photoFlowApp
 */
angular.module('photoFlowApp')
  .controller('MainCtrl', ['$scope', 'apiHelper',
    function($scope, apiHelper) {
      var prefix = 'http://localhost:8000';
      var apiMap = {
        getPictureList: 'GET ' + prefix + '/picture/list/'
      };
      apiHelper.config(apiMap);

      apiHelper('getPictureList').then(function(data) {
        $scope.pictures = data.data;
        // 这段是为了应对前后端口不一样才做的，上线后不用这一段
        angular.forEach($scope.pictures, function(v) {
          v.img = 'http://localhost:8000/' + v.img;
        });
      });
    }
  ]);