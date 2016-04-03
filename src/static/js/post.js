/**
 * Created by kymid on 03.04.16.
 */
function load_comments() {
    $('#comments').load('{% url "post:post_comments" pk=post.id %}');
};
window.setInterval(load_comments, 1000);