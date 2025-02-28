document.getElementById('register-open-btn').addEventListener('click', function () {
    document.getElementById('register-form').style.display = 'block';
});

document.getElementById('login-open-btn').addEventListener('click', function () {
    document.getElementById('login-form').style.display = 'block';
});

document.querySelectorAll('.close-btn').forEach(btn => {
    btn.addEventListener('click', function () {
        this.parentElement.style.display = 'none';
    });
});

// Реєстрація
document.getElementById('register-btn').addEventListener('click', function () {
    const userData = {
        username: document.getElementById('register-username').value,
        email: document.getElementById('register-email').value,
        password: document.getElementById('register-password').value
    };

    fetch('http://127.0.0.1:8000/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert('Реєстрація успішна!');
            document.getElementById('register-form').style.display = 'none';
        } else {
            alert('Помилка: ' + JSON.stringify(data));
        }
    })
    .catch(error => console.error('Помилка:', error));
});

// Вхід (логін)
document.getElementById('login-btn').addEventListener('click', () => {
    const loginData = {
        email: document.getElementById('login-email').value,
        password: document.getElementById('login-password').value
    };

    fetch('http://127.0.0.1:8000/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(loginData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.access) {
            localStorage.setItem('access_token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            alert('Успішний вхід!');
            document.getElementById('login-form').style.display = 'none';
            document.getElementById('logout-btn').style.display = 'inline-block';
        } else {
            alert('Помилка входу: ' + (data.message || 'Невірний логін або пароль'));
        }
    })
    .catch(error => console.error('Помилка:', error));
});




document.getElementById('logout-btn').addEventListener('click', function () {
    // Видаляємо токени з localStorage
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');

    // Перенаправляємо на сторінку входу
    window.location.href = '/login';  // або '/'; для головної сторінки
});
