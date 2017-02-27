/**
 * Created by artur on 04/03/16.
 */

$(document).ready(function () {
    var $newPostForm = $('#new-post-form');
    var $allPosts = $('#all-posts');
    var $emptyPostErrorMessage = $('#empty-post-error-message');

    $emptyPostErrorMessage.hide();

    function newPostAjaxRequest($textarea) {
        var requestData = {
            'text': $textarea.val()
        };

        var destinationUrl = $newPostForm.attr('action');

        $.post(destinationUrl, requestData)
            .done(function (newPostData) {
                $textarea.val("");
                $emptyPostErrorMessage.hide();
                var $newPost = $(postTemplate({posts: newPostData}));
                $newPost.hide();
                $allPosts.prepend($newPost);
                $newPost.slideDown("fast");
            })
            .fail(function (data) {
                $emptyPostErrorMessage.show();
            });
    }

    $newPostForm.on('submit', function (e) {
        e.preventDefault();
        $this = $(this);
        var $textarea = $this.find('[name=text]');
        newPostAjaxRequest($textarea);
    });

});