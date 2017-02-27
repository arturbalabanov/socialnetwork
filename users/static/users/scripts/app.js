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
    $scope.allPosts = [];

    $scope.retrieveAllPosts = function (username) {
        var retrieveAllPostsUrl = djangoUrl.reverse('users:get-posts', [username]);
        $http.get(retrieveAllPostsUrl).then(function (response) {
            $scope.allPosts = response.data;
        }, function (error) {
            var alert = {
                type: 'warning',
                msg: "There was problem with retrieving the posts, please try again"
            };
            $scope.alerts.push(alert);
        });
    };

    $scope.alerts = [];

    $scope.likePost = function (post) {
        var likePostUrl = djangoUrl.reverse('timeline:post-like');
        var requestData = {
            id: post.id
        };

        $http.post(likePostUrl, requestData).then(function (response) {
            // angular.copy(response.data, post);
            post.number_of_likes = response.data.number_of_likes;
        }, function (error) {
            var alert = {
                type: 'warning',
                msg: "There was problem with liking this post, please try again later."
            };
            $scope.alerts.push(alert);
        });
    };

    $scope.toggleFriendship = function (targetUsername) {
        var friendUserUrl = djangoUrl.reverse('users:toggle_friendship');
        var requestData = {
            target_username: targetUsername
        };

        $http.post(friendUserUrl, requestData).then(function (response) {
            // TODO: Move all alerts to a service
            var alert = {};
            if (response.data.areFriends) {
                alert.type = 'success';
                alert.msg = "You are now friends with " + targetUsername + ".";
            } else {
                alert.type = 'danger';
                alert.msg = "You are no longer friends with " + targetUsername + ".";
            }
            $scope.alerts.push(alert);
            $scope.areFriends = response.data.areFriends;
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
