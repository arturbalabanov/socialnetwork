/**
 * Created by artur on 24/02/17.
 */

profileApp.controller('ProfileCtrl', function ($scope, $http, djangoUrl) {
    var testUrl = djangoUrl.reverse('timeline:post-get-likes', {'pk': 1});
});
