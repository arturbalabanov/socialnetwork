/**
 * Created by artur on 24/02/17.
 */
profileApp.controller('ProfileCtrl', ['$scope', '$http', '$uibModal', 'djangoUrl', function ($scope, $http, $uibModal, djangoUrl) {
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

    $scope.showLikesModal = function (post) {
        var getLikersUrl = djangoUrl.reverse('timeline:post-get-likes', {'pk': post.id});
        $http.get(getLikersUrl).then(function (response) {
            var postLikesModal = $uibModal.open({
                templateUrl: 'templates/post-likes-modal.html',
                controller: 'PostLikesModalCtrl',
                appendTo: angular.element(document.getElementById('profile-app')),
                resolve: {
                    likers: function () {
                        return response.data;
                    }
                }

            });
        }, function (error) {
            var alert = {
                type: 'warning',
                msg: "There was a problem with the server, try again later"
            };
            $scope.alerts.push(alert);
        });
    };

    $scope.createNewPost = function () {
        var createNewPostUrl = djangoUrl.reverse('timeline:post-list');
        var requestData = {
            'text': $scope.create_post_form.text
        };

        $http.post(createNewPostUrl, requestData).then(function (response) {
            $scope.allPosts.push(response.data);
            $scope.create_post_form.text = "";
        }, function (error) {
            var alert = {
                type: 'warning',
                msg: "There was a problem with the server, try again later"
            };
            $scope.alerts.push(alert);
        });
    };

    $scope.post_comment_form = {};

    $scope.createNewPostComment = function (post) {
        var createNewPostCommentUrl = djangoUrl.reverse('timeline:postcomment-list');
        var request_data = {
            text: $scope.post_comment_form['post_id_' + post.id].text,
            post_id: post.id
        };

        $http.post(createNewPostCommentUrl, request_data).then(function (response) {
            post.comments.push(response.data);
            $scope.post_comment_form['post_id_' + post.id].text = ""
        }, function (error) {
            var alert = {
                type: 'warning',
                msg: "There was a problem with the server, try again later"
            };
            $scope.alerts.push(alert);
        });
    };
}]);

