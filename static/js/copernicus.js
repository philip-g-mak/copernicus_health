/**
 * Created by tomnahass on 3/12/15.
 */
(function () {
    'use strict';

    angular
        .module('copernicus', [
            'copernicus.config',
            'copernicus.routes',
            'copernicus.authentication'
        ]);

    angular
        .module('copernicus')
        .run(run);

    run.$inject = ['$http'];

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }


    angular
        .module('copernicus.config', []);

    angular
        .module('copernicus.routes', ['ngRoute'])
})();

