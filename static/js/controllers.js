
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

    Team.addGoalkeaper = function(player){
        Team.goalkeaper = player;
    };

    Team.addDefender = function(player){
        Team.defenders.push(player);
    };

    Team.addMidfielder = function(player){
        Team.midfielders.push(player);
    };
    
    Team.addForward = function(player){
        Team.forwards.push(player);
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
        switch($scope.positionsToShow){
            case('GK'):
                Team.addGoalkeaper(player);
                break;
            case('D'):
                Team.addDefender(player);
                break;
            case('M'):
                Team.addMidfielder(player);
                break;
            case('F'):
                Team.addForward(player);
                break;
        }
        console.log(Team.goalkeaper)
        console.log(Team.defenders)
        console.log(Team.midfielders)
        console.log(Team.forwards)
        
    }
}
