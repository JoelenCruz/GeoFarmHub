const csrftoken = getCookie('csrftoken');

const transactionForm = document.getElementById('transaction-form');
const tableBody = document.querySelector('#transactions-table tbody');

transactionForm.addEventListener('submit', async function (e) {
    e.preventDefault(); 

    const formData = new FormData(transactionForm);

    try {
        const response = await fetch('/api/transactions/', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert('Error: ' + JSON.stringify(errorData));
            return;
        }

        const newTransaction = await response.json();
        console.log('New transaction created:', newTransaction);

        // Update the transactions table dynamically
        const newRow = document.createElement('tr');
        newRow.setAttribute('data-transaction-id', newTransaction.id);
        newRow.innerHTML = `
            <td>${newTransaction.id}</td>
            <td>${newTransaction.client ? newTransaction.client.name : ''}</td>
            <td>${newTransaction.farm ? newTransaction.farm.name : ''}</td>
            <td>${newTransaction.transaction_date}</td>
            <td>$${newTransaction.price}</td>
        `;
        tableBody.appendChild(newRow);

        transactionForm.reset();
    } catch (error) {
        console.error('Request error:', error);
    }
});
