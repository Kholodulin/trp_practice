document.addEventListener('DOMContentLoaded', function () {
    const helloElement = document.getElementById('hello');
    const changeLanguageButton = document.getElementById('changeLanguage');
    const changeThemeButton = document.getElementById('changeTheme');
    const info1Element = document.getElementById('info1');
    const info2Element = document.getElementById('info2');

    let currentLanguage = 'en';
    let currentTheme = 'light';

    const languages = {
        en: {
            hello: 'Hello, World!',
            changeLanguageButton: 'Change Language',
            changeThemeButton: 'change Theme',
            info1: 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Repellendus deserunt voluptas quo nobis suscipit placeat labore repellat adipisci illo quae reprehenderit nulla amet voluptates non consequuntur, veritatis officiis! Enim, harum.',
            info2: 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Repellendus deserunt voluptas quo nobis suscipit placeat labore repellat adipisci illo quae reprehenderit nulla amet voluptates non consequuntur, veritatis officiis! Enim, harum.',
        },
        ru: {
            hello: 'Привет, мир!',
            changeLanguageButton: 'Изменить язык',
            changeThemeButton: 'изменить тему',
            info1: 'Здравствуйте, за этим действительно больно следить. Отталкиваясь от удовольствия, которое нам нравится, оно отталкивает усилия получить то, чего критикуя, никакие заботы об удовольствиях не достигают, обязанности истины! Для этих',
            info2: 'Здравствуйте, за этим действительно больно следить. Отталкиваясь от удовольствия, которое нам нравится, оно отталкивает усилия получить то, чего критикуя, никакие заботы об удовольствиях не достигают, обязанности истины! Для этих',
        },
    };

    function updateText() {
        helloElement.textContent = languages[currentLanguage].hello;
        changeLanguageButton.textContent = languages[currentLanguage].changeLanguageButton;
        changeThemeButton.textContent = languages[currentLanguage].changeThemeButton;
        info1Element.textContent = languages[currentLanguage].info1;
        info2Element.textContent = languages[currentLanguage].info2;
    }

    function updateTheme() {
        document.body.classList.remove('light-theme', 'dark-theme');
        document.body.classList.add(`${currentTheme}-theme`);
    }

    function toggleTheme() {
        currentTheme = currentTheme === 'light' ? 'dark' : 'light';
        updateTheme();
    }

    changeLanguageButton.addEventListener('click', function () {
        currentLanguage = currentLanguage === 'en' ? 'ru' : 'en';
        updateText();
    });

    changeThemeButton.addEventListener('click', toggleTheme);

    updateText();
    updateTheme();
});
