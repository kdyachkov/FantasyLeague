'use strict';

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