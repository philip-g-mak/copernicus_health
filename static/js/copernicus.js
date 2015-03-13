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
        .module('copernicus.config', []);

    angular
        .module('copernicus.routes', ['ngRoute'])
})();

