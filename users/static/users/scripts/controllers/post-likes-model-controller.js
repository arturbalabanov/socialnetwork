/**
 * Created by artur on 28/02/17.
 */
profileApp.controller('PostLikesModalCtrl', function ($scope, $uibModalInstance, likers) {
    $scope.users = likers;
});
