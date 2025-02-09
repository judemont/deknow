
async function loadPages() {
    const response = await fetch(':5050/api/pages');
    const pages = await response.json();
    pagesContainer.innerHTML = '';
    pages.forEach(page => {
        const pageElement = document.createElement('div');
        pageElement.innerHTML = `
            <h2>${page.title}</h2>
            <p>${page.content}</p>
        `;
        pagesContainer.appendChild(pageElement);
    });
}

loadPages();