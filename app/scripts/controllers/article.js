'use strict';

/**
 * @ngdoc function
 * @name photoFlowApp.controller:ArticleCtrl
 * @description
 * # ArticleCtrl
 * Controller of the photoFlowApp
 */
angular.module('photoFlowApp')
  .controller('ArticleCtrl', ['$scope', 'apiHelper', '$routeParams',

    function($scope, apiHelper, $routeParams) {
      var prefix = 'http://localhost:8000';
      var apiMap = {
        // delBlackList: 'GET /api/app/{app_id}/blacklist/delete',
        getBlog: 'GET ' + prefix + '/blog/article/:id/'
      };
      apiHelper.config(apiMap);

      apiHelper('getBlog', {
        param: {
          'id': $routeParams.id
        }
      }).then(function(data) {
        $scope.blog = data.data;
        $scope.markdown = data.data.content;
      });
    }
  ]);