const csrftoken = getCookie('csrftoken');

const transactionForm = document.getElementById('transaction-form');

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

        // If the POST is successful, reload the page to update the transaction list
        window.location.reload();
    } catch (error) {
        console.error('Request error:', error);
    }
});
