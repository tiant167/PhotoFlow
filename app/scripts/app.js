'use strict';

/**
 * @ngdoc overview
 * @name photoFlowApp
 * @description
 * # photoFlowApp
 *
 * Main module of the application.
 */
angular
  .module('photoFlowApp', [
    'ngRoute'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
