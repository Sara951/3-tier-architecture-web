document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;

    fetch('http://localhost:5000/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, age }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('name').value = '';
        document.getElementById('age').value = '';
        fetchData();
    });
});

function fetchData() {
    fetch('http://localhost:5000/data')
    .then(response => response.json())
    .then(data => {
        const dataDisplay = document.getElementById('dataDisplay');
        dataDisplay.innerHTML = '<h3>Submitted Data</h3>' + data.map(item => `<p>${item.name} (Age: ${item.age})</p>`).join('');
    });
}

fetchData();
