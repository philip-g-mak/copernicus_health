/**
 * Created by tomnahass on 3/12/15.
 */
(function () {
    'use strict';

    angular
        .module('copernicus.routes')
        .config(config);

    config.$inject = ['$routeProvider'];


    function config($routeProvider) {
        $routeProvider.when('/register', {
            controller: 'RegisterController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/authentication/register.html'
        }).otherwise('/');
    }

})();