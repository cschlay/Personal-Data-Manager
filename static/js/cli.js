// Output buffer as queue.
var buffer_size = 0;
const MAX_BUFFER_SIZE = 10;

function print(output) {
    let o = document.getElementById('cli-output');

    if (buffer_size > 0) {
        o.appendChild(document.createElement("br"));
    }

    if (buffer_size >= MAX_BUFFER_SIZE) {
        o.removeChild(o.firstChild);    // Removes the text.
        o.removeChild(o.firstChild);    // and the <br> tag.
    }
    else {
        buffer_size += 1;
    }
    o.appendChild(document.createTextNode(output));
}

function toggle() {
    let e = document.getElementById('cli-output');
     e.style.display = (e.style.display == 'block') ? 'none' : 'block';
}

