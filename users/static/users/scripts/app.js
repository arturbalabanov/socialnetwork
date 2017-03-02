/**
 * Created by artur on 24/02/17.
 */
var profileApp = angular.module('profileApp', ['djng.urls', 'ngAnimate', 'ui.bootstrap']);

profileApp.config(function ($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

