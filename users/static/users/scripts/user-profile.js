/**
 * Created by artur on 04/03/16.
 */

$(document).ready(function () {
    function likePosts() {
        var $likeButtons = $('.like-button');

        function likePostAjaxRequest($post) {
            var id = $post.attr('data-post-id');

            var requestData = {
                'id': id
            };

            $.post(LIKE_TIMELINE_POST_URL, requestData).success(function (data) {
                $post.find('.number-of-likes').text(data['number_of_likes']);
            });
        }

        $likeButtons.click(function (e) {
            var $this = $(this);
            var $post = $this.closest('.timeline-post');
            likePostAjaxRequest($post);
        });
    }

    // ==================================================

    // var postLikesTemplate = Handlebars.compile($('#post-likes-list-template').html());
    //
    // function showPostLikes() {
    //     var $postLikesLinks = $('.post-likes-link');
    //     var $postLikesModal = $('#post-likes-modal');
    //     var $allPostsLikes = $('#all-post-likes');
    //
    //     function showLikesDialog(postId) {
    //         // FIXME: hard coded URL, filthy heretic!
    //         $.get("/timeline/posts/" + postId + "/get-likes/").success(function (data) {
    //             $allPostsLikes.html(postLikesTemplate({users: data}));
    //             $postLikesModal.modal('show');
    //         });
    //     }
    //
    //     $postLikesLinks.click(function (e) {
    //         var $this = $(this);
    //         var postId = $this.closest('.timeline-post').attr('data-post-id');
    //         showLikesDialog(postId);
    //     })
    // }

    // ==================================================

    // $('#post-likes-modal').modal('show');
    // var postTemplate = Handlebars.compile($('#timeline-post-template').html());

    // $.get(POSTS_LIST_URL).done(function (data) {
    //     $allPosts.append(postTemplate({posts: data}));
    //     likePosts();
    //     // showPostLikes();
    // });

    // ==================================================

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