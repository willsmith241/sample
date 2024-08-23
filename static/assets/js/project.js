document.addEventListener('DOMContentLoaded', () => {
    const projects = [
        {
            title: 'Project One',
            image: 'project1-thumbnail.jpg',
            description: 'Description of Project One.',
            link: 'project.html'
        },
        {
            title: 'Project Two',
            image: 'project2-thumbnail.jpg',
            description: 'Description of Project Two.',
            link: 'project.html'
        }
        // Add more projects here
    ];

    const projectGrid = document.querySelector('.project-grid');

    projects.forEach(project => {
        const projectDiv = document.createElement('div');
        projectDiv.innerHTML = `
            <img src="${project.image}" alt="${project.title}">
            <h3>${project.title}</h3>
            <p>${project.description}</p>
            <a href="${project.link}">View Details</a>
        `;
        projectGrid.appendChild(projectDiv);
    });
});
