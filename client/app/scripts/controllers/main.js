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
         $scope.labels = [];
         $scope.series = ['Target Price', 'Lowest Price'];
         
         $scope.data = [
         
         ];
         $scope.output = "";

         for(var i = 0; i < $scope.watchers.length; i++){
            //$scope.output += "<p>" + "The product's name is: " + $scope.watchers[i]['name'] + "</p>";
            if(i == 0){
                $scope.data = [
                     [$scope.watchers[i]['target_price']],
                     [$scope.watchers[i]['lowest_price']]
                ];
                $scope.labels = ["SKU: " + $scope.watchers[i]['query_string']];
            }else{
                //$scope.data.push([$scope.watchers[i]['target_price']],$scope.watchers[i]['lowest_price']);
                $scope.labels.push("SKU: " + $scope.watchers[i]['query_string']);
                $scope.data[0].push($scope.watchers[i]['target_price']);
                $scope.data[1].push($scope.watchers[i]['lowest_price']);
            }   
         }

         
         for(var i = 0; i < $scope.watchers.length; i++){
            $scope.output += "<ul> <li>SKU: " + $scope.watchers[i]['query_string'] + " [" + $scope.watchers[i]['status'] + "] " + "</li><li>Product's Name: " + $scope.watchers[i]['name'];
            if($scope.watchers[i]['purchase']){
                $scope.output += "</li><li> It's a <strong>good time</strong> to make a purchase </li>";
            }else{
                $scope.output += "</li><li> It's <strong>not a good time</strong> to make a purchase </li>";
            }
            $scope.output += "</ul>";
         }
    };

   
    $interval( function(){$scope.updateWatchers();}, 3000)

    $scope.getSkuFromURL = function(url) {
        return url.substring(url.indexOf("skuId=")+6, url.length);
    };


  });
