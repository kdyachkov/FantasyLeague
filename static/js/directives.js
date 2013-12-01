
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
                if(pos === 'ALL'){return 'All'}
                else if(pos === 'GK'){return 'Goalkeepers'}
                else if(pos === 'D'){return 'Defenders'}
                else if(pos === 'M'){return 'Midfielders'}
                else if(pos === 'F'){return 'Forwards'}
            }
        },
        template:  "<button class ='btn btn-primary'>Show {{getPositionFull()}}</button>"
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
            $scope.isAffordable = function(){
                if((Team.getTotalValue() + Number($scope.player.init_value)) > Team.maxValueToSpend){
                    return false;
                }
                return true;
            }
        },
        template: "<button class='btn btn-primary' ng-click='addPlayer()' ng-disabled='!isAffordable()' ng-show='!isAdded()'>Select</button>\
                    <button class='btn btn-danger' ng-click='removePlayer()' ng-show='isAdded()'>Remove</button>\
                    <button class='btn btn-info'>Info</button> "
    }
})

myApp.directive('teamplayer', function(Team){
    return {
        restrict: 'E',
        scope: {
            players: '='
        },
        // template: "blahblah"
        template: "<button class='btn btn-success' ng-repeat='player in players'>{{player.name}}</button>"
    }
})


// myApp.directive('teamplayers', function(Team){
//     var elem = function(position){
//         elems = []
//         elems.push(angular.element("<button class='btn btn-info'>Info</button>"));
//         elems.push(angular.element("<button class='btn btn-danger'>REMOVE</button>"));
//         return elems
//     }
//     return {
//         restrict: 'E',
//         scope:{
//             position: "@",
//             players: "=",
//             getMaxPlayers: "&maxplayers",
//         },
//         // controller: function($scope){
//         //     console.log($scope.players)
//         //     console.log($scope.maxplayers)
//         // },
//         template: function($scope){
//             return "<button class='btn'>Add</button>"
//         },
//         link: function(scope){
//             console.log(scope.getMaxPlayers())
//             scope.$watchCollection('players', function(players){
//                 console.log(players)
//             })       
//         }

//         // compile: function(templateElement, scope){
//         //     // console.log(scope.position)
//         //     // templateElement.append(elem(scope.position))
//         // }
//     }
// })