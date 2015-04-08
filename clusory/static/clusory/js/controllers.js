var clusoryControllers = angular.module('clusoryApp.controllers', []);

clusoryControllers.controller('DebateListCtrl', function DebateListCtrl($scope, Debate) {
  $scope.debates = {};
   
  Debate.query(function(response) {
    $scope.debates = response;
  });

  $scope.submitDebate = function(text) {
    var debate = new Debate({text: text});
    debate.$save(function(){
      $scope.debates.unshift(debate);
    })
  }
});

clusoryControllers.controller('UserCtrl', function UserCtrl($scope, User, AuthUser) {
  $scope.debates = {};
  id = AuthUser.id;
  User.get({id:id}, function(response) {
    $scope.user = response;
    $scope.debates = response.debates;
  });
});

clusoryControllers.controller('DebateCtrl', function DebateCtrl($scope, $state, $stateParams, Debate) {
  $scope.debate = '';
  Debate.get({id: $stateParams.debateId}, function(response){
    $scope.debate = response;
    // $scope.state= $state.current
    // $  
   });


});

