
myApp.factory('Players', function($http){
    var Players = {};

    var method = 'POST';
    var url = '/get_players/';
    $http({method: 'GET', url: url}).
        success(function(data, status, headers, config) {
            Players.players = data['players']
            // this callback will be called asynchronously
            // when the response is available
        }).
        error(function(data, status, headers, config) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
        });

    return Players;

});

myApp.factory('Team', function(){
    var Team = {};
    Team.goalkeaper = '';
    Team.defenders = [];
    Team.midfielders = [];
    Team.forwards = []
    Team.allPlayers = []
    Team.maxPlayers = 8;
    Team.maxGoalkeepers = 1;
    Team.maxDefenders = 3;
    Team.maxMidfielders = 3;
    Team.maxForwards = 1;

    Team.addPlayer = function(player, position){
        if (Team.allPlayers.length >= Team.maxPlayers){
            alert("Cannot add any more players")
            return false;
        }
        isAdded = false;
        switch(position){
            case('GK'):
                isAdded = Team.addGoalkeaper(player);
                break;
            case('D'):
                isAdded = Team.addDefender(player);
                break;
            case('M'):
                isAdded = Team.addMidfielder(player);
                break;
            case('F'):
                isAdded = Team.addForward(player);
                break;
        }

        if (isAdded==true){
            Team.allPlayers.push(player)
            console.log(Team.goalkeaper)
            console.log(Team.defenders)
            console.log(Team.midfielders)
            console.log(Team.forwards)
            return true;
        }
        else{
            return false;
        }
    }

    Team.addGoalkeaper = function(player){
        Team.goalkeaper = player;
        return true
    };

    Team.addDefender = function(player){
        if (Team.defenders.length >= Team.maxDefenders){
            alert("Cannot add any more defenders")
            return false;
        }
        Team.defenders.push(player);
        return true;
    };

    Team.addMidfielder = function(player){
        if (Team.midfielders.length >= Team.maxMidfielders){
            alert("Cannot add any more midfielders")
            return false;
        }
        Team.midfielders.push(player);
        return true;
    };
    
    Team.addForward = function(player){
        if (Team.forwards.length >= Team.maxForwards){
            alert("Cannot add any more forwards")
            return false;
        }
        Team.forwards.push(player);
        return true;
    }

    Team.removePlayer = function(player, position){
        Team.allPlayers = _.without(Team.allPlayers, player)
        if(position=='GK'){
            Team.goalkeaper = _.without(Team.goalkeaper, player)
        }
        else if (position==='D'){
            Team.defenders = _.without(Team.defenders, player)
        }
        else if (position==='M'){
            Team.midfielders = _.without(Team.midfielders, player)
        }
        else if (position==='F'){
            Team.forwards = _.without(Team.forwards, player)
        }
        return true;
    }

    return Team
});


function PlayersCtrl($scope, Players, Team){
    $scope.allPlayers = Players;
    $scope.positionsToShow = 'ALL'
    $scope.getPlayers = function(){
        if ($scope.positionsToShow === 'ALL'){
            return $scope.allPlayers.players;
        }
        else{
            players = _.filter($scope.allPlayers.players, 
                function(player){
                    return _.contains(player.position, $scope.positionsToShow);
                }
            )
            return players;    
        }
    };
    $scope.udatePlayersTable = function(posToShow){
        $scope.positionsToShow = posToShow;
        $scope.getPlayers()
    }

    $scope.addPlayer = function(player){
        Team.addPlayer(player, $scope.positionsToShow);
        
    }
}

function TeamCtrl($scope, Team){

}
