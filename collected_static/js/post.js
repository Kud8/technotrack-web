/**
 * Created by kymid on 03.04.16.
 */
// function load_comments() {
//     $('[data-comments-url]').each(function() {
//         var url = $(this).data('comments-url');
//         $(this).load(url);
//     });
// };

function show(id) {
    $(id).show();
}

function hide_dialog(id) {
    $(id).hide();
}

window.setInterval(load_comments, 1000);