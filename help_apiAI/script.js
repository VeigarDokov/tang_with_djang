function fetchCryptoData() {
    fetch('api_data.json')
        .then(response => response.json())
        .then(data => {
            const cryptoDataElement = document.getElementById('cryptoData');
            let html = '<ul>';
            data.forEach(coin => {
                html += `<li>${coin.symbol}: ${coin.quote.USD.price}</li>`;
            });
            html += '</ul>';
            cryptoDataElement.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching cryptocurrency data:', error);
        });
}

fetchCryptoData();
setInterval(fetchCryptoData, 60000);
