/**
 * Created by artur on 24/02/17.
 */
var profileApp = angular.module('profileApp', ['djng.urls', 'ngAnimate', 'ui.bootstrap']);

profileApp.config(function ($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

profileApp.controller('ProfileCtrl', function ($scope, $http, $uibModal, djangoUrl) {
    $scope.alerts = [];

    $scope.toggleFriendship = function (targetUsername) {
        var friendUserUrl = djangoUrl.reverse('users:toggle_friendship');
        var requestData = {
            target_username: targetUsername
        };

        $http.post(friendUserUrl, requestData).then(function (response) {
            var alert = {};
            if (response.data.areFriends) {
                alert.type = 'success';
                alert.msg = "You are now friends with " + targetUsername + ".";
            } else {
                alert.type = 'danger';
                alert.msg = "You are no longer friends with " + targetUsername + ".";
            }
            $scope.alerts.push(alert);
        }, function (error) {
            var alert = {
                type: 'warning',
                msg: "There was a problem with the server, try again later"
            };
            $scope.alerts.push(alert);
        });
    };

    $scope.closeAlert = function (index) {
        $scope.alerts.splice(index, 1);
    };

    var testUrl = djangoUrl.reverse('timeline:post-get-likes', {'pk': 3});

    $http.get(testUrl).then(function (response) {
        $scope.likers = response.data;
    }, function (error) {
        console.log("error:", error);
    });
});
