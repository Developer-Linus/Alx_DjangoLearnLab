// Basic example script to demonstrate dynamic behavior
document.addEventListener('DOMContentLoaded', function() {
    console.log('Blog page loaded');
});

//Javascript for toggling comments
function toggleComments() {
    let hiddenComments = document.querySelectorAll('.hidden-comment');
    let toggleButton = document.getElementById('toggle-comments');

    if (hiddenComments[0].style.display === "none" || hiddenComments[0].style.display === "") {
        hiddenComments.forEach(comment => comment.style.display = "block");
        toggleButton.textContent = "Less Comments";
    } else {
        hiddenComments.forEach(comment => comment.style.display = "none");
        toggleButton.textContent = "More Comments";
    }
}
