'use strict';


// var underscore = angular.module('underscore', []);
// underscore.factory('_', function() {
//   return window._; // assumes underscore has already been loaded on the page
// });

// var myApp = angular.module('myApp', ['underscore']);
// myApp.config(function($interpolateProvider) {
//     $interpolateProvider.startSymbol('{[{');
//     $interpolateProvider.endSymbol('}]}');
// });

// var myApp = angular.module('myApp').config(function($httpProvider) {
//     $httpProvider.defaults.headers.post['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
// });

var myApp = angular.module('myApp', ['ngCookies', 'ngTable']).
    config([
    '$httpProvider', 
    '$interpolateProvider', 
    function($httpProvider, $interpolateProvider) {
        // $interpolateProvider.startSymbol('{$');
        // $interpolateProvider.endSymbol('$}');
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    }]).
    run([
    '$http', 
    '$cookies', 
    function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    }]);

