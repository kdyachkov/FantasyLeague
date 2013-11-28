
myApp.directive("position", function(){
    return {
        restrict: "E",
        scope:{
        	position: "@",

        },
        controller: function($scope){
            $scope.getPosition = function(){
                return $scope.position;
            }
            $scope.getPositionFull = function(){
                pos = $scope.position;
                if(pos === 'GK'){return 'Goalkeeper'}
                else if(pos === 'D'){return 'Defender'}
                else if(pos === 'M'){return 'Midfielder'}
                else if(pos === 'F'){return 'Forward'}
            }
        },
        template:  "<button class ='btn btn-primary'>Add {{getPositionFull()}}</button>"
    }
});

myApp.directive('player', function(Team){
    return {
        restrict: "E",
        scope: {
            player: "=",
            position: "@"
        },
        controller: function($scope){
            $scope.addPlayer = function(){
                Team.addPlayer($scope.player, $scope.position)
            }
            $scope.removePlayer = function(){
                Team.removePlayer($scope.player, $scope.position)
            }
            $scope.isAdded = function(){
                return _.contains(Team.allPlayers, $scope.player)
            }
        },
        template: "<button class='btn btn-primary' ng-click='addPlayer()' ng-show='!isAdded()'>Add</button>\
                    <button class='btn btn-danger' ng-click='removePlayer()' ng-show='isAdded()'>Remove</button>\
                    <button class='btn btn-info'>Info</button> "
    }
})