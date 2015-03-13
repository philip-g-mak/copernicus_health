/**
 * Created by tomnahass on 3/12/15.
 */
(function () {
    'use strict';

    angular
        .module('copernicus.config')
        .config(config);

    config.$inject = ['$locationProvider'];


    function config($locationProvider) {
        $locationProvider.html5mode(true);
        $locationProvider.hashPrefix('!');
    }
})();
