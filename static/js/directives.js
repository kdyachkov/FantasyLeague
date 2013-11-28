
myApp.directive("player", function(){
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