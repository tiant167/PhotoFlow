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
    function($scope) {
      // config apiHelper
      var apiMap = {
        // delBlackList: 'GET /api/app/{app_id}/blacklist/delete',

      };
      apiHelper.config(apiMap);


    }
  ]);