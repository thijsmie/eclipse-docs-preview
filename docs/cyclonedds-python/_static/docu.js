window.addEventListener("load", function() {
    let e = document.querySelector(".sphinxsidebarwrapper");
    let ul = document.createElement("ul");
    let path = window.location.href.split('/');
    var root;

    for(var i = 0; i < path.length; ++i) {
        if (path[i] == "docs") {
            root = path.slice(0, i+1).join('/')
        }
    }

    ul.innerHTML = `
        <li class="toctree-l1"><a class="reference internal" href="${root}/index.html">Back to overview</a></li>
    `;
    e.insertBefore(ul, e.firstChild);
    Array(...document.querySelectorAll("dt.py")).forEach((e) => e.classList.add("highlight"));
});
