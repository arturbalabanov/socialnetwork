/**
 * Created by artur on 24/02/17.
 */
console.log('js file');

var profileApp = angular.module('profileApp', ['djng.urls']);

profileApp.config(function ($httpProvider) {
    console.log('js config');
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

profileApp.controller('ProfileCtrl', function ($scope, $http, djangoUrl) {
    var testUrl = djangoUrl.reverse('timeline:post-get-likes', {'pk': 1});

    $http.get(testUrl).success(function (data) {
        console.log(data[0].username);
    }).error(function (error) {
        console.log("error:", error);
    });
});
