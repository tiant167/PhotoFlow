'use strict';

/**
 * @ngdoc function
 * @name photoFlowApp.controller:PictureCtrl
 * @description
 * # PictureCtrl
 * Controller of the photoFlowApp
 */
angular.module('photoFlowApp')
  .controller('PictureCtrl', ['$scope', 'apiHelper', 'Lightbox',
    function($scope, apiHelper, Lightbox) {
      var prefix = '/api';
      var apiMap = {
        getPictureList: 'GET ' + prefix + '/picture/list/'
      };
      apiHelper.config(apiMap);

      apiHelper('getPictureList').then(function(data) {
        $scope.pictures = data.data;
        var smallPic = [];
        var longPic = [];
        angular.forEach($scope.pictures, function(v) {
          v.url = v.middle;
          v.thumbUrl = v.thumbnail;
          // 这段是把长的短的区分开
          if (v.long) {
            longPic.push(v);
          } else {
            smallPic.push(v);
          }
        });

        // 合并长图短图，短图一定要三张连着
        for (var i = 0; i < longPic.length; i++) {
          var longItem = longPic[i];
          if (smallPic.length < 4 * i + 3) {
            // 剩下的不足3个咯,所以往上一个长图后面继续插，把小图留在最后
            smallPic.splice(4 * i - 1, 0, longItem);
          } else {
            smallPic.splice(4 * i + 3, 0, longItem);
          }
        }
        $scope.pictures = smallPic;
      });

      $scope.openLightboxModal = function(index) {
        Lightbox.openModal($scope.pictures, index);
      };

      $scope.seo = {
        pageTitle: 'Gallery',
        pageDescription: 'Photo Gallery of My Blog'
      };
    }
  ]);