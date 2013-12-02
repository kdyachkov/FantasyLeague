'use strict';


var underscore = angular.module('underscore', []);
underscore.factory('_', function() {
  return window._; // assumes underscore has already been loaded on the page
});

var myApp = angular.module('myApp', ['underscore']);
// myApp.config(function($interpolateProvider) {
//     $interpolateProvider.startSymbol('{[{');
//     $interpolateProvider.endSymbol('}]}');
// });


