const toggleMenu = (e) => {

    const menuToggle = document.querySelector('.menu-toggle');
    const menu = document.querySelector('.menu');


    menuToggle.addEventListener('click', () => {
        menu.classList.toggle('hidden');
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            menu.classList.add('hidden');
        }
    }
    );
};

toggleMenu();