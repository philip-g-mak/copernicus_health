/**
 * Created by tomnahass on 3/12/15.
 */
(function () {
    'use strict';

    angular
        .module('copernicus.authentication', [
            'copernicus.authentication.controllers',
            'copernicus.authentication.services'
        ]);

    angular
        .module('copernicus.authentication.controllers', []);

    angular
        .module('copernicus.authentication.services', ['ngCookies']);
})();
