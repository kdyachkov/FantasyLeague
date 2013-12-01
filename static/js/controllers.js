
myApp.factory('Players', function($http){
    var Players = {};

    var method = 'POST';
    var url = '/get_players/';
    $http({method: 'GET', url: url}).
        success(function(data, status, headers, config) {
            Players.players = data['players']
            Players.goalkeapers = _.filter(Players.players, function(player){ return player.primary_position == 'GK'})
            Players.defenders = _.filter(Players.players, function(player){ return player.primary_position == 'D'})
            Players.midfielders = _.filter(Players.players, function(player){ return player.primary_position == 'M'})
            Players.forwards = _.filter(Players.players, function(player){ return player.primary_position == 'F'})
            // this callback will be called asynchronously
            // when the response is available
        }).
        error(function(data, status, headers, config) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
        });

    Players.playersToShow = ''
    Players.getPlayersToShow = function(){
        if (Players.playersToShow === ''){return []}
        else if (Players.playersToShow === 'ALL'){return Players.players}
        else if (Players.playersToShow === 'GK'){return Players.goalkeapers}
        else if (Players.playersToShow === 'D'){return Players.defenders}
        else if (Players.playersToShow === 'M'){return Players.midfielders}
        else if (Players.playersToShow === 'F'){return Players.forwards}
    }

    return Players;

});

myApp.factory('Team', function(){
    var Team = {};
    Team.goalkeaper = [];
    Team.defenders = [];
    Team.midfielders = [];
    Team.forwards = []
    Team.allPlayers = []
    Team.maxPlayers = 8;
    Team.maxGoalkeepers = 1;
    Team.maxDefenders = 3;
    Team.maxMidfielders = 3;
    Team.maxForwards = 1;
    Team.maxValueToSpend = 50;

    Team.addPlayer = function(player, position){
        console.log("IN HERE")
        console.log(position)
        if (Team.allPlayers.length >= Team.maxPlayers){
            alert("Cannot add any more players")
            return false;
        }
        if (_.contains(Team.allPlayers, player)){
            alert("Cannot add the same player twice");
            return false
        }
        if((Team.getTotalValue() + Number(player.init_value)) > Team.maxValueToSpend){
            console.log((Team.getTotalValue() + player.init_value))
            alert("Cannot add player, insufficient funds");
            return false;
        }
        isAdded = false;
        switch(position){
            case('GK'):
                isAdded = Team.addGoalkeaper(player);
                break;
            case('D'):
                console.log("IN HERE2")
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
            // console.log(Team.goalkeaper)
            // console.log(Team.defenders)
            // console.log(Team.midfielders)
            // console.log(Team.forwards)
            return true;
        }
        else{
            return false;
        }
    }

    Team.addGoalkeaper = function(player){
        if (Team.goalkeaper.length >= Team.maxGoalkeepers){
            alert("Cannot add any more goalkeapers")
            return false;
        }
        Team.goalkeaper.push(player);
        return true
    };

    Team.addDefender = function(player){
        if (Team.defenders.length >= Team.maxDefenders){
            alert("Cannot add any more defenders")
            return false;
        }
        Team.defenders.push(player);
        console.log('HERE')
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
        Team.goalkeaper = _.without(Team.goalkeaper, player)
        Team.defenders = _.without(Team.defenders, player)
        Team.midfielders = _.without(Team.midfielders, player)
        Team.forwards = _.without(Team.forwards, player)
        return true;
    }

    Team.getTotalValue = function(){
        var total = 0;
        _.each(Team.allPlayers,function(player){
            total += Number(player.init_value);
        })
        return total;
    }

    Team.getPositionLine = function(position){
        if(position=='GK'){
            return [Team.goalkeaper, Team.maxGoalkeepers]
        }
        else if(position=='D'){
            return [Team.defenders, Team.maxDefenders]
        }
        else if(position=='M'){
            return [Team.midfielders, Team.maxMidfielders]
        }
        else if(position=='F'){
            return [Team.forwards, Team.maxForwards]
        }
    }

    return Team
});


function PlayersCtrl($scope, Players, Team){
    $scope.allPlayers = Players;
    $scope.positionsToShow = function(){
        return Players.playersToShow;
    }
    $scope.getPlayers = function(){
        return Players.getPlayersToShow()
    };
    $scope.udatePlayersTable = function(posToShow){
        Players.playersToShow = posToShow;
        // $scope.getPlayers()
    }

    $scope.addPlayer = function(player){
        Team.addPlayer(player, $scope.positionsToShow);
        
    }
}

function TeamCtrl($scope, Team){
    
    $scope.showAllPlayers = function(){
        console.log(Team.allPlayers)
        return Team.allPlayers;
    }

    $scope.getGoalkeeper = function(){
        return Team.goalkeaper
    }
    $scope.getMaxGoalkeepers = function(){
        return Team.maxGoalkeepers;
    }
    $scope.getDefenders = function(){
        return Team.defenders;
    }
    $scope.getMaxDefenders = function(){
        // console.log("HERE")
        return Team.maxDefenders;
    }
    $scope.getMidfielders = function(){
        return Team.midfielders;
    }
    $scope.getMaxMidfielders = function(){
        return Team.maxMidfielders;
    }
    $scope.getForwards = function(){
        return Team.forwards;
    }
    $scope.getMaxForwards = function(){
        return Team.maxForwards;
    }


    $scope.getTotalValue = function(){
        return Team.getTotalValue()
    }
} 
