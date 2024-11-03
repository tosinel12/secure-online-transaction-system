document.getElementById('transaction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const amount = document.getElementById('amount').value;
    const currency = document.getElementById('currency').value;
    const recipient = document.getElementById('recipient').value;

    const transactionDetails = {
        amount: amount,
        currency: currency,
        recipient: recipient
    };

    fetch('http://localhost:5000/process_transaction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(transactionDetails)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Transaction successful!');
        } else {
            alert('Transaction failed: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while processing the transaction.');
    });
});
