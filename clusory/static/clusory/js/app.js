angular.module('clusoryApp', [
  'ui.router',
  'ngResource',
  'clusoryApp.services',
  'clusoryApp.controllers',
])
  .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {
    // Force angular to use square brackets for template tag
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

    // Django expects jQuery like headers
    // $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';

    // Routing

    $urlRouterProvider.otherwise('/');
    $stateProvider
      .state('debates', {
        url: '/',
        templateUrl: 'static/clusory/partials/debate-list.html',
        controller: 'DebateListCtrl',
      })
      .state('my-debates', {
        url: '/:userId',
        templateUrl: 'static/clusory/partials/debate-list.html',
        controller: 'UserCtrl',
      })
      .state('profile', {
        url: '/profile/:userId',
        templateUrl: 'static/clusory/partials/profile.html',
        controller: 'UserCtrl',
      })
      .state('debate', {
        url: '/debate/:debateId',
        templateUrl: 'static/clusory/partials/debate.html',
        controller: 'DebateCtrl',
      })
  });
