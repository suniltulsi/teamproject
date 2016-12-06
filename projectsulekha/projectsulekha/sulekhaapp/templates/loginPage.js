var app = angular.module('myApp', []);
app.controller('loginCtrl', function($scope){
$scope.registerDiv = false;
$scope.loginDiv = true;
    $scope.register = function(){
    	$scope.registerDiv = true;
    	$scope.loginDiv = false;
    }

 });