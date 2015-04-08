
angular.module('clusoryApp.services', ['ngResource'])
  .factory('Debate', function($resource) {
  	console.log("DEBATE MOD WRR");
    return $resource('/api/debates/:id/'); 
  })
  .factory('User', function($resource) {
    return $resource('/api/users/:id/'); 
  });
