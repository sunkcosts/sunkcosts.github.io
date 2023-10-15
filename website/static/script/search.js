function openSearch() {
    search_input.focus()
    search_input.select()
    header.style["z-index"] = "10000";
    search.style["opacity"] = "1";
    quick_search_open = true;
    console.log("open search")
}

function closeSearch() {
    header.style["z-index"] = "0";
    search.style["opacity"] = "0";
    search_input.blur()
    quick_search_open = false;
    console.log("close search")

}

function checkShortcuts(event) {
    if (((event.metaKey || event.ctrlKey) && event.key === 'k') && (!quick_search_open)) {
        openSearch()
    } else if ((((event.metaKey || event.ctrlKey) && event.key === 'k') || (event.keyCode == 27)) && (quick_search_open)) {
        closeSearch();
    }
}

var search = document.querySelector('.md-search')
var search_input = document.querySelector('.md-search__input')
var search_overlay = document.querySelector(".md-search__overlay")
var header = document.querySelector('.md-header')

var quick_search_open = false;

document.onkeydown = checkShortcuts

search_overlay.onclick = function () {
    closeSearch()
}