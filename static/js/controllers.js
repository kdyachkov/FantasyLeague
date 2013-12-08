myApp.factory('SharedService', function($rootScope, $http){
    var SharedService = {};

    SharedService.broadcastItem = function(name, args) {
        $rootScope.$broadcast(name, args);
    };

    SharedService.makePOSTRequest = function(url, data){
        return this.makeRequest('POST', url, data)
    };
    SharedService.makeGETRequest = function(url, data){
        return this.makeRequest('GET', url, data)
    };
    SharedService.makeRequest = function(rtype, url, data){
        var headers =  {'X-CSRFToken' : window.CSRF_TOKEN };
        return $http({method: rtype, url: url, data: $.param(data || {}), headers: headers})
    };

    return SharedService;
});





myApp.factory('Players', function(SharedService){
    var Players = {};

    var method = 'POST';
    var url = '/get_players/';
    // $http({method: 'GET', url: url}).
    SharedService.makeGETRequest(url).
        success(function(data, status, headers, config) {
            Players.players = data['players']
            console.log(Players.players)
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
        else if (Players.playersToShow === 'S'){return Players.players}
    }

    return Players;

});

myApp.factory('Team', function(SharedService){
    var Team = {};
    Team.exists = false;
    Team.name = '';
    Team.goalkeaper = [];
    Team.defenders = [];
    Team.midfielders = [];
    Team.forwards = [];
    Team.subs = [];
    Team.allPlayers = []
    Team.maxPlayers = 8;
    Team.maxGoalkeepers = 1;
    Team.maxDefenders = 2;
    Team.maxMidfielders = 2;
    Team.maxForwards = 1;
    Team.maxSubs = 2;
    Team.maxValueToSpend = 0;
    Team.players = {};


    Team.loadTeam = function(){
        var url = '/get_team/';
        // $http({method: 'GET', url: url}).
        SharedService.makePOSTRequest(url, {team_name:Team.name}).
        success(function(data, status, headers, config) {
            Team.name = data.team_name;
            Team.exists = data.team_exists;
            Team.maxValueToSpend = data.money_to_spend;
            Team.allPlayers = data.players;
            if (Team.allPlayers.length > 0){
                Team.goalkeaper = data.goalkeeper;
                Team.defenders = data.defenders;
                Team.midfielders = data.midfielders;
                Team.forwards = data.forwards;
                Team.subs = data.subs;


            }
            else{
                console.log("NO players found")
            }
//            Team.allPlayers = Team.goalkeaper.concat(Team.defenders, Team.midfielders, Team.forwards, Team.subs);


            // this callback will be called asynchronously
            // when the response is available
        }).
        error(function(data, status, headers, config) {
            console.log(data);
//            alert(data.message)
        });
    }

    Team.doesTeamExist = function(){
        return Team.exists
    }

    Team.addPlayer = function(player, position){
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
                isAdded = Team.addDefender(player);
                break;
            case('M'):
                isAdded = Team.addMidfielder(player);
                break;
            case('F'):
                isAdded = Team.addForward(player);
                break;
            case('S'):
                isAdded = Team.addSub(player);
                break;
        }

        if (isAdded==true){
            Team.allPlayers.push(player)
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
    };
    Team.addSub = function(player){
        if (Team.subs.length >= Team.maxSubs){
            alert("Cannot add any more subs")
            return false;
        }
        Team.subs.push(player);
        return true;
    }

    Team.removePlayer = function(player){
        Team.allPlayers = _.without(Team.allPlayers, player)
        Team.goalkeaper = _.without(Team.goalkeaper, player)
        Team.defenders = _.without(Team.defenders, player)
        Team.midfielders = _.without(Team.midfielders, player)
        Team.forwards = _.without(Team.forwards, player)
        Team.subs = _.without(Team.subs, player)
        return true;
    }

    Team.getTotalValue = function(){
        var total = 0;
        _.each(Team.allPlayers,function(player){
            total += Number(player.init_value);
        })
        return total;
    }

    Team.getPositionPlayersToAdd = function(position){
        if(position=='GK'){
            return Team.maxGoalkeepers - Team.goalkeaper.length
        }
        else if(position=='D'){
            return Team.maxDefenders - Team.defenders.length
        }
        else if(position=='M'){
            return Team.maxMidfielders - Team.midfielders.length
        }
        else if(position=='F'){
            return Team.maxForwards - Team.forwards.length
        }
        else if(position=='S'){
            return Team.maxSubs - Team.subs.length
        }
    }

    Team.saveTeam = function(){
        Team.players['GK'] = Team.goalkeaper;
        Team.players['D'] = Team.defenders;
        Team.players['M'] = Team.midfielders;
        Team.players['F'] = Team.forwards;
        Team.players['S'] = Team.subs;
        console.log(Team.players)
        var team = JSON.stringify(Team.players)
        console.log(team)
        var url = '/save_team/'
        SharedService.makePOSTRequest(url, {team: team}).
            success(function(data, status, headers, config) {
                console.log(data)
        }).
        error(function(data, status, headers, config) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
        });
    };

    Team.createTeam = function(team_name){
        Team.name = team_name
        var url = '/create_team/'
        SharedService.makePOSTRequest(url, {team_name: Team.name}).
            success(function(data, status, headers, config){
                console.log(data)
                Team.exists = true;
            }).
            error(function(data, status, headers, config) {
                console.log(data)
                alert(data.message)
        });


    }

    return Team
});


function PlayersCtrl($scope, $rootScope, Players, Team){
    $rootScope._ = _

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

    $scope.name = '';

    $scope.getTeamName = function(){
        return Team.name
    }

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
    $scope.getSubs = function(){
        return Team.subs
    }
    $scope.getTotalValue = function(){
        return Team.getTotalValue()
    }
    $scope.getMaxValueToSpend = function(){
        return Team.maxValueToSpend
    }

    $scope.saveTeam = function(){
        Team.saveTeam()
    }

    $scope.createTeam = function(){
        Team.createTeam($scope.name);
    }

    $scope.loadTeam = function(){
        Team.loadTeam()
    }

    $scope.doesTeamExist = function(){
        return Team.doesTeamExist();
    }
}
