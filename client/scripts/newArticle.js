function sendNew() {
    var title = document.getElementById("title").value;
    var content = document.getElementById("content").value;


    var article = {
        title: title,
        content: content,
    };

    fetch('http://localhost:5050/api/new', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(article),
    }).then(() => {
        window.location.href = "index.html"
    })

}