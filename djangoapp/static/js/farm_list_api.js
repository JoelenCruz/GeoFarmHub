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

        const newFarm = await response.json();
        console.log('New farm created:', newFarm);

        const tableBody = document.querySelector('#farms-table tbody');
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
      <td>${newFarm.id}</td>
      <td>${newFarm.name}</td>
      <td>${newFarm.owner}</td>
      <td>${newFarm.area_hectares}</td>
    `;
        tableBody.appendChild(newRow);


        farmForm.reset();
    } catch (error) {
        console.error('Request error:', error);
    }
});
