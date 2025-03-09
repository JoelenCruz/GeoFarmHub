const csrftoken = getCookie('csrftoken');

document.getElementById('client-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => { data[key] = value; });

    try {
        const response = await fetch('/api/clients/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert('Error: ' + JSON.stringify(errorData));
            return;
        }

        const newClient = await response.json();
        const tableBody = document.querySelector('#clients-table tbody');
        const newRow = document.createElement('tr');
        newRow.setAttribute('data-client-id', newClient.id);
        newRow.innerHTML = `
          <td>${newClient.id}</td>
          <td>${newClient.name}</td>
          <td>${newClient.email}</td>
          <td>${newClient.phone}</td>
        `;
        tableBody.appendChild(newRow);

        form.reset();
    } catch (error) {
        console.error('Request error:', error);
    }
});
