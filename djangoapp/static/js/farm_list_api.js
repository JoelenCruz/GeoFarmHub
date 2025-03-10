const farmForm = document.getElementById('farm-form');

farmForm.addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData(farmForm);

    try {
        const response = await fetch('/api/farms/', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert('Erro: ' + JSON.stringify(errorData));
            return;
        }
        window.location.reload();
    } catch (error) {
        console.error('Request error:', error);
    }
});
