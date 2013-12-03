
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
                console.log($scope.position)
                console.log($scope.player)
                Team.removePlayer($scope.player, $scope.position)
            }
            $scope.isAdded = function(){
                return _.contains(Team.allPlayers, $scope.player)
            }
            $scope.canBuy = function(){
                if((Team.getTotalValue() + Number($scope.player.init_value)) > Team.maxValueToSpend){
                    return false;
                }
                return true;
            }
        },
        template: "<button class='btn btn-primary' ng-click='addPlayer()' ng-disabled='!canBuy()' ng-show='!isAdded()'>Select</button>\
                    <button class='btn btn-danger' ng-click='removePlayer()' ng-show='isAdded()'>Remove</button>\
                    <button class='btn btn-info'>Info</button> "
    }
})

myApp.directive('teamplayers', function(Team){
    return {
        restrict: 'E',
        scope: {
            players: '='
        },
        controller: function($scope){
            
            
            
        },
        // template: "blahblah"
        template: "<div class='teamplayers' ng-repeat='player in players'>\
            <button class='btn btn-success' ng-click='showControlBox(player)'>{{player.name}} ({{player.init_value}})</button>\
            <div class='alert alert-danger' ng-show='shouldShowControlBox(player)'>\
                <button class='btn btn-danger' ng-click='removePlayer(player)'>Remove</button>\
                <button class='btn btn-info'>Info</button>\
            </div>\
            </div>",
        // link: function(scope, iElement){
        //     iElement.bind('mouseover', function(e){
        //         console.log("Mouse over")
        //         iElement.html("<button class='btn btn-danger'>Remove</btn>");
        //         iElement.unbind('mouseover');
        //     })
        // }
    }
})


myApp.directive('teamplayer', function(Team){
    return{
        restrict: 'E',
        scope:{
            player: '=',
        },
        controller: function($scope){
            $scope.showControlBox = false;
            $scope.toggleControlBox = function(){
                $scope.showControlBox = !$scope.showControlBox
            }
            $scope.removePlayer = function(player){
                Team.removePlayer(player)
            }
        },
        template: "<button class='btn btn-success' ng-click='toggleControlBox()'>{{player.name}} ({{player.init_value}})</button>\
                    <div class='alert alert-danger' ng-show='showControlBox'>\
                        <button class='btn btn-danger' ng-click='removePlayer(player)'>Remove</button>\
                        <button class='btn btn-info'>Info</button>\
                    </div>"
    }
})


myApp.directive('addplayers', function(Players, Team){
    return {
        restrict: 'E',
        scope: {
            position: '@'
        },
        controller: function($scope){
            $scope.playersToAdd = function(){
                return  Team.getPositionPlayersToAdd($scope.position)
            }

            $scope.showPlayers = function(){
                Players.playersToShow = $scope.position
            }
        },
        template: "<button class='btn' ng-repeat='i in [] | range:1:playersToAdd()' ng-click='showPlayers()'>Add</button>"
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