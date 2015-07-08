'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
  .controller('MainCtrl', function ($scope, $http, $interval) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma',
    ];

    $scope.watchers = [];
    $scope.empty = {};


    $scope.accept = function(watcher) {
    	console.log("Adding Query: " + watcher.query);
    	$http.post('http://localhost:8000/watchers/', {'query_string':watcher.query,'name':'test','target_price':watcher.target,'threshold':watcher.threshold, 'email':watcher.email}).
    		success(function(data, status, headers, config){
    			$scope.updateWatchers();
    			$scope.watcher = $scope.empty;
    		});
    };

    $scope.updateWatchers = function() {
    	 $http.get('http://localhost:8000/watchers/').
    	 	success(function(data, status, headers, config){
    	 		$scope.watchers = data;
    	 	}).
    	 error(function(data, status, headers, config){

    	 });
    };

    $interval( function(){$scope.updateWatchers();}, 2000)
  });
