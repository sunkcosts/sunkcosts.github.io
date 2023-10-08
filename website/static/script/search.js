
document.addEventListener('DOMContentLoaded', function () {
    setInterval(manage_search, 100);
})

function search_expanded() {
    var focus_visible = document.querySelectorAll(".md-search__input.focus-visible");
    return focus_visible.length > 0;
}

function manage_search() {
    var header = document.querySelector('.md-header')
    var drawer_icon = document.querySelector('.md-header__button.md-icon[for="__drawer"]')
    if (search_expanded()) {
        header.style["z-index"] = "11";
    } else {
        drawer_icon.style["z-index"] = "0";
    }
}