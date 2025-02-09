

async function loadPages() {
    const pagesContainer = document.getElementById("pages");

    const response = await fetch('http://localhost:5050/api/pages');
    const pages = await response.json();
    pagesContainer.innerHTML = '';
    pages.forEach(page => {
        const pageElement = document.createElement('div');
        pageElement.innerHTML = `
            <li><a href="#" onclick='gotoPage(${page.id})'>${page.title}</a></li>
        `;
        pagesContainer.appendChild(pageElement);
    });
}

loadPages();