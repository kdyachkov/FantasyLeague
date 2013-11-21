

function FirstCtrl2($scope){
	$scope.data = {message: 'Hello'}
}

function FirstCtrl($scope, $http) {
	var method = 'POST';
	var url = '/get_players/';
	$http({method: 'GET', url: url}).
	  success(function(data, status, headers, config) {
	  	console.log(data)
	    $scope.data = {players:data['players']}
	    // this callback will be called asynchronously
	    // when the response is available
	  }).
	  error(function(data, status, headers, config) {
	    // called asynchronously if an error occurs
	    // or server returns response with an error status.
	});
}