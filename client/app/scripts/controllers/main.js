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
    $scope.length = $scope.watchers.length;
    $scope.send_email = 'False'
    
    $scope.accept = function(watcher) {
        var sku = $scope.getSkuFromURL(watcher.query);
        var email = ''
        if($scope.send_email == 'True'){
            email = watcher.email;
        }
    	$http.post('http://localhost:8000/watchers/', {'query_string':sku,'name':'test','target_price':watcher.target,'threshold':watcher.threshold,'email':email, 'send_email':$scope.send_email}).
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
         $scope.output = "";
         for(var i = 0; i < $scope.watchers.length; i++){
            //$scope.output += "<p>" + "The product's name is: " + $scope.watchers[i]['name'] + "</p>";
            $scope.output += "<ul> The product's name is:" + $scope.watchers[i]['name'] ;
            $scope.output += "<li>Your Target Price: " + $scope.watchers[i]['target_price'] + "</li>";
            $scope.output += "<li>The Lowest Price: " + $scope.watchers[i]['lowest_price'] + "</li>";
            if($scope.watchers[i]['purchase']){
                $scope.output += "<li> It's a good time to make a purchase" + "</li>";
            }else{
                $scope.output += "<li> It's not a good time to make a purchase" + "</li>";
            }
            $scope.output += "</ul>";
         }
    };

   
    $interval( function(){$scope.updateWatchers();}, 6000)

    $scope.getSkuFromURL = function(url) {
        return url.substring(url.indexOf("skuId=")+6, url.length);
    };


  });
